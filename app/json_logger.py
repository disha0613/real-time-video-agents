import json
import os
from datetime import datetime

LOG_FILE = "data/detections.json"  # Log file path

def log_detection(detections, scene):
    """
    Logs detection data into a JSON file.
    
    :param detections: List of detections (bounding boxes, class labels)
    :param scene: Detected scene context
    """
    log_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "scene": scene,
        "detections": []
    }

    for x1, y1, x2, y2, cls, label in detections:
        log_entry["detections"].append({
            "bbox": [x1, y1, x2, y2],
            "class_id": cls,
            "label": label
        })

    # Read existing logs
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as file:
            try:
                logs = json.load(file)
            except json.JSONDecodeError:
                logs = []
    else:
        logs = []

    # Append new entry
    logs.append(log_entry)

    # Write back to JSON file
    with open(LOG_FILE, "w") as file:
        json.dump(logs, file, indent=4)

    print(f"Logged {len(detections)} detections in {scene} scene.")  
