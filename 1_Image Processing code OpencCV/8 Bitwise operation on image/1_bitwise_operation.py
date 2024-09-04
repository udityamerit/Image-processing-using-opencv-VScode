import cv2 as cv
import numpy as np

img = cv.imread('image_1.jpg', 1)
img2 = np.zeros((250, 500, 3), np.uint8)
img2 = cv.rectangle(img2, (100, 40), (300, 200), (255, 255,255), -1)
print(img2.shape)

img = cv.resize(img, (512,512))
img2 = cv.resize(img2, (512,512))

cv.imshow('img', img)
cv.imshow('img2', img2) 

bitand = cv.bitwise_and(img, img2)
bitor = cv.bitwise_or(img, img2)
bitnor1 = cv.bitwise_not(img)
bitnor2 = cv.bitwise_not(img2)

cv.imshow('and', bitand)
cv.imshow('or', bitor)
cv.imshow('nor1', bitnor1)
cv.imshow('nor2', bitnor2)

cv.waitKey(0)
cv.destroyAllWindows()

