import cv2
import mediapipe as mp
import pyautogui

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

finger_tips = [4, 8, 12, 16, 20]

def check_gesture(hand_landmarks):
    all_open = all(hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y for tip in finger_tips)
    all_closed = all(hand_landmarks.landmark[tip].y > hand_landmarks.landmark[tip - 2].y for tip in finger_tips)
    index_open = hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y and \
                all(hand_landmarks.landmark[tip].y > hand_landmarks.landmark[tip - 2].y for tip in [4, 12, 16, 20])
    index_middle_open = hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y and \
                hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y and \
                all(hand_landmarks.landmark[tip].y > hand_landmarks.landmark[tip - 2].y for tip in [4, 16, 20])
    if all_open:
        return 'play'
    elif all_closed:
        return 'pause'
    elif index_open:
        return 'skip'
    elif index_middle_open:
        return 'rewind'
    else:
        return None

def perform_action(gesture):
    if gesture == 'play':
        pyautogui.press('space') 
        print("Action: Play")
    elif gesture == 'pause':
        pyautogui.press('space')  
        print("Action: Pause")
    elif gesture == 'skip':
        pyautogui.press('right')  
        print("Action: Skip")
    elif gesture == 'rewind':
        pyautogui.press('left') 
        print("Action: Rewind")
        
cap = cv2.VideoCapture(0)

print("Control Gestures:")
print(" - Play: All fingers open")
print(" - Pause: All fingers closed")
print(" - Skip: Index finger open")
print(" - Rewind: Index and middle fingers open")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    result = hands.process(frame)
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = check_gesture(hand_landmarks)
            if gesture:
                perform_action(gesture)

    cv2.imshow("Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
