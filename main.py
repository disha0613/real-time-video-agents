print("🔥 Starting detection system...")

import cv2
from app.detection import detect_objects
from app.json_logger import log_detection 

cap = cv2.VideoCapture(0)
print("🎥 Trying to access webcam...")

if not cap.isOpened():
    print("❌ Error: Cannot open webcam")
    exit()
else:
    print("✅ Webcam opened successfully!")

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Failed to grab frame.")
        break

    # Detect objects and scene
    detections, scene = detect_objects(frame)

    # Log detection
    log_detection(detections, scene)

    # Draw detections
    for x1, y1, x2, y2, cls, label in detections:
        x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)

    # Draw scene text
    cv2.putText(frame, f"Scene: {scene}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

    # Display window
    cv2.imshow("YOLOv8 Detection with Scene Context", frame)

    # Exit condition
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("🛑 Exiting detection loop.")
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
