import cv2 as cv

cap = cv.VideoCapture(0)  # this is use for the capturing the video form the webcam

fourcc = cv.VideoWriter_fourcc(*'Xvid')  # this is use for the fourcc codec which is said that what type of mode it is going to save.

# copy = cv.VideoWriter('copy video.avi', fourcc, 30.0, (640, 480))  # this is use fot the write the video in the given fourcc codec

copy = cv.VideoWriter('copy_video.mp4', fourcc, 30.0, (640, 480))  # this is use fot the write the video in the given fourcc codec
''' 
in this function 1--> argument contain the name of your file and type
    2--> argument contain the fourcc codec
    3--> argument contain the frame rate
    4--> argument contain the resulution of your camera in the form of the tuple
'''

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # getting the width of the video:
        W = cap.get(cv.CAP_PROP_FRAME_WIDTH)
        print(W)

        # getting the height of the video:
        H = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
        print(H)

        # change the color of the video capture
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # call the function so that we save the copy the system
        copy.write(frame)

        cv.imshow('frame', gray)
        k = cv.waitKey(1)
        # if k == ord('s'):
        #     copy.write(frame)

        if k == ord('q'):
            break

    else:
        break

cap.release()
copy.release()
cv.destroyAllWindows()
