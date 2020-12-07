import glob
import imageio
import imgaug as ia
import imgaug.augmenters as iaa
import numpy as np
import os,shutil
import xml.etree.ElementTree as ET
import xml
import cv2
import xmltodict
import json
import xml.etree.cElementTree as e
import numpy as np
import uuid 
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
import sys
import time
import threading
from multiprocessing import Process

source_path = "D:\\lincode\\22-09-2020\\batch\\batch_83"
dest_path = "D:\\lincode\\22-09-2020\\batch\\batch_83_aug\\"
augment_list = ['flip_hr','flip_vr','affine','contrast','rotate','brightness']#'rotate','flip_hr','flip_vr',,'resize','crop',


##Augmentations
#rotate
rotate=iaa.Affine(rotate=(-50, 30))
#flipping image verically
flip_vr=iaa.Flipud(p=1.0)
#flipping image horizontally
flip_hr=iaa.Fliplr(p=1.0)
#Affine
move=iaa.Affine(translate_percent={"x": 0.1,"y": 0.1}, scale=0.8)
#contrast
contrast=iaa.GammaContrast(gamma=2.0)
#resize
resize = iaa.Resize({"height": 480, "width": 640})#"height": 480, "width": 640
#crop
crop = iaa.CenterCropToFixedSize(height=300, width=650)
#brightness
brightness = iaa.WithBrightnessChannels(iaa.Add((-50, 50)))




augmentations = {'rotate':rotate,'flip_hr':flip_hr,'flip_vr':flip_vr,'affine':move,'contrast':contrast,'resize':resize,'crop':crop,
                'brightness':brightness}

def create_directory(directory):#create directory
    try:
        os.makedirs(directory)
    except:
        print('directory already exists!!')

def del_create_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)  # delete output folder
        print(directory ,' already exists!!')
        print(directory ,'Removed')
        os.makedirs(directory)
    else:
        os.makedirs(directory) # make new output folder
    print(directory , ' created!')

def read_xml2json(file):
    with open(file) as xml_file:
        my_dict=xmltodict.parse(xml_file.read())
    xml_file.close()
    json_data=json.dumps(my_dict)
    jason = json.loads(json_data)
    # print(file ,'converted to json!')
    return jason

def read_image(jason,source_path):
    img_file = jason['annotation']['filename']
    image = imageio.imread(source_path+'/'+img_file)
    # print(img_file ,' Image found!!')
    return image

def unique_id():
    id = uuid.uuid4() 
    return id

def uid_rename_file(jason):
    id = unique_id()
    img_file = jason['annotation']['filename']
    img_name = img_file.replace(img_file[-4],str(id)+img_file[-4])
    xml_name = img_name.replace(img_name[-4:],'.xml')
    return img_name,xml_name

def aug_rename_file(jason,aug):
    id = str(aug)
    img_file = jason['annotation']['filename']
    img_name = img_file.replace(img_file[-4],str(id)+img_file[-4])
    xml_name = img_name.replace(img_name[-4:],'.xml')
    return img_name,xml_name

def objects_coord_aug(jason,augment,image):#json format and which augumantation and image
    object_list = []
    # print(type(jason['annotation']['object']))
    # print(len(jason['annotation']['object']))
    # for i,x in enumerate(jason['annotation']['object']):
    object_dict = {'name': '',
    'pose': 'Unspecified',
    'truncated': '0',
    'difficult': '0',
    'bndbox': {}}
    x = jason['annotation']['object']
    x1,y1,x2,y2 = x['bndbox']['xmin'],x['bndbox']['ymin'],x['bndbox']['xmax'],x['bndbox']['ymax']
    bbs = BoundingBoxesOnImage([BoundingBox(x1=int(x1), x2=int(x2), y1=int(y1), y2=int(y2))], shape=image.shape)
    image_aug, bbs_aug = augment(image=image, bounding_boxes=(bbs))
    coordinates = bbs_aug.to_xyxy_array()
    xmin,ymin,xmax,ymax = (coordinates[0][0]),(coordinates[0][1]),(coordinates[0][2]),(coordinates[0][3])  
    # print(xmin,ymin,xmax,ymax)
    object_dict['name']=x['name']
    object_dict['bndbox']= {'xmin':int(xmin),'ymin':int(ymin),'xmax':int(xmax),'ymax':int(ymax)} 
    object_list=(object_dict)
    # print(object_list)
    return object_list,image_aug

#augmentation of img and bnd_box
def multi_objects_coord_aug(jason,augment,image):
    bbs_list = []
    object_list = []
    for i,x in enumerate(jason['annotation']['object']):#read the boubding box from the json 
        x1,y1,x2,y2 = int(x['bndbox']['xmin']),int(x['bndbox']['ymin']),int(x['bndbox']['xmax']),int(x['bndbox']['ymax'])
        # print(x1,y1,x2,y2)
        bbs_list.append(BoundingBox(x1=int(x1), x2=int(x2), y1=int(y1), y2=int(y2),label = str(x['name'])))
        bbs = BoundingBoxesOnImage(bbs_list,shape=image.shape)   
        image_aug, bbs_aug = augment(image=image, bounding_boxes=(bbs))#augments the image and bounding boxes
    for i,x in enumerate(jason['annotation']['object']):
        object_dict = {'name': '',
        'pose': 'Unspecified',
        'truncated': '0',
        'difficult': '0',
        'bndbox': {}}
        # print(bbs_aug[i].x1_int)
        xmin,ymin,xmax,ymax = bbs_aug[i].x1_int,bbs_aug[i].y1_int,bbs_aug[i].x2_int,bbs_aug[i].y2_int
        # print(xmin,ymin,xmax,ymax)
        object_dict['name']=x['name']
        object_dict['bndbox']= {'xmin':int(xmin),'ymin':int(ymin),'xmax':int(xmax),'ymax':int(ymax)} 
        object_list.append(object_dict)
    # print(object_list)
    return object_list,image_aug


