import cv2 as cv

cap = cv.VideoCapture(0)
print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# cap.set(3,1280)
# cap.set(4, 720)
 
# set function set the maximum resulution of your camera and show it :

cap.set(3,30000) 
cap.set(4, 30000)

print(cap.get(3))
print(cap.get(4))

while True:
        ret, frame = cap.read()
        if ret:
                hsv = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)
                cv.imshow('test', hsv)
                k = cv.waitKey(1)
                if k == ord('q'):
                        break
        else:
                break
cap.release()
cv.destroyAllWindows()
