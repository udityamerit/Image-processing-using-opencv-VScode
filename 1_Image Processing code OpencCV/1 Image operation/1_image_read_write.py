import cv2
import numpy as np
# cv2 module are provides the function to read and write the images

# img = cv2.imread("lena.jpg", 1)
img1 = cv2.imread("ml.png", 0)
# ''' in the imread function the "first argument" is take the location of file
#     or name of the file and "second argument" is take the "flag" which is [0,1,-1]
#     0 means your image is show in the gray color scale.
#     1 means you image is shows in the RGB color scale.
#    -1 means your image is shows in the alpha scale means high saturation values.
# '''
# print(img)
# print(img1)
#
# cv2.imshow('image', img)
# cv2.imshow("image1", img1)
# ''' imshow is used to display the image on the system, and first argument
#   is take the name of your display window . '''
#
# cv2.waitKey(0)
# # waitKey (0) is used to send a command to the system to wait until user is not close the image manually
#
#
# cv2.destroyAllWindows()
# # destroyAllWindows() is used to destroy all the windows which is creating by the imshow() method


# code to save the photos on the system:
cv2.imshow("original", img1)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("ml_copy.png", img1)
    cv2.destroyAllWindows()
