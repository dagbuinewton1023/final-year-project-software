# from ultralytics import YOLO
# import cv2
# import math
# import tkinter as tk
# from tkinter import filedialog
# from tkinter import messagebox
# from PIL import Image, ImageTk

# # Load YOLO model
# model = YOLO("yolo-Weights/yolov8n.pt")

# # Custom object classes for mining-related items (Optional)
# classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
#               "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
#               "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
#               "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
#               "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
#               "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
#               "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
#               "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
#               "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
#               "teddy bear", "hair drier", "toothbrush"]

# # Function to process and display classification
# def process_classification(file_path):
#     if file_path.endswith(('.jpg', '.jpeg', '.png')):
#         img = cv2.imread(file_path)
#         if img is None:
#             messagebox.showerror("Error", "Failed to load image. Check the file path.")
#             return
#         results = model(img, stream=True)
#         img = process_results(results, img)
#         display_image(img)

#     elif file_path.endswith(('.mp4', '.avi', '.mov')):
#         cap = cv2.VideoCapture(file_path)
#         if not cap.isOpened():
#             messagebox.showerror("Error", "Failed to open video. Check the file path.")
#             return
#         while cap.isOpened():
#             ret, frame = cap.read()
#             if not ret:
#                 break
#             results = model(frame, stream=True)
#             frame = process_results(results, frame)
#             display_image(frame)
#             cv2.waitKey(1)  # Display frame for a short time

#         cap.release()
#         cv2.destroyAllWindows()
#     else:
#         messagebox.showerror("Error", "Unsupported file type. Please provide an image or video.")

# # Function to process results and draw bounding boxes
# def process_results(results, img):
#     for r in results:
#         boxes = r.boxes
#         for box in boxes:
#             # Bounding box
#             x1, y1, x2, y2 = box.xyxy[0]
#             x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Convert to integers

#             # Draw bounding box
#             cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

#             # Confidence
#             confidence = math.ceil((box.conf[0] * 100)) / 100
#             cls = int(box.cls[0])
#             class_name = f"{classNames[cls]} {confidence}"

#             # Display class name and confidence on frame
#             org = (x1, y1 - 10)
#             font = cv2.FONT_HERSHEY_SIMPLEX
#             fontScale = 1
#             color = (255, 0, 0)
#             thickness = 2
#             cv2.putText(img, class_name, org, font, fontScale, color, thickness)
#     return img

# # Function to display the image in Tkinter window
# def display_image(img):
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     img = Image.fromarray(img)
#     img = ImageTk.PhotoImage(img)

#     panel.configure(image=img)
#     panel.image = img

# # Function to open file dialog and load image or video
# def upload_file():
#     file_path = filedialog.askopenfilename(title="Select Image or Video", filetypes=[("All Files", "*.*"), ("Images", "*.jpg;*.jpeg;*.png"), ("Videos", "*.mp4;*.avi;*.mov")])
#     if file_path:
#         process_classification(file_path)

# # Create Tkinter window
# root = tk.Tk()
# root.title("Image/Video Classification App")

# # Create upload button
# upload_button = tk.Button(root, text="Upload Image/Video", command=upload_file)
# upload_button.pack(pady=20)

# # Create a panel to display the uploaded image
# panel = tk.Label(root)
# panel.pack(padx=10, pady=10)

# # Run the Tkinter loop
# root.mainloop()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# from ultralytics import YOLO
# import cv2
# import math
# import tkinter as tk
# from tkinter import filedialog
# from tkinter import messagebox
# from tkinter import Label
# from PIL import Image, ImageTk
# import time

# # Load YOLO model
# model = YOLO("yolo-Weights/yolov8n.pt")

# # Custom object classes for mining-related items (Optional)
# classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
#               "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
#               "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
#               "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
#               "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
#               "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
#               "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
#               "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
#               "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
#               "teddy bear", "hair drier", "toothbrush"]

# # Function to process and display classification
# def process_classification(file_path):
#     if file_path.endswith(('.jpg', '.jpeg', '.png')):
#         img = cv2.imread(file_path)
#         if img is None:
#             messagebox.showerror("Error", "Failed to load image. Check the file path.")
#             return
#         start_time = time.time()
#         results = model(img, stream=True)
#         inference_time = time.time() - start_time
#         img = process_results(results, img)
#         display_image(img, inference_time)
    
