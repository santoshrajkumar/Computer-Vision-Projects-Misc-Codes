import cv2
import numpy as np
import matplotlib.pyplot as plt

#just a function to open image using matplotlib.pyplot in bigger size
def show_img(img):
    plt.figure(figsize = (12,10))
    return plt.imshow(img, cmap = 'gray')

#importing original image
scenery = cv2.imread('scenery.jpg')


#creating a copy for applying algorithom
img = scenery.copy()

#  applying median blur
img = cv2.medianBlur(img, 15)

# coverting img to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#thresholding with OTSU's method 
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

#noise removal with morphological opening operation
kernel = np.ones((3,3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations =1)


# sure background area
sure_bg = cv2.dilate(opening,kernel,iterations=3)


# applying distance transform
dist_tr = cv2.distanceTransform(opening, cv2.DIST_L2, 5)

# thresholding distance transformed image
ret, sure_fg = cv2.threshold(dist_tr, 0.01*dist_tr.max(), 255,0)

#sure foreground
sure_fg = np.uint8(sure_fg)

#subtracting sure back & foregrounds
unknown = cv2.subtract(sure_bg, sure_fg)

#defining markers
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0

# applying watershed method
markers = cv2.watershed(img, markers)

#calculating contours 
contours, hierarchy = cv2.findContours(markers.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

#drawing contours
for i in range(len(contours)):
    if hierarchy[0][i][3] == -1:
        cv2.drawContours(scenery, contours,i,(255,0,0), 2)

#shwoing watersheded image
show_img(scenery)


