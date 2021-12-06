import mediapipe as mp
from math import atan, sqrt
import cv2


mp_holistic = mp.solutions.holistic


def process_img(image):

    with mp_holistic.Holistic(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as holistic:

        # Flip the image horizontally for a later selfie-view display, and convert
        # the BGR image to RGB.
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        results = holistic.process(image)

        try:
            landmarks = results.pose_landmarks.landmark
            print(landmarks)
        except:
            pass

        if results.pose_landmarks:
            # Wrists
            right_wrist_x, right_wrist_y = landmarks[mp_holistic.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp_holistic.PoseLandmark.RIGHT_WRIST.value].y
            left_wrist_x, left_wrist_y = landmarks[mp_holistic.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_holistic.PoseLandmark.LEFT_WRIST.value].y
            # Fingers
            x_index_tip, y_index_tip = landmarks[mp_holistic.HandLandmark.INDEX_FINGER_TIP].x, landmarks[mp_holistic.HandLandmark.INDEX_FINGER_TIP].y
            x_thumb_tip, y_thumb_tip = landmarks[mp_holistic.HandLandmark.THUMB_TIP].x, landmarks[mp_holistic.HandLandmark.THUMB_TIP].y
            # Wheel
            wheel_x = (right_wrist_x + left_wrist_x) / 2
            wheel_y = (right_wrist_y + left_wrist_y) / 2


            # rip out the wheel
            right_wrist_x -= wheel_x
            left_wrist_x -= wheel_x
            right_wrist_y -= wheel_y
            left_wrist_y -= wheel_y
            
            k = right_wrist_y / right_wrist_x
            angle = round(atan(k), 2) * 57,3

            return angle, wheel_y
