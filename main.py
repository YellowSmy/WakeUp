import cv2 as opencv
import webbrowser
import time

from detect import detector
from detect import _blinking_detect
#from vibe import _vive

## value
passed_time = 0;


##webcam set
capture = opencv.VideoCapture(opencv.CAP_DSHOW+0)
capture.set(opencv.CAP_PROP_FRAME_WIDTH, 640)
capture.set(opencv.CAP_PROP_FRAME_HEIGHT, 480)

while True :
    _, image = capture.read()

    # convert frame to gray
    gray = opencv.cvtColor(image, opencv.COLOR_BGR2GRAY)
    faces = detector(gray)

    #for loop
    for face in faces:
        blinking_ratio = _blinking_detect(image,gray,face);

        if blinking_ratio >= 6.0:
            passed_time += 1

            if (passed_time == 5): 
                print('wake up!') #console

                webbrowser.open_new_tab("C:/Users/User/Desktop/WakeUP_openCV/templates/index.html") #web
                #_vive(); # arduino
                time.sleep(2)
                passed_time = 0 #reset & loop

        else:
            passed_time = 0

    # show the frame
    opencv.imshow("Frame", image)
    key = opencv.waitKey(1) & 0xFF

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
        

##conda create -n CV python=3.9
##pip install opencv-python
##conda install -c conda-forge dlib
#그러면 끝!