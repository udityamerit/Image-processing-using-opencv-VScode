import cv2
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
copy = cv2.VideoWriter('practice.avi', fourcc, 30.0, (640, 480))
while cap.isOpened():
        ret, frame = cap.read()
        if ret:
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV_FULL)
                copy.write(gray) # 
                cv2.imshow('frame',gray)
                k = cv2.waitKey(1)
                if k == ord('q'):
                        break
        else:
                break
cap.release()
copy.release()
cv2.destroyAllWindows()

