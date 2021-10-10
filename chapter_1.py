# camera read

# import cv2
# cap=cv2.VideoCapture(0)
# while True:
#     success,img=cap.read()
#     cv2.imshow('video',img)
#     if cv2.waitKey(1)& 0xFF==ord('q'):
#         break

# image read

# import cv2
# img=cv2.imread('resources\photov.jpg')
# cv2.imshow('output',img)
# cv2.waitKey()

#video read 

# import cv2
# cap=cv2.VideoCapture('resources\myvideo.mp4',)
# while True:
#     success,img=cap.read()
#     cv2.imshow('video window',img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break
import cv2,numpy as np
cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars',500,400)

def nothing(x):
    pass
cv2.createTrackbar("L - H", "Trackbars",0,179, nothing)
cv2.createTrackbar("L - S", "Trackbars",0,255, nothing)
cv2.createTrackbar("L - V", "Trackbars",0,255, nothing)
cv2.createTrackbar("U - H", "Trackbars",179,179, nothing)
cv2.createTrackbar("U - S", "Trackbars",255,255, nothing)
cv2.createTrackbar("U - V", "Trackbars",255,255, nothing)

cap=cv2.imread(r'computer-vision-samples-master\image-processing\missing-coins-detection\tray-of-coins.jpg')
while True:
    # success,img=cap.read()
    hsv = cv2.cvtColor(cap, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")
    
    lower = np.array([l_h, l_s, l_v])
    upper = np.array([u_h, u_s, u_v])
    mask_created = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(cap,cap,mask=mask_created)
    
    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.namedWindow('mask created',cv2.WINDOW_NORMAL)
    cv2.namedWindow('result',cv2.WINDOW_NORMAL)
    cv2.imshow("frame", cap)
    cv2.imshow("mask created", mask_created)
    cv2.imshow("result", result)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break