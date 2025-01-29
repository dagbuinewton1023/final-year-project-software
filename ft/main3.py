from ultralytics import YOLO
import cv2
import math

# Load YOLO model
model = YOLO("yolo-Weights/yolov8n.pt")

# Custom object classes for mining-related items (Optional)
classNames = ["excavator", "dump truck", "bulldozer", "loader", "mining truck", "crane", "drilling machine", 
              "transport truck", "haul truck", "mining equipment", "earth mover", "mining machinery", "person"]

# Load the image (use the path to your image)
img_path = "3.png"  # Replace with the path to your image
img = cv2.imread(img_path)

if img is None:
    print("Failed to load image. Check the file path.")
else:
    results = model(img, stream=True)

    # Process results
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # Bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Convert to integers

            # Draw bounding box
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # Confidence
            confidence = math.ceil((box.conf[0] * 100)) / 100
            print("Confidence --->", confidence)

            # Class name
            cls = int(box.cls[0])
            print("Class name -->", classNames[cls])

            # Display class name and confidence on frame
            org = (x1, y1 - 10)
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

            cv2.putText(img, f"{classNames[cls]} {confidence}", org, font, fontScale, color, thickness)

    # Show the image with detected objects
    cv2.imshow('Image Classification', img)
    cv2.waitKey(0)  # Wait indefinitely until a key is pressed

    cv2.destroyAllWindows()