#     elif file_path.endswith(('.mp4', '.avi', '.mov')):
#         cap = cv2.VideoCapture(file_path)
#         if not cap.isOpened():
#             messagebox.showerror("Error", "Failed to open video. Check the file path.")
#             return
        
#         # Video display loop
#         def video_loop(inference_time):
#             ret, frame = cap.read()
#             if ret:
#                 results = model(frame, stream=True)
#                 frame = process_results(results, frame)
#                 display_image(frame, inference_time)
#                 panel.after(10, video_loop, inference_time)  # Call video_loop again after 10ms to update frame
#             else:
#                 cap.release()
#                 cv2.destroyAllWindows()

#         start_time = time.time()
#         video_loop(time.time() - start_time)  # Start video loop and pass inference_time

#     else:
#         messagebox.showerror("Error", "Unsupported file type. Please provide an image or video.")

# # Function to process results and draw bounding boxes
# def process_results(results, img):
#     for r in results:
#         boxes = r.boxes
#         for box in boxes:
#             # Bounding box
#             x1, y1, x2, y2 = box.xyxy[0]
#             x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Convert to integers

#             # Draw bounding box
#             cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

#             # Confidence
#             confidence = math.ceil((box.conf[0] * 100)) / 100
#             cls = int(box.cls[0])
#             class_name = f"{classNames[cls]} {confidence}"

#             # Display class name and confidence on frame
#             org = (x1, y1 - 10)
#             font = cv2.FONT_HERSHEY_SIMPLEX
#             fontScale = 1
#             color = (255, 0, 0)
#             thickness = 2
#             cv2.putText(img, class_name, org, font, fontScale, color, thickness)
#     return img

# # Function to display the image or video frame in Tkinter window
# def display_image(img, inference_time=None):
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     img = Image.fromarray(img)
#     img = ImageTk.PhotoImage(img)

#     panel.configure(image=img)
#     panel.image = img

#     if inference_time:
#         inference_label.config(text=f"Speed: {inference_time:.2f}s inference")

# # Function to open file dialog and load image or video
# def upload_file():
#     file_path = filedialog.askopenfilename(title="Select Image or Video", filetypes=[("All Files", "*.*"), ("Images", "*.jpg;*.jpeg;*.png"), ("Videos", "*.mp4;*.avi;*.mov")])
#     if file_path:
#         process_classification(file_path)

# # Function to delete the image and reset the UI
# def delete_file():
#     panel.configure(image='')
#     panel.image = None
#     inference_label.config(text="")

# # Create Tkinter window
# root = tk.Tk()
# root.title("Image/Video Classification App")

# # Create upload button
# upload_button = tk.Button(root, text="Upload Image/Video", command=upload_file)
# upload_button.pack(pady=20)

# # Create delete button
# delete_button = tk.Button(root, text="Delete Image/Video", command=delete_file)
# delete_button.pack(pady=10)

# # Create a panel to display the uploaded image
# panel = tk.Label(root)
# panel.pack(padx=10, pady=10)

# # Create a label to show inference time
# inference_label = tk.Label(root, text="Speed: N/A", font=("Helvetica", 10))
# inference_label.pack(pady=10)

# # Run the Tkinter loop
# root.mainloop()


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# from ultralytics import YOLO
# import cv2
# import math
# import tkinter as tk
# from tkinter import filedialog
# from tkinter import messagebox
# from tkinter import Label
# from PIL import Image, ImageTk
# import time

# # Load YOLO model
# model = YOLO("yolo-Weights/yolov8n.pt")

# # Custom object classes for mining-related items (Optional)
# classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
#               "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
#               "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
#               "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
#               "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
#               "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
#               "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
#               "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
#               "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
#               "teddy bear", "hair drier", "toothbrush"]

# # Function to process and display classification
# def process_classification(file_path):
#     if file_path.endswith(('.jpg', '.jpeg', '.png')):  # Image processing
#         img = cv2.imread(file_path)
#         if img is None:
#             messagebox.showerror("Error", "Failed to load image. Check the file path.")
#             return
#         start_time = time.time()
#         results = model(img, stream=True)
#         inference_time = time.time() - start_time
#         img = process_results(results, img)
#         display_image(img, inference_time)
    
#     elif file_path.endswith(('.mp4', '.avi', '.mov')):  # Video processing
#         cap = cv2.VideoCapture(file_path)
#         if not cap.isOpened():
#             messagebox.showerror("Error", "Failed to open video. Check the file path.")
#             return
        
