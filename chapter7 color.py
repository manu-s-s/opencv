import cv2
import numpy as np

def nothing(x):
    pass

cap=cv2.VideoCapture(0)

cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars',500,400)

cv2.createTrackbar("L - H", "Trackbars",0,179, nothing)
cv2.createTrackbar("L - S", "Trackbars",0,255, nothing)
cv2.createTrackbar("L - V", "Trackbars",0,255, nothing)
cv2.createTrackbar("U - H", "Trackbars",179,179, nothing)
cv2.createTrackbar("U - S", "Trackbars",255,255, nothing)
cv2.createTrackbar("U - V", "Trackbars",255,255, nothing)

while True:

    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")
    
    lower = np.array([l_h, l_s, l_v])
    upper = np.array([u_h, u_s, u_v])
    mask_created = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame,frame,mask=mask_created)
    
    cv2.imshow("frame", frame)
    cv2.imshow("mask created", mask_created)
    cv2.imshow("result", result)

    if cv2.waitKey(1)==27: 
        break  
