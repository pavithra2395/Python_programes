# template matching 
import cv2 
import numpy as np 
import settings_roller
from utils_roller import DetectTemplate
from collections import Counter

def get_template():
    print("Inside get_template Function")
    all_template_ids = [i.get('template_id') for i in settings_roller.TEMPLATES]
    return all_template_ids

def detect_template_in_frame(all_template_ids,frame):
    temp_results = []
    for id in all_template_ids:
        print(id)
        print(frame)
        db, locs = DetectTemplate(frame, id).detect_frame()
        w,h = DetectTemplate(frame,id).get_w_h()
        temp_results.append([locs,w,h])
    return temp_results,locs,w,h

def set_flag_for_roller_empty_or_not(temp_results,locs,w,h,frame):
    flag = 0
    for item in temp_results:
        loc,w,h = item
        iou = []
        rectangles = []
        for pt in zip(*loc[::-1]): 
    
            x1 = pt[0]
            y1 = pt[1]
            x2 = pt[0]+w
            y2 = pt[1]+h
            rect = np.array([(x1,y1,x2,y2)])
            rectangles.append(rect)
                
            for bboxes in rectangles:
                iou = DetectTemplate(frame, id).non_max_suppression_fast(bboxes, 0.9)
                #print("The computed iou:",iou)
                  
                if iou is not None:
                    #print("Roller is empty")
                    #cv2.putText(frame, "Roller is empty", (200,40), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0),  1, cv2.LINE_AA)
                    flag = 1 #set flag for roller is empty
                    break        
    return flag


    

    


    
    