#         # Video display loop
#         def video_loop(inference_time):
#             ret, frame = cap.read()
#             if ret:
#                 results = model(frame, stream=True)
#                 frame = process_results(results, frame)
#                 display_image(frame, inference_time)
#                 panel.after(10, video_loop, inference_time)  # Call video_loop again after 10ms to update frame
#             else:
#                 cap.release()
#                 cv2.destroyAllWindows()

#         start_time = time.time()
#         video_loop(time.time() - start_time)  # Start video loop and pass inference_time

#     else:
#         messagebox.showerror("Error", "Unsupported file type. Please provide an image or video.")

# # Function to process results and draw bounding boxes
# def process_results(results, img):
#     global class_name, confidence_score
#     for r in results:
#         boxes = r.boxes
#         for box in boxes:
#             # Bounding box
#             x1, y1, x2, y2 = box.xyxy[0]
#             x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Convert to integers

#             # Draw bounding box
#             cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

#             # Confidence
#             confidence = math.ceil((box.conf[0] * 100)) / 100
#             cls = int(box.cls[0])
#             class_name = f"{classNames[cls]}"  # Get class name
#             confidence_score = f"{confidence}"  # Get confidence score

#             # Display class name and confidence on frame
#             org = (x1, y1 - 10)
#             font = cv2.FONT_HERSHEY_SIMPLEX
#             fontScale = 1
#             color = (255, 0, 0)
#             thickness = 2
#             cv2.putText(img, f"{class_name} {confidence_score}", org, font, fontScale, color, thickness)
#     return img

# # Function to display the image or video frame in Tkinter window
# def display_image(img, inference_time=None):
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     img = Image.fromarray(img)
#     img = ImageTk.PhotoImage(img)

#     panel.configure(image=img)
#     panel.image = img

#     if inference_time:
#         inference_label.config(text=f"Speed: {inference_time:.2f}s inference")
    
#     # Update classification and confidence labels
#     if class_name:
#         class_label.config(text=f"Class: {class_name}")
#     if confidence_score:
#         confidence_label.config(text=f"Confidence: {confidence_score}")

# # Function to open file dialog and load image or video
# def upload_file():
#     file_path = filedialog.askopenfilename(title="Select Image or Video", filetypes=[("All Files", "*.*"), ("Images", "*.jpg;*.jpeg;*.png"), ("Videos", "*.mp4;*.avi;*.mov")])
#     if file_path:
#         process_classification(file_path)

# # Function to delete the image and reset the UI
# def delete_file():
#     panel.configure(image='')
#     panel.image = None
#     inference_label.config(text="Speed: N/A")
#     class_label.config(text="Class: N/A")
#     confidence_label.config(text="Confidence: N/A")

# # Create Tkinter window
# root = tk.Tk()
# root.title("Image/Video Classification App")

# # Create upload button
# upload_button = tk.Button(root, text="Upload Image/Video", command=upload_file)
# upload_button.pack(pady=20)

# # Create delete button
# delete_button = tk.Button(root, text="Delete Image/Video", command=delete_file)
# delete_button.pack(pady=10)

# # Create a panel to display the uploaded image
# panel = tk.Label(root)
# panel.pack(padx=10, pady=10)

# # Create labels for showing inference time, class, and confidence
# inference_label = tk.Label(root, text="Speed: N/A", font=("Helvetica", 10))
# inference_label.pack(pady=5)

# class_label = tk.Label(root, text="Class: N/A", font=("Helvetica", 10))
# class_label.pack(pady=5)

# confidence_label = tk.Label(root, text="Confidence: N/A", font=("Helvetica", 10))
# confidence_label.pack(pady=5)

# # Run the Tkinter loop
# root.mainloop()




# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# from ultralytics import YOLO
# import cv2
# import math
# import tkinter as tk
# from tkinter import filedialog
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import time

# # Load YOLO model
# model = YOLO("yolo-Weights/yolov8n.pt")

# classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
#               "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
#               "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
#               "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
#               "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
#               "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
#               "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
#               "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
#               "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
#               "teddy bear", "hair drier", "toothbrush"]

# objects_identified = []

