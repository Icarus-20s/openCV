import cv2 as cv
import os
import mediapipe as mp
import argparse


# Define global paths
img_path = os.path.join('.', 'faceAnonymizerproject', 'data', 'testimg.png')
video_path = os.path.join('.', 'faceAnonymizerproject', 'data', 'testVideo.mp4')
output_path = os.path.join('.', 'faceAnonymizerproject', 'data', 'output')

if not os.path.exists(output_path):
    os.mkdir(output_path)


def process_img(img, face_detection):
    """
    Process an image to detect faces and apply blurring to anonymize them.
    """
    H, W, _ = img.shape
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)
    if out.detections is not None:
        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box
            x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height
            x1 = int(x1 * W)
            y1 = int(y1 * H)
            w = int(w * W)
            h = int(h * H)
            # Draw rectangle around the face (optional, remove if not needed)
            cv.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 5)
            # Apply blur to anonymize the face
            img[y1:y1 + h, x1:x1 + w, :] = cv.blur(img[y1:y1 + h, x1:x1 + w, :], (50, 50))
    return img


def process_image(face_detection):
    """
    Process a single image to anonymize faces.
    """
    img = cv.imread(img_path)
    if img is None:
        print('Could not open or find the image.')
        return
    img = process_img(img, face_detection)
    output_img_path = os.path.join(output_path, 'face_hide.jpg')
    cv.imwrite(output_img_path, img)
    print(f"Processed image saved to: {output_img_path}")


def process_video(face_detection):
    """
    Process a video to anonymize faces in each frame.
    """
    vid = cv.VideoCapture(video_path)
    if not vid.isOpened():
        print(f"Could not open or find the video: {video_path}")
        return
    _, frame = vid.read()
    output_vid_path = os.path.join(output_path, 'face_hide.mp4')
    output_vid = cv.VideoWriter(output_vid_path, cv.VideoWriter_fourcc(*'mp4v'), 25, (frame.shape[1], frame.shape[0]))
    while _:
        frame = process_img(frame, face_detection)
        output_vid.write(frame)
        _, frame = vid.read()
    vid.release()
    output_vid.release()
    print(f"Processed video saved to: {output_vid_path}")


def process_webcam(face_detection):
    """
    Process live webcam feed to anonymize faces in real-time.
    """
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print('Could not open webcam.')
        return
    print("Press 'q' to quit.")
    _, frame = cap.read()
    while _:
        frame = process_img(frame, face_detection)
        cv.imshow('Webcam Feed', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        _, frame = cap.read()
    cap.release()


def main():
    parser = argparse.ArgumentParser(description="Face Anonymizer using MediaPipe")
    parser.add_argument('--mode', type=str, required=True, choices=['img', 'vid', 'cam'],
                        help="Mode of operation: 'img' for image, 'vid' for video, 'cam' for webcam.")
    args = parser.parse_args()

    mp_face_detection = mp.solutions.face_detection
    with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
        if args.mode == 'img':
            process_image(face_detection)
        elif args.mode == 'vid':
            process_video(face_detection)
        elif args.mode == 'cam':
            process_webcam(face_detection)

    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
