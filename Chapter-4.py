import cv2
import numpy as np


faceCascade = cv2.CascadeClassifier("opencv-master/data/haarcascades_cuda/haarcascade_frontalface_alt2.xml")

path = 'a/3.jpg'
img = cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('img',img)
cv2.waitKey(0)