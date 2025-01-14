import cv2 as cv
import numpy as np



def get_limits(color):
    c = np.uint8([[color]])
    hsvC = cv.cvtColor(c,cv.COLOR_BGR2HSV)
    hue = hsvC[0][0][0]

    if hue>=165:
        lower_limit = np.array([hue-10 ,100,100])
        upper_limit = np.array([hue+10 ,255,255])

    elif hue<=15:
        lower_limit= np.array([0,100,100])
        upper_limit = np.array([hue+10,255,255])
    else:
        lower_limit = np.array ([hue-10,100,100])
        upper_limit = np.array ([hue+10,255,255])


    return lower_limit , upper_limit

