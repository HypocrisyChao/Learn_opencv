import numpy as np
import cv2

img = np.zeros((512,512))
imgColor = np.zeros((512,512,3),np.uint8)
#imgColor[200:300,100:300] = 255,0,0

cv2.line(imgColor,(0,0),(imgColor.shape[1],imgColor.shape[0]),(0,255,0),3)
cv2.rectangle(imgColor,(0,0),(250,250),(0,0,255),2)
cv2.circle(imgColor,(400,50),30,(255,255,0),2)
cv2.putText(imgColor,"opencv",(300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),2)


cv2.imshow("image",img)
cv2.imshow("imgColor",imgColor)

cv2.waitKey(0)