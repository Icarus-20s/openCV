import os 
import cv2


# Read the video

video_path = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4"
vid = cv2.VideoCapture(video_path)
total_frames = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"Total frames in the video: {total_frames}")


#vizualize the video

ret = True
while ret:
    ret ,frame = vid.read()
    
    if ret:
        cv2.imshow('video',frame)
        cv2.waitKey(0) & 0xFF==ord('q')

vid.release()
cv2.destroyAllWindows()





