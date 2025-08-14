from ultralytics import YOLO
import cv2
from picamera2 import Picamera2

# Load YOLO model
model = YOLO("train_model/ft2/detect/train/weights/best.pt")  # Update path if needed

# Initialize PiCamera2
picam2 = Picamera2()
camera_config = picam2.create_preview_configuration(main={"format": "BGR888", "size": (640, 480)})
picam2.configure(camera_config)
picam2.start()

print("[INFO] Starting YOLO Pi camera feed. Press 'q' to exit.")

while True:
    frame = picam2.capture_array()  # Capture frame from Pi camera
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


    # Run YOLO inference
    results = model(frame)

    # Draw detection boxes
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            label = result.names[int(box.cls[0])]

            # Draw bounding box and label
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{label}: {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow("YOLO Pi Camera Feed", frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cv2.destroyAllWindows()
picam2.close()
