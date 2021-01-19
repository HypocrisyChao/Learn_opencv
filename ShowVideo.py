import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier("opencv-master/data/haarcascades/haarcascade_frontalface_alt.xml")
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,130)

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow('Video',img)
    cv2.imshow('VideoGray',imgGray)
    if cv2.waitKey(1) & 0xff  ==ord('q'):
        break