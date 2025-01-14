import cv2 as cv
from utils import get_limits
from PIL import Image
import time


cap = cv.VideoCapture(0)
green = [0,255,0]

if not cap:
    print("Error: Could not open webcam.")
    exit()

while True:
    start_time = time.time()
    _ , frame = cap.read()
    hsv_img = cv.cvtColor(frame , cv.COLOR_BGR2HSV)
    lower_limit , upper_limit = get_limits(green)
    mask = cv.inRange(hsv_img ,lower_limit,upper_limit)
    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

     # Display FPS on the frame
    if bbox is not None:
        x1,y1,x2,y2 = bbox
        cv.rectangle (frame , (x1,y1),(x2,y2),(255,0,255),4)

    end_time = time.time()
    fps = int(1 / (end_time - start_time))
    cv.putText(frame, f"FPS: {fps}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv.imshow('frame',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()