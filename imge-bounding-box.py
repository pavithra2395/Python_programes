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
import sys
import time
import threading
from multiprocessing import Process

source_path = "D:\\puppies\\images"
dest_path = "D:\\puppies\\images\\"


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


if __name__ == "__main__":
    start_time = time.time()
    # aug_img_bndbox(source_path,dest_path,augment_list)
    p = Process(args=[source_path,dest_path])
    p.start()
    p.join()

    end_time = time.time()
    time_elapsed = end_time - start_time
    print(start_time)
    print(end_time)
    print('Time elapsed ', time_elapsed ,' secs')
