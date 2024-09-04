import cv2 as cv
import numpy as np

# creating a window
cv.namedWindow('imageTrackbar')

def printNumber(x):
        print(x)

# creating the trackbar on the window

cv.createTrackbar('cp' , 'imageTrackbar', 0, 400, printNumber )

switch  = 'color\gray'

cv.createTrackbar(switch, 'imageTrackbar',0, 1, printNumber)

while True:
        img  = cv.imread('lena.jpg')


        pos = cv.getTrackbarPos('cp', 'imageTrackbar')
        text = cv.FONT_HERSHEY_COMPLEX
        cv.putText(img, str(pos), (50, 100), text,4 , (234,321,345), 6)

        if cv.waitKey(1) == ord('q'):
                break
        
        s = cv.getTrackbarPos(switch, 'imageTrackbar')

        if s == 0:
                pass
        else:
                img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        
        cv.imshow('imageTrackbar', img)
        

cv.destroyAllWindows()
