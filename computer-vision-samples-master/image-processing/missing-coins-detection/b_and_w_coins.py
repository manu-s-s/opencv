import cv2,numpy as np 
import matplotlib.pyplot as plt

def empty(x):
    pass

cv2.namedWindow('Parameters')
cv2.createTrackbar('Threshold 1','Parameters',0,255,empty)
cv2.createTrackbar('Threshold 2','Parameters',255,255,empty)

f,axarr=plt.subplots(1,4)

while True:
    img=cv2.imread('blackandwhite.jpg')
    imgblur=cv2.GaussianBlur(img,(17,17),0)
    imggray=cv2.cvtColor(imgblur,cv2.COLOR_BGR2GRAY)
    imgcanny=cv2.Canny(imggray,cv2.getTrackbarPos('Threshold 1','Parameters'),cv2.getTrackbarPos('Threshold 2','Parameters'))

    axarr[0].imshow(img),axarr[0].axis('off'),axarr[0].set_title('img')
    axarr[1].imshow(imgblur),axarr[1].axis('off'),axarr[1].set_title('imgblur')
    axarr[2].imshow(imggray,cmap='gray'),axarr[2].axis('off'),axarr[2].set_title('imggray')
    axarr[3].imshow(imgcanny,cmap='gray'),axarr[3].axis('off'),axarr[3].set_title('imgcanny')

plt.show()