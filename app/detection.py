import cv2
import torch
import numpy as np
from ultralytics import YOLO

# Load model
model = YOLO("yolov8n.pt")

# Class names for YOLOv8 (COCO dataset)
CLASS_NAMES = model.names

def detect_objects(frame):
    results = model(frame)
    detections = []

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()  # Convert tensor to list of floats
            conf = float(box.conf[0])              # Convert tensor to float
            cls = int(box.cls[0])                  # Convert tensor to int
            label = CLASS_NAMES.get(cls, "Unknown")

            if conf > 0.5:
                # Make sure all values are JSON-serializable (basic Python types)
                detections.append((x1, y1, x2, y2, cls, label))

    # You can update the scene detection logic later if needed
    scene = "Some Scene"
    return detections, scene
