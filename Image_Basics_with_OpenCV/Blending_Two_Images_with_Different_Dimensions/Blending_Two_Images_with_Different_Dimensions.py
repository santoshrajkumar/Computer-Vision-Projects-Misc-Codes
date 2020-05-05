# Blending two images of different sizes 

# Here img1 is the main image onto which we want to blend image2 (intel logo) (in the bottom right corner)

import cv2
import matplotlib.pyplot as plt
import numpy as np


#importing images
img1 = cv2.imread('dog_backpack.jpg')
img2 = cv2.imread('intel.png')

# this step of converting is necessary only when we wish to see the image using plt, otherwise you can leave this step
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

#here img2 is of smaller size, so our region of interest's offsets(i.e img1's offset (initial top left corner points are))
x_offset = img1.shape[1]- img2.shape[1]
y_offset = img1.shape[0]- img2.shape[0]

#region of interst in the larger img 1
roi = img1[y_offset:1401, x_offset:934]

#converting to gray image
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

#creating inverse mask of the img2_gray
mask_inv = cv2.bitwise_not(img2_gray)

#applying mask on img2
img2_masked = cv2.bitwise_or(img2, img2, mask = mask_inv)

#final_roi is the bitwise_or b/w img2_masked & roi
final_roi = cv2.bitwise_or(roi,img2_masked)

#assigning the final_roi portion opf img1
img1[y_offset: y_offset+img2.shape[0], x_offset: x_offset + img2.shape[1]] = final_roi

plt.figure(figsize=(15,8))

#the blended image
plt.imshow(img1)
