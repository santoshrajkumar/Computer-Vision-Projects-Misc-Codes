import cv2
import numpy as np
import matplotlib.pyplot as plt


#initializing the blank (black background image as numpy array)
img = np.zeros((512,512,3), np.int8)


#function_to_draw_circles on the blank image
def draw_circle(event, x,y, flags, params):
    
    #if left mouse button is pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        #draw circle of Green (0,255,0) color & 50 radius, -1 thickness implies filled circle
        cv2.circle(img, (x,y), 50, (0,255,0), -1)
    #if right mouse button is pressed
    elif event == cv2.EVENT_RBUTTONDOWN:
        #draw circle of Blue (255,0,0) color & 50 radius, -1 thickness implies filled circle
        cv2.circle(img, (x,y), 50, (255,0,0), -1)

#assigning the opencv window
cv2.namedWindow(winname = 'my_img')

# linking mousecallback to the window & drawing function
cv2.setMouseCallback('my_img', draw_circle)


# this loop shows the image on which we can draw & exits when esc is pressed
while True:
    #the OpenCV window (used to show the image to draw)
    cv2.imshow('my_img', img)
    # assigning esc exit key
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()
