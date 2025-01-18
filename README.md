# Gesture-Controlled-Media-Player-Using-Computer-Vision-and-Mediapipe
This project leverages Computer Vision and Mediapipe to enable a gesture-based control system for media players. With this tool, users can interact with media playback using simple hand gestures, eliminating the need for physical input devices.

Features
Play/Pause Media: Control playback by opening or closing all fingers.
Skip Forward: Use the index finger gesture to skip to the next segment.
Rewind: Open the index and middle fingers to rewind.
Real-time Hand Tracking: Utilizes Mediapipe's hand landmark detection for accurate and efficient gesture recognition.
Hands-Free Interaction: Seamlessly integrates gesture control for touchless media navigation.

Technologies Used
Python: Programming language for logic and integration.
OpenCV: For video feed processing and real-time visualization.
Mediapipe: For hand-tracking and landmark recognition.
PyAutoGUI: To simulate keyboard inputs for media controls.
How It Works
Hand Detection: Mediapipe detects the hand and tracks the position of fingertips and joints.
Gesture Analysis: Custom logic determines gestures (play, pause, skip, rewind) based on finger positions.
Action Execution: PyAutoGUI translates recognized gestures into corresponding media playback commands.

Usage Instructions
Clone this repository: git clone <repository-url>
Install required libraries: pip install opencv-python mediapipe pyautogui
Run the script: python gesture_control.py
Use the following gestures to control media:
Play: All fingers open.
Pause: All fingers closed.
Skip: Index finger open.
Rewind: Index and middle fingers open.
