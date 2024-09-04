import cv2 as cv

import datetime
cap = cv.VideoCapture(0)
# fourcc = cv.VideoWriter_fourcc(*"XVID")

# Supporting the Mp4 flile codec is AVC, DivX, Xvid, MPEG4, MPEG2, AVCHD.
fourcc = cv.VideoWriter_fourcc(*"Xvid")

# duplicate  = cv.VideoWriter('folder5_1.avi',fourcc, 30.0, (1280,720))
# duplicate  = cv.VideoWriter('folder5_1.avi',fourcc, 30.0, (640, 480))
duplicate  = cv.VideoWriter('Test6_1.mp4',fourcc, 30.0, (640, 480))

# this is set the max resulution of your camera parameter which is availabe in your default  which is (1280 and 720 )
# cap.set(3,3000)
# cap.set(4,3000)

cap.set(3,700)
cap.set(4,500)

while True:
        ret , frame = cap.read()
        if ret:
                gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV_FULL)

                font = cv.FONT_HERSHEY_COMPLEX # this is use for selecting the font 

                text = "Width:"+ str(cap.get(3)) + "  Height:"+ str(cap.get(4)) # this is use for add the texts

                text1 = "   Image processing"
                text2 = text +text1
                # this is used for add the text of the video screen
                ''' here the putText take the argument:  
                1==> source where you want to add the Text
                2==> text variable where you have to save the text
                3==> origin point where it start
                4==> type of font
                5==> font scale (how big font show on the image or video)
                6==> color
                7==> thickness
                ''' 
                cv.putText(frame, text2, (10,50), font, 1, (255,456,0), 3,)

                #put the text on the another video
                cv.putText(hsv, text2, (10,50), font, 1, (255,456,0), 3,)
               

                # put the current time and date on the video frame:
                date = str(datetime.datetime.now())
                ''' here the putText take the argument:  
                1==> source where you want to add the Text
                2==> date variable where you have to save the text
                3==> origin point where it start
                4==> type of font
                5==> font scale (how big font show on the image or video)
                6==> color
                7==> thickness
                ''' 
                cv.putText(frame, date, (10,100), font, 1, (255,456,0), 3,)


                cv.putText(hsv, date, (10,100), font, 1, (255,456,0), 3,)

                # draw the shaps on the video:
                # frame = cv.circle(frame, (300, 500), 10, (0,234,213), -1)

                ''' here the rectangle take the argument:  
                1==> source where you want to add the rectangle
                2==> starting point of the Geometry (x,y) coordinate
                3==> ending point of the Geometry (x,y) coordinate
                4==> color in form of (B, G, R)
                5==> thickness of the rectangle

                'but the variable name is same as like if you work on the video then the variable is frame whare it read the video in case of the image the variable is same image name'
                ''' 
                frame = cv.rectangle(frame, (5,150), (600, 250), (234,5890,0), -1)
                # frame = cv.arrowedLine(frame, (40,330), (40, 230), (55,255,255), 4)

                text4 = 'Name: Uditya Narayan Tiwari' 
                cv.putText(frame, text4, (10,200), font, 1, (255,0,0), 3,)

                cv.putText(hsv, text4, (10,200), font, 1, (255,0,0), 3,)

                frame = cv.line(frame, (10,210), (540,210), (234,40,321),3)
                

                # duplicate.write(hsv)
                # duplicate.write(gray)
                duplicate.write(frame)

                cv.imshow('folder5', hsv)
                cv.imshow('test1', frame)
                cv.imshow('test2', gray)

                if cv.waitKey(1) == ord('q'):
                        break
        else:
                break
cap.release()
cv.destroyAllWindows()
