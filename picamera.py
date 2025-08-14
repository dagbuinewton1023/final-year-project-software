from picamera2 import Picamera2
import cv2
import time

# Initialize the camera
picam2 = Picamera2()

# Configure camera for preview with 480x360 resolution
config = picam2.create_preview_configuration(main={"size": (480, 360)})
picam2.configure(config)

# Start camera
picam2.start()
time.sleep(1)  # Allow camera to warm up

print("?? Press 'q' to quit the live feed.")

while True:
    # Capture frame as numpy array
    frame = picam2.capture_array()

    # Show frame in OpenCV window
    cv2.imshow("Raspberry Pi Camera Live Feed", frame)

    # Check for 'q' key to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cv2.destroyAllWindows()
picam2.stop()