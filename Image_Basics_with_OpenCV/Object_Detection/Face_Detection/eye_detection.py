# -*- coding: utf-8 -*-
"""
Created on Sun May 10 10:35:14 2020

@author: Santosh
"""

import cv2
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import cm

#loading the image
img = cv2.imread('Nadia_Murad.jpg')

# importing the cascade classifier (putting it the the desired directory)
eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

#function to detect eyes
def detect_eyes(img):
    
    face_img = img.copy()
    
    # returns coordinates of starting point & w , h of detetcted eyes
    eyes_rects = eye_cascade.detectMultiScale(face_img, scaleFactor = 1.2, minNeighbors=5)
    
    #drawing the rectangle
    for (x,y,w,h) in eyes_rects:
        cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,0,0), 10 )
    
    return face_img

#now call the function to detect eyes
detected_faces = detect_eyes(img)


#displaying detected faces
while True:
    
    cv2.imshow('Detected Faces', detected_faces)
    
    k = cv2.waitKey(1) 
    if k == 27:
        break
    
cv2.destroyAllWindows()
