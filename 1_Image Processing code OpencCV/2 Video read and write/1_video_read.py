# Video reading using the files in the system

import cv2 as cv
cap = cv.VideoCapture('Megamind_bugy.avi')
# cv.VideoCapture is take the argument as the name of the video which name it is stored

cv.namedWindow("test1")

while True:
    ret, vid = cap.read()
    if ret:
        cv.imshow('test1', vid)
        print(vid)  # this is used for the printing the matrix of the video.
        if cv.waitKey(23) == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()



