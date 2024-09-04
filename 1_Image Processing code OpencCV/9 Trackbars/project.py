import cv2 as cv
import numpy as np

# in the np.zeros  the dimention is take the (no of row, no of column)
img = np.zeros((640,640,3), np.uint8)

cv.namedWindow('image')
# define a funciton which is print the value of slider:
def printValue(x):
        print(x)

font = cv.FONT_HERSHEY_COMPLEX
text = 'Welcome to the Electronic model'

img = cv.circle(img, (320,320), 15,(255,255,0), 20)

#creating a trackbar in the window
switch = 'No. of orbit'
cv.createTrackbar(switch, 'image', 1, 10, printValue)

cv.putText(img, text, (10, 30), font, .789, (21,453,212), 2)

s = cv.getTrackbarPos(switch, 'image')


if s == 1:
        img = cv.circle(img, (320, 320), 50, (0, 0, 255), 1)
        cv.imshow('image', img)
elif s == 2:
        img = cv.circle(img, (320, 320), 100, (0, 0, 255), 1)
        cv.imshow('image', img)
elif s == 3:
        img = cv.circle(img, (320, 320), 150, (0, 0, 255), 1)
        cv.imshow('image', img)




cv.waitKey(0)
cv.destroyAllWindows()

