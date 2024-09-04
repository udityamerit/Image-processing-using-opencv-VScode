

#  Saving the video in the system file


# import cv2 as cv
# cap = cv.VideoCapture(0)
# fourcc = cv.VideoWriter_fourcc(*'XVID')
# copy = cv.VideoWriter('function.avi', fourcc, 30.0, (640, 480))
# while True:
#     ret, frame = cap.read()
#
#     if ret:
#         gray = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)
#         cv.imshow('frame', gray)
#         print(gray)
#         copy.write(frame)
#         k = cv.waitKey(1)
#         if k == ord('s'):
#             # copy.write(frame)
#             break
#
#         # if k == ord('q'):
#         #     break
#     else:
#         break


import cv2 as cv
cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
copy = cv.VideoWriter('function.avi', fourcc, 30.0, (640, 480))
def saving():
    while True:
        ret, frame = cap.read()
        if ret:
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            cv.imshow('test1', gray)
            copy.write(frame)
            k = cv.waitKey(1)
            if k == ord('s'):
                print("Video saved successfully")
                break
        else:
            break

def notsaving():
    while True:
        ret, frame = cap.read()
        if ret:
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            cv.imshow('test1', gray)
            k = cv.waitKey(1)
            if k == ord('q'):
                print("Video terminated successfully")
                break
        else:
            break


print("Please Enter the option to operate on the function:\n press -->1 for saving the video:\n press -->2 for not saving the video:\n ")
press = int(input())
if press == 1:
    saving()
elif press == 2:
    notsaving()
else:
    print("Try again press only given commands:")


cap.release()
copy.release()
cv.destroyAllWindows()


