import os
import cv2
import time

if not os.path.exists('DCIM'):
    os.makedirs('DCIM')

os.chdir('DCIM')

cam = cv2.VideoCapture("http://192.168.0.2:8080/video")

while True:

    ret, frame1 = cam.read()
    ret, frame2 = cam.read()

    diff = cv2.absdiff(frame1, frame2)

    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for c in contours:
        if cv2.contourArea(c) < 25000:
            continue

        timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
        cv2.imwrite("Motion_{}.jpg".format(timestr), frame1)
