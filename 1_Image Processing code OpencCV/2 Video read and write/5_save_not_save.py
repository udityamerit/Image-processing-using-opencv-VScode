import cv2 as cv
cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
copy = cv.VideoWriter('test5.avi', fourcc, 40, (700,500))
while True:
    def saving():
        # cap = cv.VideoCapture(0)
        # fourcc = cv.VideoWriter_fourcc(*'XVID')
        # copy = cv.VideoWriter('test3.avi', fourcc, 40, (700,500))
        while True:
            ret, frame = cap.read()
            if ret:
                gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                cv.imshow('test3', gray)
                copy.write(frame)
                k = cv.waitKey(1)
                if k == ord('s'):
                    print("Video saved successfully")
                    cap.release()
                    copy.release()
                    cv.destroyAllWindows()
                    break
            else:
                break


    def notsaving():
        # cap = cv.VideoCapture(0)
        # cv.namedWindow('test3')
        while True:
            ret, frame = cap.read()
            if ret:
                gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                cv.imshow('test3', gray)
                k = cv.waitKey(1)
                if k == ord('q'):
                    print("Video terminated successfully")
                    cap.read()
                    cv.destroyAllWindows()
                    break
            else:
                break

    print("Please Enter the option to operate on the function:\n press -->1 for saving the video:\n press -->2 for not saving the video:\n ")
    press = int(input())
    if press == 1:
        saving()
        break
    elif press == 2:
        notsaving()
        break
    else:
        print("Try again press only given commands:")
        break



