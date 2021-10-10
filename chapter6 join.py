import cv2
import numpy as np
img=cv2.imread('resources\images.jpeg')
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgHoriz=np.hstack((img,imgray))
cv2.imshow('stackes',imgHoriz)
cv2.waitKey()