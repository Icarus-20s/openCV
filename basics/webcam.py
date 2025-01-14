import os 
import cv2


#read webcam

webcam = cv2.VideoCapture(0)



#vizualize the webcam
while True:
    ret , frame = webcam.read()
    cv2.imshow('webcam',frame)
    if cv2.waitKey(40) & 0xFF==ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
