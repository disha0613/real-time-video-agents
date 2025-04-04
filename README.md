Smart Gesture-Based SOS Detection System

Objective:
To build a real-time, gesture-based emergency alert system that can detect human presence and predefined SOS gestures using a webcam feed. The aim is to provide an intuitive, contactless safety mechanism, especially useful in situations where physical interaction is not possible.

Problem Statement:
Many existing safety solutions require users to unlock their phone or press a specific button to raise an alert. In threatening or high-stress situations, this interaction may not be possible. A system that uses camera vision to recognize specific gestures and detect human presence offers a hands-free and reliable emergency alternative.

Proposed Solution:
The proposed system integrates MediaPipe's Holistic model for human body detection and a custom gesture recognition logic to detect three SOS hand gestures. On successful recognition, visual feedback is shown, and an SOS message is printed in the console.

Key Features:
Detects Presence of a Person: Utilizes body landmarks for real-time human detection.

Recognizes Three Emergency Gestures:

Palm Raise

Fist Clench & Open Twice

Two-Finger Tap on Palm

Live Webcam Feed Overlay: Provides a visual of the landmarks detected on the webcam feed.

Console Alert: Displays an SOS message in the console when an SOS gesture is recognized.

Tech Stack:
Python: Main programming language.

OpenCV: For accessing and displaying webcam video.

MediaPipe: To detect hand and body landmarks.

Custom Gesture Logic: Used to define and recognize SOS gestures.

GestureRecognition Class:
The GestureRecognition class is responsible for recognizing hand gestures using MediaPipe Hands. It detects the following gestures:

Palm Raise: All four fingers must be above the palm landmark, triggering an SOS.

Fist Clench and Open Twice: A clenched fist is detected, and if the gesture is performed twice in quick succession (within 1.5 seconds), an SOS is triggered.

Two-Finger Tap: The index and middle fingers must be close to the palm, triggering an SOS.

Combined Person and Gesture Detection:
This script handles the webcam feed, detects body landmarks using MediaPipe Holistic, and integrates the gesture recognition logic from movement.py to process gestures in real time.

Future Scope:
Add Audio Command Support: Trigger SOS via voice commands.

Real-Time Alerts: Trigger real-time SMS, Email, or WhatsApp alerts.

Deployment: Deploy as a desktop or web application.

Gesture Logs: Store logs of detected gestures for incident analysis.

Conclusion:
This system marks a significant step forward in creating intuitive, contactless safety tools. By combining real-time video processing and gesture-based logic, it empowers users with faster emergency communication when every second counts.

Author: Sai Disha Jayaram
