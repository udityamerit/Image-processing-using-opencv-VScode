import cv2 as cv
img = cv.imread('messi5.jpg', 1)
img2 = cv.imread('butterfly.jpg', 1)

# resizing the image use the function and give the source and then the second argument is in the form of tuple which contain the number of the rows and column:

img = cv.resize(img, (512, 512))
img2 = cv.resize(img2, (512, 512))

# this function is used to add or merg two images:
dst = cv.add(img, img2)

# how we can use the transperancy of the image it is called the addWeighted it is contain (img, trancperancy of first img, img2, trancperancy of second img, gama(it is the scalar value))
tra = cv.addWeighted(img, 0.8, img2, 0.2, 4)

cv.imshow('addweighted', tra)

# cv.imshow('adding', dst)
cv.waitKey(0)
cv.destroyAllWindows()
