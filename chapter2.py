
# image read
import numpy as np
import cv2
kernel=np.ones((5,5))
img=cv2.imread('resources\photov.jpg')
cv2.imshow('output',img)
imgcanny=cv2.Canny(img,500,500)
imgerosion=cv2.erode(imgcanny,kernel,iterations=1)
imgdilation=cv2.dilate(imgcanny,kernel,iterations=1)
cv2.imshow('canny',imgcanny)
cv2.imshow('erosion',imgerosion)
cv2.imshow('dilation',imgdilation)
cv2.waitKey()
