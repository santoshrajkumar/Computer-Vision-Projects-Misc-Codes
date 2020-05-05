import cv2
import numpy as np
import matplotlib.pyplot as plt

#initializing the blank (black background image as numpy array)
img = np.zeros((1512,1512,3))

drawing = False
ix = -1
iy = -1

#function_to_draw rectangles on the blank image
def draw_rectangle(event, x,y, flags, params):
    global ix, iy, drawing
    
    #if left mouse button is pressed 
    if event == cv2.EVENT_LBUTTONDOWN:
        #start drawing
        drawing = True
        ix, iy = x,y
    #when the mouse moves    
    elif event == cv2.EVENT_MOUSEMOVE:
        # if drawing is on
        if drawing == True:
            #show drawn rectangle
            cv2.rectangle(img, (ix,iy), (x,y), (0,0,255), -1)
    #when button released
    elif event == cv2.EVENT_LBUTTONUP:
        # drawing stops
        drawing = False
        #draw the completed circle
        cv2.rectangle(img, (ix,iy), (x,y), (0,0,255), -1)

#assigning the opencv window
cv2.namedWindow(winname = 'my_img')

# linking mousecallback to the window & drawing function
cv2.setMouseCallback('my_img', draw_rectangle)


# this loop shows the image on which we can draw & exits when esc is pressed
while True:
    #the OpenCV window (used to show the image to draw)
    cv2.imshow('my_img', img)
    # assigning esc exit key
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()
