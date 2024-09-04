import cv2 as cv
img = cv.imread('messi5.jpg', 1)
b,g,r= cv.split(img)
img = cv.merge((b,g,r))

print(img.shape) 
print(img.size)
print(img.dtype)

# copy the ball and past the other place
'''
first select the region of the object and than the select the place where you want to add the object  assigne the value of ball in that region'''

ball = img[300:340, 350:410] #here the img[] contain the place of the ball or coordinate of the ball 

img[293:333, 120:180] = ball
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
