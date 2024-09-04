import cv2 as cv

import numpy as np

def printingvalue(x):
        print(x)

img = np.zeros((553,553,3), np.uint8)
cv.namedWindow('image')

# add the trackbar in the window:

cv.createTrackbar('B', 'image', 0, 255,printingvalue)
cv.createTrackbar('G', 'image', 0, 255,printingvalue)
cv.createTrackbar('R', 'image', 0, 255,printingvalue)

# creating the switch on the window:

Switch = '0: OFF\n 1: ON'
cv.createTrackbar(Switch, 'image', 0, 1,printingvalue)

while True:
        cv.imshow('image', img)
        
        if  cv.waitKey(1) == ord('q'):
                break


# this is used for get the value of b, g, r channal in the image so that it is change the value of color is changes:

        b = cv.getTrackbarPos('B', 'image')
        g = cv.getTrackbarPos('G', 'image')
        r = cv.getTrackbarPos('R', 'image')
        s = cv.getTrackbarPos(Switch, 'image')

# display the color on the screen: 

        if s == 0:
                img[:] = 0
        else: 
                img[:] = [b, g, r]

cv.destroyAllWindows()