def edit_jason(jason,object_list,aug): #Edit the json
    img_name,xml_name = aug_rename_file(jason,aug)
    jason['annotation']['folder'] = str(dest_path.split('/')[-1])
    jason['annotation']['path'] = dest_path + img_name
    jason['annotation']['filename'] = img_name
    jason['annotation']['object'] = object_list
    
    return jason,img_name,xml_name

def write_xml(jason,xml_name,dest_path): #converts json to xml and writes xml
    d = jason
    r = e.Element("annotation")
    e.SubElement(r,"folder").text = d['annotation']["folder"]
    e.SubElement(r,"filename").text = d['annotation']["filename"]
    e.SubElement(r,"path").text = str(d['annotation']["path"])
    source_ = e.SubElement(r,"source")
    e.SubElement(source_,'database').text = str(d['annotation']["source"]['database'])
    size_ = e.SubElement(r,"size")
    e.SubElement(size_,'width').text = str(d['annotation']["size"]['width'])
    e.SubElement(size_,'height').text = str(d['annotation']["size"]['height'])
    e.SubElement(size_,'depth').text = str(d['annotation']["size"]['depth'])


    e.SubElement(r,"segmented").text = str(d['annotation']["segmented"])
 
    if type(jason['annotation']['object']) == list:
        for i,z in enumerate(d['annotation']["object"]):
            exec(f'object_{i}= e.SubElement(r,"object")') 
            exec(f'e.SubElement(object_{i},"name").text = str(z["name"])')
            exec(f'e.SubElement(object_{i},"pose").text = str(z["pose"])')
            exec(f'e.SubElement(object_{i},"truncated").text = str(z["truncated"])')
            exec(f'e.SubElement(object_{i},"difficult").text = str(z["difficult"])')
            exec(f'bndbox_{i} = e.SubElement(object_{i},"bndbox")')
            exec(f"e.SubElement(bndbox_{i},'xmin').text = str(z['bndbox']['xmin'])")
            exec(f"e.SubElement(bndbox_{i},'ymin').text = str(z['bndbox']['ymin'])")
            exec(f"e.SubElement(bndbox_{i},'xmax').text = str(z['bndbox']['xmax'])")
            exec(f"e.SubElement(bndbox_{i},'ymax').text = str(z['bndbox']['ymax'])")
    else:
        i =0
        z = jason['annotation']['object']
        exec(f'object_{i}= e.SubElement(r,"object")') 
        exec(f'e.SubElement(object_{i},"name").text = str(z["name"])')
        exec(f'e.SubElement(object_{i},"pose").text = str(z["pose"])')
        exec(f'e.SubElement(object_{i},"truncated").text = str(z["truncated"])')
        exec(f'e.SubElement(object_{i},"difficult").text = str(z["difficult"])')
        exec(f'bndbox_{i} = e.SubElement(object_{i},"bndbox")')
        exec(f"e.SubElement(bndbox_{i},'xmin').text = str(z['bndbox']['xmin'])")
        exec(f"e.SubElement(bndbox_{i},'ymin').text = str(z['bndbox']['ymin'])")
        exec(f"e.SubElement(bndbox_{i},'xmax').text = str(z['bndbox']['xmax'])")
        exec(f"e.SubElement(bndbox_{i},'ymax').text = str(z['bndbox']['ymax'])")

    a = e.ElementTree(r)
    a.write(dest_path+xml_name)

def write_image(dest_path,image_aug,img_name):
    imageio.imwrite(dest_path+img_name, image_aug)


def aug_img_bndbox( source_path,dest_path ,augment_list):
    del_create_directory(dest_path)
    for xml in sorted(glob.glob(source_path + '/*.xml')):
        for aug in augment_list:
            jason = read_xml2json(xml)
            image = read_image(jason,source_path)
            augment = augmentations[aug]
            try:
                object_list,image_aug = multi_objects_coord_aug(jason,augment,image)                
                # if type(jason['annotation']['object']) == dict:
                    # print('dict yes')
            except:
                # else:
                    # print('list yes')
                object_list,image_aug = objects_coord_aug(jason,augment,image)
            jason,img_name,xml_name = edit_jason(jason,object_list,aug)
            write_xml(jason,xml_name,dest_path)
            write_image(dest_path,image_aug,img_name)
            print(xml , aug ,'augmented !')



if __name__ == "__main__":
    start_time = time.time()
    # aug_img_bndbox(source_path,dest_path,augment_list)
    p = Process(target=aug_img_bndbox,args=[source_path,dest_path,augment_list])
    p.start()
    p.join()

    end_time = time.time()
    time_elapsed = end_time - start_time
    print(start_time)
    print(end_time)
    print('Time elapsed ', time_elapsed ,' secs')

# if __name__ == "__main__":
#     start_time = time.time()
#     # aug_img_bndbox(source_path,dest_path,augment_list)
#     thread_one = threading.Thread(target=aug_img_bndbox,args=[source_path,dest_path,augment_list])
#     thread_two = threading.Thread(target=aug_img_bndbox,args=[source_path,dest_path,augment_list])
#     thread_one.start()
#     thread_two.start()
#     thread_one.join()
#     thread_two.join()
#     end_time = time.time()
#     time_elapsed = end_time - start_time
#     print(start_time)
#     print(end_time)
#     print('Time elapsed ', time_elapsed ,' secs')


