from ultralytics import YOLO
import cv2
import os
from datetime import datetime

# Load the YOLO model (ensure this path is correct on the Pi)
model = YOLO("train_model/ft2/detect/train/weights/best.pt")

# Use the Pi camera (camera ID 0 works for most Pi Camera Modules)
cap = cv2.VideoCapture(0)

# Set resolution (you can change this to suit your Pi camera)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Check if the camera opened correctly
if not cap.isOpened():
    print("Error: Could not open Raspberry Pi camera.")
    exit()

# Get frame properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))
if fps == 0:  # fallback if FPS not detected
    fps = 20

# Create output directory
os.makedirs("recordings", exist_ok=True)

# Define output video path with timestamp
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_path = f"recordings/pi_stream_{timestamp}.mov"

# Define video writer
fourcc = cv2.VideoWriter_fourcc(*"avc1")  # or use "mp4v"
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

print("[INFO] Starting live stream. Press 'q' to stop and save recording.")

# Start reading frames
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Run inference
    results = model(frame)

    # Draw results
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            label = result.names[int(box.cls[0])]

            # Draw bounding box and label
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            text = f"{label}: {conf:.2f}"
            cv2.putText(frame, text, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow("YOLOv8 Pi Live Stream", frame)

    # Save the frame
    out.write(frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("[INFO] Stream stopped by user.")
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
print(f"[INFO] Recording saved to: {output_path}")
