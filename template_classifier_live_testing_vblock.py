# %matplotlib inline
# %config InlineBackend.figure_format = 'retina'
import matplotlib.pyplot as plt
import numpy as np
import cv2
import numpy as np
from PIL import Image
import glob
import os
import statistics
import template_matching_classifier_vblock as tm_vblock

def load_template_matching() :
    all_template_ids = tm_vblock.get_template()
    return all_template_ids
    

def predict_image_roller(frame,all_template_ids) :
    status = ""
    temp_results,locs,w,h = tm_vblock.detect_template_in_frame(all_template_ids,frame)
    flag = tm_vblock.set_flag_for_vblock_empty_or_not(temp_results,locs,w,h,frame)
    if flag == 1:
            print("Flag set is {} and Vblock empty".format(flag))
            status = "vblock_empty"
    elif flag == 0:
            print("Flag set is {} and Vblock is not empty".format(flag))
            status = "vblock_not_empty"
    return status

def test_classifier_on_video():
    all_template_ids = load_template_matching()
    cap = cv2.VideoCapture('D:\\LincodeLabsInternship-CatalerProject\\Stage1\\Classifier\\VideoTesting\\Input\\my_video1.mp4')
    #cap = cv2.VideoCapture(1)
    frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))
    #cap.set(cv2.CAP_PROP_FOCUS,16) #top = 5-10, side(right) = 70, vblock 16-20
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    outvid1 = cv2.VideoWriter('D:\\LincodeLabsInternship-CatalerProject\\Stage1\\Classifier\\template_matching_based_classifier\\VideoTesting\\template_matching_vblock.avi',fourcc, 15,(frame_width,frame_height))
    while True:
        ret , frame = cap.read()
        print(type(frame))
        if (ret == 0):
            print("End of video")
            break
        #image = Image.fromarray(frame)
        status  = predict_image_roller(frame,all_template_ids)
        font = cv2.FONT_HERSHEY_SIMPLEX  
        thickness = 2
        print(status)
        frame1 = cv2.putText(frame,(status).upper(), (50,50), font, 0.5, (0, 100, 255),thickness , cv2.LINE_AA)
        cv2.imshow('classifier',frame1)
        outvid1.write(frame1)
        if cv2.waitKey(1) == ord('q'): 
            raise StopIteration
    cap.release()
    cv2.destroyAllWindows()
    
    
test_classifier_on_video()
        
     