# # Function to process and display classification
# def process_classification(file_path):
#     if file_path.endswith(('.jpg', '.jpeg', '.png')):
#         img = cv2.imread(file_path)
#         if img is None:
#             messagebox.showerror("Error", "Failed to load image. Check the file path.")
#             return
#         start_time = time.time()
#         results = model(img, stream=True)
#         inference_time = time.time() - start_time
#         img = process_results(results, img)
#         display_image(img, inference_time)
#     elif file_path.endswith(('.mp4', '.avi', '.mov')):
#         cap = cv2.VideoCapture(file_path)
#         if not cap.isOpened():
#             messagebox.showerror("Error", "Failed to open video. Check the file path.")
#             return

#         def video_loop(inference_time):
#             ret, frame = cap.read()
#             if ret:
#                 results = model(frame, stream=True)
#                 frame = process_results(results, frame)
#                 display_image(frame, inference_time)
#                 panel.after(10, video_loop, inference_time)
#             else:
#                 cap.release()
#                 cv2.destroyAllWindows()

#         start_time = time.time()
#         video_loop(time.time() - start_time)
#     else:
#         messagebox.showerror("Error", "Unsupported file type. Please provide an image or video.")

# # Function to process results and draw bounding boxes
# def process_results(results, img):
#     global objects_identified
#     objects_identified = []
#     for r in results:
#         boxes = r.boxes
#         for box in boxes:
#             x1, y1, x2, y2 = box.xyxy[0]
#             x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
#             cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
#             confidence = math.ceil((box.conf[0] * 100)) / 100
#             cls = int(box.cls[0])
#             class_name = f"{classNames[cls]}"
#             confidence_score = f"{confidence}"
#             objects_identified.append(f"{class_name}: {confidence_score}")
#             org = (x1, y1 - 10)
#             font = cv2.FONT_HERSHEY_SIMPLEX
#             fontScale = 1
#             color = (255, 0, 0)
#             thickness = 2
#             cv2.putText(img, f"{class_name} {confidence_score}", org, font, fontScale, color, thickness)
#     return img

# # Function to display the image or video frame in Tkinter window
# def display_image(img, inference_time=None):
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     img = Image.fromarray(img)
#     img = ImageTk.PhotoImage(img)

#     panel.configure(image=img)
#     panel.image = img

#     if inference_time:
#         inference_label.config(text=f"Speed: {inference_time:.2f}s inference")

#     if objects_identified:
#         identified_objects_label.config(text="\n".join(objects_identified))

# # Function to open file dialog and load image or video
# def upload_file():
#     file_path = filedialog.askopenfilename(title="Select Image or Video", filetypes=[("All Files", "*.*"), ("Images", "*.jpg;*.jpeg;*.png"), ("Videos", "*.mp4;*.avi;*.mov")])
#     if file_path:
#         process_classification(file_path)

# # Function to delete the image and reset the UI
# def delete_file():
#     panel.configure(image='')
#     panel.image = None
#     inference_label.config(text="Speed: N/A")
#     identified_objects_label.config(text="")

# # Create Tkinter window
# root = tk.Tk()
# root.title("Image/Video Classification App")
# root.geometry("800x600")  # Set a default size

# # Create a centered frame
# frame = tk.Frame(root)
# frame.pack(expand=True)

# # Create upload button
# upload_button = tk.Button(frame, text="Upload Image/Video", command=upload_file)
# upload_button.grid(row=0, column=0, pady=10)

# # Create delete button
# delete_button = tk.Button(frame, text="Delete Image/Video", command=delete_file)
# delete_button.grid(row=1, column=0, pady=10)

# # Create a panel to display the uploaded image
# panel = tk.Label(frame)
# panel.grid(row=2, column=0, padx=10, pady=10)

# # Create labels for showing inference time and identified objects
# inference_label = tk.Label(frame, text="Speed: N/A", font=("Helvetica", 10))
# inference_label.grid(row=3, column=0, pady=5)
# identified_objects_label = tk.Label(frame, text="", font=("Helvetica", 10))
# identified_objects_label.grid(row=4, column=0, pady=5)

# root.mainloop()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------


# from ultralytics import YOLO
# import cv2
# import math
# import tkinter as tk
# from tkinter import filedialog
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import time

# # Load YOLO model
# model = YOLO("yolo-Weights/yolov8n.pt")

# classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
#               "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
#               "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
#               "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
#               "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
#               "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
#               "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
#               "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
#               "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
#               "teddy bear", "hair drier", "toothbrush"]

