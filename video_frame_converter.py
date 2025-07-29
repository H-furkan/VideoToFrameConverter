import cv2
import os

video_path = 'camera_right.mp4'
output_dir = 'results/right'

cap = cv2.VideoCapture(video_path)
if not os.path.exists(output_dir):
    print("Error: Output directory does not exist.")
    exit(1)
frame_idx = 0
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"Frames per second: {fps}")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame_filename = os.path.join(output_dir, f'{frame_idx:05d}.png')
    cv2.imwrite(frame_filename, frame)
    frame_idx += 1

cap.release()
print(f"Extracted {frame_idx} frames to {output_dir}.")