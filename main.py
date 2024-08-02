from ultralytics import YOLO
import tensorflow as tf
import cv2
from inference_sdk import InferenceHTTPClient

#Load YOLOv8
model = YOLO('yolov8x')

print('Hello, YOLOv8!')

# initialize the client
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="rg1zT8powDYuvF95NQZv"
)

# Preprocess Video
# Post Processing Video
def postprocess_detections(detections, frame):
    for detection in detections['predictions']:
        x1, y1 = int(detection['x'] - detection['width'] / 2), int(detection['y'] - detection['height'] / 2)
        x2, y2 = int(detection['x'] + detection['width'] / 2), int(detection['y'] + detection['height'] / 2)
        confidence = detection['confidence']
        label = detection['class']

        # Draw bounding boxes and labels on the frame
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(frame, f"{label}: {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    return frame

# Load up the Video
cap = cv2.VideoCapture('video.mp4')
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'DIVX'), 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Send the frame to the Inference API
    detections = CLIENT.infer(frame, model_id="tekkenai/2")

    # Postprocess the detections
    frame = postprocess_detections(detections, frame)

    # Display the frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    #Save Video (TEST)
    out.write(frame)

# Release the VideoCapture and destroy the windows
cap.release()
cv2.destroyAllWindows()
