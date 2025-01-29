from ultralytics import YOLO
import cv2
import math

# Load YOLO model
model = YOLO("yolo-Weights/yolov8n.pt")

# Custom object classes for mining-related items (Optional)
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"]

# Function to process and display classification on image or video
def classify_image_or_video(input_path):
    # Check if the input is an image or video by file extension
    if input_path.endswith(('.jpg', '.jpeg', '.png')):
        # Load the image (use the path to your image)
        img = cv2.imread(input_path)
        if img is None:
            print("Failed to load image. Check the file path.")
            return
        results = model(img, stream=True)
        # Process results for image
        process_results(results, img)
        cv2.imshow('Image Classification', img)
        cv2.waitKey(0)  # Wait indefinitely until a key is pressed
        cv2.destroyAllWindows()

    elif input_path.endswith(('.mp4', '.avi', '.mov')):
        # Open video file
        cap = cv2.VideoCapture(input_path)
        if not cap.isOpened():
            print("Failed to open video. Check the file path.")
            return

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            results = model(frame, stream=True)
            # Process results for video
            process_results(results, frame)
            cv2.imshow('Video Classification', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
                break

        cap.release()
        cv2.destroyAllWindows()

    else:
        print("Unsupported file type. Please provide an image or video.")

# Function to process results and draw bounding boxes with class names
def process_results(results, img):
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
            # Class name
            cls = int(box.cls[0])
            class_name = f"{classNames[cls]} {confidence}"

            # Display class name and confidence on frame
            org = (x1, y1 - 10)
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2
            cv2.putText(img, class_name, org, font, fontScale, color, thickness)

# Example usage for image or video file
input_path = "1.jpg"  # Replace with the image or video path
classify_image_or_video(input_path)
