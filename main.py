import cv2
import mediapipe as mp
from movement import GestureRecognition  # ✅ Using your original SOS logic

# Initialize MediaPipe for holistic model
mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
holistic = mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Your custom gesture detection logic
gesture_detector = GestureRecognition()

# Function to process video stream with Gesture Recognition and Person Detection
def process_video_stream(index=0):
    cap = cv2.VideoCapture(index)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        print("❌ Cannot open camera. Check index.")
        return

    print("🔥 Starting real-time video analytics with Gesture SOS detection and Person Detection...")

    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            print("❌ Frame capture failed.")
            break

        # Convert the image to RGB for MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Run holistic model to detect person and hand landmarks
        holistic_results = holistic.process(rgb_frame)

        # Person Detection (check if pose landmarks exist)
        if holistic_results.pose_landmarks:
            mp_drawing.draw_landmarks(frame, holistic_results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
            print("✅ Person detected")

        # Use gesture recognition logic from movement.py
        frame, sos_triggered = gesture_detector.recognize_gesture(frame)
        if sos_triggered:
            print("🚨 SOS Gesture Detected!")

        # Display frame
        cv2.imshow("Real-Time Gesture + Person Detection", frame)

        # Exit on 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_video_stream(index=0)
