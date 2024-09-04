import cv2 as cv
import numpy as np

img = cv.imread('ml.png', 1)
img2 = cv.imread('lena.jpg', 0)
img3 = cv.imread('messi5.jpg', 1)

# creating the image using the numpy
# img = np.zeros([519,321,3],np.uint8)

# text on the image
font = cv.FONT_HERSHEY_COMPLEX
img = cv.putText(img, "What!", (10,50), font, 1, (321,45,32), 2)
cv.imshow("imagetext", img)

# geometry on the image
'''
here the rectangle take the argument:  
                1==> source where you want to add the rectangle
                2==> starting point of the Geometry (x,y) coordinate
                3==> ending point of the Geometry (x,y) coordinate
                4==> color in form of (B, G, R)
                5==> thickness of the rectangle
'''

img = cv.line(img,(34, 32), (255, 234), (233, 0, 213), 4)
img = cv.circle(img, (56, 56), 50, (123, 123, 123), -1)
img2 = cv.rectangle(img2, (23, 23), (100, 100), (253, 0, 0), -1)
img2 = cv.ellipse(img2,(89,50), (3,4), 0,0, 270,(255,0,0), 300)

cv.imshow('line', img)
cv.imshow('img2test', img2)
print("size of the img")
print(img.shape)
# print(img)
cv.waitKey(0)
cv.destroyAllWindows()