# objects_identified = []

# # Function to process and display classification
# def process_classification(file_path):
#     if file_path.endswith(('.jpg', '.jpeg', '.png')):
#         img = cv2.imread(file_path)
#         if img is None:
#             messagebox.showerror("Error", "Failed to load image. Check the file path.")
#             return
#         start_time = time.time()
#         results = model(img, stream=True)
#         inference_time = time.time() - start_time
#         img = process_results(results, img)
#         display_image(img, inference_time)
#     elif file_path.endswith(('.mp4', '.avi', '.mov')):
#         cap = cv2.VideoCapture(file_path)
#         if not cap.isOpened():
#             messagebox.showerror("Error", "Failed to open video. Check the file path.")
#             return

#         def video_loop(inference_time):
#             ret, frame = cap.read()
#             if ret:
#                 results = model(frame, stream=True)
#                 frame = process_results(results, frame)
#                 display_image(frame, inference_time)
#                 panel.after(10, video_loop, inference_time)
#             else:
#                 cap.release()
#                 cv2.destroyAllWindows()

#         start_time = time.time()
#         video_loop(time.time() - start_time)
#     else:
#         messagebox.showerror("Error", "Unsupported file type. Please provide an image or video.")

# # Function to process results and draw bounding boxes
# def process_results(results, img):
#     global objects_identified
#     objects_identified = []
#     for r in results:
#         boxes = r.boxes
#         for box in boxes:
#             x1, y1, x2, y2 = box.xyxy[0]
#             x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
#             cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
#             confidence = math.ceil((box.conf[0] * 100)) / 100
#             cls = int(box.cls[0])
#             class_name = f"{classNames[cls]}"
#             confidence_score = f"{confidence}"
#             objects_identified.append(f"{class_name}: {confidence_score}")
#             org = (x1, y1 - 10)
#             font = cv2.FONT_HERSHEY_SIMPLEX
#             fontScale = 1
#             color = (255, 0, 0)
#             thickness = 2
#             cv2.putText(img, f"{class_name} {confidence_score}", org, font, fontScale, color, thickness)
#     return img

# # Function to display the image or video frame in Tkinter window
# def display_image(img, inference_time=None):
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     img = Image.fromarray(img)
#     img = ImageTk.PhotoImage(img)

#     panel.configure(image=img)
#     panel.image = img

#     if inference_time:
#         inference_label.config(text=f"Speed: {inference_time:.2f}s inference")

#     if objects_identified:
#         identified_objects_label.config(text="\n".join(objects_identified))

# # Function to open file dialog and load image or video
# def upload_file():
#     file_path = filedialog.askopenfilename(title="Select Image or Video", filetypes=[("All Files", "*.*"), ("Images", "*.jpg;*.jpeg;*.png"), ("Videos", "*.mp4;*.avi;*.mov")])
#     if file_path:
#         process_classification(file_path)

# # Function to delete the image and reset the UI
# def delete_file():
#     panel.configure(image='')
#     panel.image = None
#     inference_label.config(text="Speed: N/A")
#     identified_objects_label.config(text="")

# # Create Tkinter window
# root = tk.Tk()
# root.title("Image/Video Classification App")
# root.geometry("800x600")

# # Center container
# container = tk.Frame(root)
# container.place(relx=0.5, rely=0.5, anchor="center")

# # Upload and delete buttons
# upload_button = tk.Button(container, text="Upload Image/Video", command=upload_file)
# upload_button.pack(pady=10)
# delete_button = tk.Button(container, text="Delete Image/Video", command=delete_file)
# delete_button.pack(pady=10)

# # Panel to display the uploaded image
# panel = tk.Label(container)
# panel.pack(pady=10)

# # Labels for showing inference time and identified objects
# inference_label = tk.Label(container, text="Speed: N/A", font=("Helvetica", 10))
# inference_label.pack(pady=5)
# identified_objects_label = tk.Label(container, text="", font=("Helvetica", 10))
# identified_objects_label.pack(pady=5)

# root.mainloop()

#hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
# from ultralytics import YOLO
# import cv2
# import math
# import tkinter as tk
# from tkinter import filedialog
# from tkinter import messagebox
# from PIL import Image, ImageTk
# import time

# # Load YOLO model
# model = YOLO("yolo-Weights/yolov8n.pt")

# classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
#               "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
#               "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
#               "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
#               "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
#               "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
#               "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
#               "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
#               "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
#               "teddy bear", "hair drier", "toothbrush"]

# objects_identified = []

# # Function to process and display classification
# def process_classification(file_path):
#     if file_path.endswith(('.jpg', '.jpeg', '.png')): 
#         img = cv2.imread(file_path)
#         if img is None:
#             messagebox.showerror("Error", "Failed to load image. Check the file path.")
#             return
#         start_time = time.time()
#         results = model(img, stream=True)
#         inference_time = time.time() - start_time
#         img = process_results(results, img)
#         display_image(img, inference_time)
#     elif file_path.endswith(('.mp4', '.avi', '.mov')): 
#         cap = cv2.VideoCapture(file_path)
#         if not cap.isOpened():
#             messagebox.showerror("Error", "Failed to open video. Check the file path.")
#             return

#         def video_loop(inference_time):
#             ret, frame = cap.read()
#             if ret:
#                 results = model(frame, stream=True)
#                 frame = process_results(results, frame)
#                 display_image(frame, inference_time)
#                 panel.after(10, video_loop, inference_time)
#             else:
#                 cap.release()
#                 cv2.destroyAllWindows()

#         start_time = time.time()
#         video_loop(time.time() - start_time)
#     else:
#         messagebox.showerror("Error", "Unsupported file type. Please provide an image or video.")

# # Function to process results and draw bounding boxes
# def process_results(results, img):
#     global objects_identified
#     objects_identified = []
#     for r in results:
#         boxes = r.boxes
#         for box in boxes:
#             x1, y1, x2, y2 = box.xyxy[0]
#             x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
#             cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
#             confidence = math.ceil((box.conf[0] * 100)) / 100
#             cls = int(box.cls[0])
#             class_name = f"{classNames[cls]}"
#             confidence_score = f"{confidence}"
#             objects_identified.append(f"{class_name}: {confidence_score}")
#             org = (x1, y1 - 10)
#             font = cv2.FONT_HERSHEY_SIMPLEX
#             fontScale = 1
#             color = (255, 0, 0)
#             thickness = 2
#             cv2.putText(img, f"{class_name} {confidence_score}", org, font, fontScale, color, thickness)
#     return img

# # Function to display the image or video frame in Tkinter window
# def display_image(img, inference_time=None):
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     img = Image.fromarray(img)
#     img = ImageTk.PhotoImage(img)

#     panel.configure(image=img)
#     panel.image = img

#     if inference_time:
#         inference_label.config(text=f"Speed: {inference_time:.2f}s inference")

#     if objects_identified:
#         identified_objects_label.config(text="\n".join(objects_identified))

# # Function to open file dialog and load image or video
# def upload_file():
#     file_path = filedialog.askopenfilename(title="Select Image or Video", filetypes=[("All Files", "*.*"), ("Images", "*.jpg;*.jpeg;*.png"), ("Videos", "*.mp4;*.avi;*.mov")])
#     if file_path:
#         process_classification(file_path)

# # Function to delete the image and reset the UI
# def delete_file():
#     panel.configure(image='')
#     panel.image = None
#     inference_label.config(text="Speed: N/A")
#     identified_objects_label.config(text="")

# # Create Tkinter window
# root = tk.Tk()
# root.title("Image/Video Classification App")

# # Create a canvas for scrolling
# canvas = tk.Canvas(root)
# canvas.pack(side="left", fill="both", expand=True)

# # Create a vertical scrollbar for the canvas
# scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
# scrollbar.pack(side="right", fill="y")

# canvas.config(yscrollcommand=scrollbar.set)

# # Create a frame to contain all UI elements
# frame = tk.Frame(canvas)
# canvas.create_window((0, 0), window=frame, anchor="nw")

# # Bind the frame's size to the canvas scrolling region
# frame.bind(
#     "<Configure>",
#     lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
# )

# # Use pack with anchor to center everything like `justify-content: center` and `align-items: center`
# frame.pack(expand=True, fill="both")
# frame.grid_rowconfigure(0, weight=1)  # Allow row 0 to grow
# frame.grid_columnconfigure(0, weight=1)  # Allow column 0 to grow

# # Create UI elements
# upload_button = tk.Button(frame, text="Upload Image/Video", command=upload_file)
# upload_button.pack(pady=10)

