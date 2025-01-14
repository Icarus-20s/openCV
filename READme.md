# Face Anonymizer & Color Detection with FPS Tracking

## Overview

This repository contains two projects:  

1. **Face Anonymizer**  
   A tool to anonymize faces in images, videos, and webcam streams using OpenCV and MediaPipe. Detected faces are blurred to maintain privacy.

2. **Color Detection with FPS Tracking**  
   A real-time tool to detect a specified color in a webcam stream and draw bounding boxes around the detected area. Additionally, it calculates and displays the FPS on the frame.

---

## Project 1: Face Anonymizer

### Features
- Detects faces in images, videos, or webcam streams.
- Blurs detected faces to anonymize them.
- Uses MediaPipe for face detection.

### Installation
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install opencv-python mediapipe
   ```

### Usage
Run the script and specify the mode:
- **Image**: Process a single image.
- **Video**: Process a video file.
- **Webcam**: Use the webcam for live face anonymization.

```bash
python face_anonymizer.py --mode [image|video|cam]
```

---

## Project 2: Color Detection with FPS Tracking

### Features
- Detects a specific color (default: green) in the webcam feed.
- Highlights the detected area with a bounding box.
- Displays the real-time FPS on the frame.

### Installation
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install opencv-python numpy pillow
   ```

### Usage
Run the script:
```bash
python color_detection.py
```

---

## Folder Structure
```
project/
│
├── face_anonymizer.py        # Script for Face Anonymizer
├── color_detection.py        # Script for Color Detection
├── utils.py                  # Helper functions for color limits
├── data/                     # Folder for input/output files
│   ├── testimg.png           # Sample input image
│   └── output/               # Output files (e.g., processed images/videos)
└── README.md                 # Project documentation
```

---

## Notes
- Press `q` to exit the webcam streams in both projects.
- Ensure the `data` directory exists for saving output files.
- Customize the color in `color_detection.py` by modifying the `green` variable.

---
