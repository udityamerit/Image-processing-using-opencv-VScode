import cv2 as cv
import numpy as np

def click_event(event, x, y, flags, params):

        
        if event == cv.EVENT_LBUTTONDOWN:
                
                cv.circle(img, (x, y), 5,(234,234,234), -1)
                points.append((x, y))
                if len(points)>=2:
                        cv.line(img, points[-1], points[-2],(345,543,213), 3)
                cv.imshow('image',img)



img = np.zeros((512,512,3), np.uint8)
# img = cv.imread('butterfly.jpg',1)
cv.imshow('image', img)
points = []
cv.setMouseCallback('image', click_event)

cv.waitKey(0)
cv.destroyAllWindows()