# delete_button = tk.Button(frame, text="Delete Image/Video", command=delete_file)
# delete_button.pack(pady=10)

# panel = tk.Label(frame)
# panel.pack(pady=10)

# inference_label = tk.Label(frame, text="Speed: N/A", font=("Helvetica", 10))
# inference_label.pack(pady=5)

# identified_objects_label = tk.Label(frame, text="", font=("Helvetica", 10))
# identified_objects_label.pack(pady=5)

# root.mainloop()









from ultralytics import YOLO
import cv2
import math
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import time

# Load YOLO model
model = YOLO("yolo-Weights/yolov8n.pt")

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

objects_identified = []

# Function to process and display classification
def process_classification(file_path):
    if file_path.endswith(('.jpg', '.jpeg', '.png')): 
        img = cv2.imread(file_path)
        if img is None:
            messagebox.showerror("Error", "Failed to load image. Check the file path.")
            return
        start_time = time.time()
        results = model(img, stream=True)
        inference_time = time.time() - start_time
        img = process_results(results, img)
        display_image(img, inference_time)
    elif file_path.endswith(('.mp4', '.avi', '.mov')): 
        cap = cv2.VideoCapture(file_path)
        if not cap.isOpened():
            messagebox.showerror("Error", "Failed to open video. Check the file path.")
            return

        def video_loop(inference_time):
            ret, frame = cap.read()
            if ret:
                results = model(frame, stream=True)
                frame = process_results(results, frame)
                display_image(frame, inference_time)
                panel.after(10, video_loop, inference_time)
            else:
                cap.release()
                cv2.destroyAllWindows()

        start_time = time.time()
        video_loop(time.time() - start_time)
    else:
        messagebox.showerror("Error", "Unsupported file type. Please provide an image or video.")

# Function to process results and draw bounding boxes
def process_results(results, img):
    global objects_identified
    objects_identified = []
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
            confidence = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])
            class_name = f"{classNames[cls]}"
            confidence_score = f"{confidence}"
            objects_identified.append(f"{class_name}: {confidence_score}")
            org = (x1, y1 - 10)
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2
            cv2.putText(img, f"{class_name} {confidence_score}", org, font, fontScale, color, thickness)
    return img

# Function to display the image or video frame in Tkinter window
def display_image(img, inference_time=None):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)

    panel.configure(image=img)
    panel.image = img

    if inference_time:
        inference_label.config(text=f"Speed: {inference_time:.2f}s inference")

    if objects_identified:
        identified_objects_label.config(text="\n".join(objects_identified))

# Function to open file dialog and load image or video
def upload_file():
    file_path = filedialog.askopenfilename(title="Select Image or Video", filetypes=[("All Files", "*.*"), ("Images", "*.jpg;*.jpeg;*.png"), ("Videos", "*.mp4;*.avi;*.mov")])
    if file_path:
        process_classification(file_path)

# Function to delete the image and reset the UI
def delete_file():
    panel.configure(image='')
    panel.image = None
    inference_label.config(text="Speed: N/A")
    identified_objects_label.config(text="")

# Create Tkinter window
root = tk.Tk()
root.title("Image/Video Classification App")

# Create a canvas for scrolling
canvas = tk.Canvas(root)
canvas.pack(side="left", fill="both", expand=True)

# Create a vertical scrollbar for the canvas
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.config(yscrollcommand=scrollbar.set)

# Create a frame to contain all UI elements
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Bind the frame's size to the canvas scrolling region
frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

# Use pack with anchor to center everything like `justify-content: center` and `align-items: center`
frame.pack(expand=True, fill="both")
frame.grid_rowconfigure(0, weight=1)  # Allow row 0 to grow
frame.grid_columnconfigure(0, weight=1)  # Allow column 0 to grow

# Create UI elements
upload_button = tk.Button(frame, text="Upload Image/Video", command=upload_file)
upload_button.pack(pady=10)

delete_button = tk.Button(frame, text="Delete Image/Video", command=delete_file)
delete_button.pack(pady=10)

panel = tk.Label(frame)
panel.pack(pady=10)

# Inference label and identified objects label will be placed below the image
inference_label = tk.Label(frame, text="Speed: N/A", font=("Helvetica", 10))
inference_label.pack(pady=5)

identified_objects_label = tk.Label(frame, text="", font=("Helvetica", 10))
identified_objects_label.pack(pady=5)

root.mainloop()
