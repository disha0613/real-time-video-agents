import cv2
import mediapipe as mp
import time

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

class GestureRecognition:
    def __init__(self):
        self.hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
        self.prev_time = 0
        self.sos_triggered = False
        self.fist_count = 0
        self.last_fist_time = 0
    
    def recognize_gesture(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                landmarks = hand_landmarks.landmark
                thumb_tip = landmarks[4]
                index_tip = landmarks[8]
                middle_tip = landmarks[12]
                ring_tip = landmarks[16]
                pinky_tip = landmarks[20]
                palm_base = landmarks[0]
                
                # Detect Palm Raise
                if (index_tip.y < palm_base.y and middle_tip.y < palm_base.y and ring_tip.y < palm_base.y and pinky_tip.y < palm_base.y):
                    self.sos_triggered = True
                    cv2.putText(frame, "SOS: Palm Raised", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                
                # Detect Fist Clench & Open Twice
                if (thumb_tip.y > index_tip.y and thumb_tip.y > middle_tip.y and thumb_tip.y > ring_tip.y and thumb_tip.y > pinky_tip.y):
                    current_time = time.time()
                    if current_time - self.last_fist_time < 1.5:  # Detect within 1.5 seconds
                        self.fist_count += 1
                    else:
                        self.fist_count = 1
                    self.last_fist_time = current_time

                    if self.fist_count >= 2:
                        self.sos_triggered = True
                        cv2.putText(frame, "SOS: Fist Clench & Open", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                        self.fist_count = 0  # Reset
                
                # Detect Two-Finger Tap on Palm
                if abs(index_tip.y - palm_base.y) < 0.05 and abs(middle_tip.y - palm_base.y) < 0.05:
                    self.sos_triggered = True
                    cv2.putText(frame, "SOS: Two-Finger Tap", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                
        return frame, self.sos_triggered

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    gesture_recognition = GestureRecognition()
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame, sos_triggered = gesture_recognition.recognize_gesture(frame)
        
        cv2.imshow("Gesture Recognition", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
