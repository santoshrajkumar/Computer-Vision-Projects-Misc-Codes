import cv2
import numpy as np
import time



# initiating Cascade Classifier (make sure the xml file in the same directory)
russian_plate_detector = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

def detect_plate(img):
    
    # detecting plates using classfier
    russian_detect = russian_plate_detector.detectMultiScale(img, scaleFactor = 1.12, minNeighbors = 5)
    
    # drawing rectangles
    for (x,y,w,h) in russian_detect:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 4)
        
    return img

# loading the video file
cap = cv2.VideoCapture('video file directory')

#if video is opneded
if cap.isOpened()== False:
    print("Error file not found or wrong, codec used")

# selecting fps
fps = 20

while cap.isOpened():
    
    ret, frame = cap.read()
    
    if ret == True:
        time.sleep(1/fps)
        frame = detect_plate(frame)
        
        cv2.imshow('frame', frame)
        
        #press q to exit
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
            
    else:
        break

        
cap.release()
cv2.destroyAllWindows()
