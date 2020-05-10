import cv2
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import cm

#loading the image
solvay = cv2.imread('solvay1.jpg')

# importing the cascade classifier (putting it the the desired directory)
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

#function to detect face
def detect_face(img):
    
    face_img = img.copy()
    
    # returns coordinates of starting point & w , h of detetcted face
    face_rects = face_cascade.detectMultiScale(face_img, scaleFactor = 1.08, minNeighbors=5)
    
    #drawing the rectangle
    for (x,y,w,h) in face_rects:
        cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,0,0), 10 )
    
    return face_img

#now call the function to detect face
detected_faces = detect_face(solvay)


#displaying detected faces
while True:
    
    cv2.imshow('Detected Faces', detected_faces)
    
    k = cv2.waitKey(1) 
    if k == 27:
        break
    
cv2.destroyAllWindows
