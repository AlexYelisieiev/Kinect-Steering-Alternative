import mediapipe as mp
from math import sqrt
import cv2


mp_hands = mp.solutions.hands


def process_hands_img(input_img):
    with mp_hands.Hands(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:

        results = hands.process(input_img)

        for hand_landmarks in results.multi_hand_landmarks:
            x_index_tip, y_index_tip = hand_landmarks.landmark[
                mp_hands.HandLandmark.INDEX_FINGER_TIP].x, hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
            x_thumb_tip, y_thumb_tip = hand_landmarks.landmark[
                mp_hands.HandLandmark.THUMB_TIP].x, hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y

            # find the distance between index and thumb fingers
            lengh_hands = sqrt((x_thumb_tip - x_index_tip)**2 +
                               (y_thumb_tip - y_index_tip)**2)
            lengh_hands = round(lengh_hands * 2, 2)  # normalize lengh_hands
            if lengh_hands > 1:
                lengh_hands = 1
            elif lengh_hands < 0:
                lengh_hands = 0
            return lengh_hands
