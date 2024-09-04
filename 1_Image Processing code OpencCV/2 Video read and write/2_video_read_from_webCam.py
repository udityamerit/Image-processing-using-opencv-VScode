import cv2 as cv
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv.imshow('frame', frame)
    k = cv.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
