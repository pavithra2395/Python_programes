import glob
import os
import xml.etree.ElementTree as ET
import cv2

path = '/home/digital/Desktop/batch_154_1'
count = 0

for file in glob.glob(os.path.join(path,'*.xml')):
#     print((file.split('/')[-1]).split('.')[0])
    tree = ET.parse(file)
    file_name = (tree.find('filename').text.replace(' (', '_')).replace(')','')
    full_path = os.path.join('/home/digital/Desktop/batch_154/',file_name)
    tree.find('filename').text = file_name
    tree.find('path').text = full_path
    print(file,tree.find('path').text)
       
#     for elt in tree.iter():
#         if((elt.tag == 'name') & (elt.text == 'Crack')):
#             print(file)
#             elt.text = 'crack'
#             count += 1
#     tree.find('filename').text = (file.split('/')[-1]).split('.')[0] + '.jpg'
    #tree.write(file)

# print(count)
