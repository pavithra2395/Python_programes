from imports import *
import settings_roller

class DetectTemplate():
    def __init__(self, img, template_id):
        self.img = img
        self.template = self.get_template_from_template_id(template_id)
    
    def get_template_from_template_id(self, template_id):
        try:
            return [i for i in settings_roller.TEMPLATES if i['template_id'] == template_id][0]
        except:
            pass
        

    def get_w_h(self):
        template = cv2.imread(self.template['template_image'] ,0) 
        w,h = template.shape[::-1]
        return (w,h)

    def detect_frame(self):
        # Read the main image 
        #img_rgb = cv2.imread(frame)
        img_rgb = self.img
        #print(img_rgb)
        # Convert it to grayscale 
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY) 
        # Apply threshold
        #thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15,3)
        #_,thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
        # Read the template 
        template = cv2.imread(self.template['template_image'] ,0) 
        # Store width and height of template in w and h 
        w, h = template.shape[::-1]
        if img_gray.shape[0]>template.shape[0] and img_gray.shape[1]>template.shape[1]:
                # Perform match operations. 
            res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        else:
            print ("Error : Template and image size are: ", template.shape, img_gray.shape)
        # Specify a threshold 
        threshold =self.template['thres'] if 'thres' in self.template else 0.95
        # Store the coordinates of matched area in a numpy array 
        loc = np.where( res >= threshold)
        # Draw a rectangle around the matched region. 
        #for pt in zip(*loc[::-1]): 
            #cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)
        # Show the final image with the matched area. 
        return img_rgb, loc

    # Malisiewicz et al.
    def non_max_suppression_fast(self, boxes, overlapThresh):
      
    # if there are no boxes, return an empty list
        if len(boxes) == 0:
           return []
    
          # if the bounding boxes integers, convert them to floats --
          # this is important since we'll be doing a bunch of divisions
          #'''if boxes.kind == "i":
          #    boxes = boxes.astype("float")'''
    
          # initialize the list of picked indexes    
        pick = []
         
        # grab the coordinates of the bounding boxes
        x1 = boxes[:,0]
        y1 = boxes[:,1]
        x2 = boxes[:,2]
        y2 = boxes[:,3]
        # compute the area of the bounding boxes and sort the bounding
        # boxes by the bottom-right y-coordinate of the bounding box
        area = (x2 - x1 + 1) * (y2 - y1 + 1)
        idxs = np.argsort(y2)
        #print(idxs)
        # keep looping while some indexes still remain in the indexes
        # list
        while len(idxs) > 0:
            # grab the last index in the indexes list and add the
            # index value to the list of picked indexes
            last = len(idxs) - 1
            i = idxs[last]
            pick.append(i)
            suppress = [last]
            # loop over all indexes in the indexes list
            for pos in range(0, last):
                # grab the current index
                j = idxs[pos]
                # find the largest (x, y) coordinates for the start of
                # the bounding box and the smallest (x, y) coordinates
                # for the end of the bounding box
                xx1 = max(x1[i], x1[j])
                yy1 = max(y1[i], y1[j])
                xx2 = min(x2[i], x2[j])
                yy2 = min(y2[i], y2[j])
                # compute the width and height of the bounding box
                w = max(0, xx2 - xx1 + 1)
                h = max(0, yy2 - yy1 + 1)
                # compute the ratio of overlap between the computed
                # bounding box and the bounding box in the area list
                overlap = float(w * h) / area[j]
                # if there is sufficient overlap, suppress the
                # current bounding box
                if overlap > overlapThresh:
                    suppress.append(pos)
             # delete all indexes from the index list that are in the
            # suppression list
            idxs = np.delete(idxs, suppress)
  
          # return only the bounding boxes that were picked
       	return boxes[pick]
