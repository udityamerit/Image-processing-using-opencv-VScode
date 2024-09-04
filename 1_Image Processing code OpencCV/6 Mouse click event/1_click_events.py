import cv2 as cv
import numpy as np

def click_event(event, x, y, flags, params):

        # use this function to show the coordinate of the image when you clicked the mouse button

        if event == cv.EVENT_LBUTTONDOWN:
                print(x,', ',y)
                font = cv.FONT_HERSHEY_COMPLEX
                strxy = str(x) + ', '+ str(y)
                cv.putText(img, strxy, (x,y), font, 1, (255, 345,0), 1)
                cv.imshow('image', img)

        # this is show the BGR channel of right click
        if event == cv.EVENT_RBUTTONDOWN:
                font = cv.FONT_HERSHEY_COMPLEX

                blue = img[y,x,0]
                green = img[y, x, 1]
                red = img[y,x,2]

                BGR = str(blue)+ ', '+ str(green)+ ', '+ str(red)
                cv.putText(img, BGR, (x,y), font, .7, (0,255,0),1)
                cv.imshow('image', img)


img = np.zeros((512,512,3), np.uint8)
img = cv.imread('butterfly.jpg',1)
cv.imshow('image', img)
cv.setMouseCallback('image', click_event)

cv.waitKey(0)
cv.destroyAllWindows()

        
