import cv2
import numpy as np
import matplotlib.pyplot as plt


def detect_face(img):
    
    face_img = img.copy()
    
    face_rects = face_cascade.detectMultiScale(face_img, scaleFactor = 1.2, minNeighbors=5)
    
    for (x,y,w,h) in face_rects:
        cv2.rectangle(face_img, (x,y), (x+w,y+h), (0,0,255), 4 )
    
    return face_img


# initializing video capture
cap = cv2.VideoCapture(0)

while True:
    #capturing video from webcam
    ret, frame = cap.read(0)
    # detecting faces in each frame
    frame = detect_face_mod(frame)
 
    cv2.imshow('Video', frame)
    
    k = cv2.waitKey(1)
    if k ==27:
        break
        
cap.release()        
cv2.destroyAllWindows()
