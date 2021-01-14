import numpy as np
import cv2

kernel = np.ones((5,5),np.uint8)
img = cv2.imread('a/1.jpg')
#print(img.shape)
imgResize = cv2.resize(img,(300,200))
#print(imgResize.shape)
imgCropped = img[0:200,200:500]

cv2.imshow('img',img)
cv2.imshow('imgResize',imgResize)
cv2.imshow('imgCropped',imgCropped)

cv2.waitKey(0)