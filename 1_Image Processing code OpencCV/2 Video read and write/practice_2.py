
#  Saving the video in the system file

import cv2 as cv
cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
copy = cv.VideoWriter('copy.avi', fourcc, 30.0, (640, 480))
while True:
    ret, frame = cap.read()

    if ret:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('test3', gray)
        copy.write(frame)
        
        print(gray)
        k = cv.waitKey(1)
        if k == ord('s'):
            break
    else:
        break

cap.release()
copy.release()
cv.destroyAllWindows()