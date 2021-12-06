from os import write
import mediapipe as mp
import cv2
import pyautogui as pygui


mp_pose = mp.solutions.pose


def process_pose_img(input_img):
    with mp_pose.Pose(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as pose:
        input_img.flags.writeable = False
        results = pose.process(input_img)

        try:
            landmarks = results.pose_landmarks.landmark
            print(landmarks)
        except:
            pass

        if results.pose_landmarks:
            right_wrist_x, right_wrist_y = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x*,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y
            left_wrist_x, left_wrist_y = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y
            
            center_x = (right_wrist_x + left_wrist_x) / 2
            center_y = (right_wrist_y + left_wrist_y) / 2
            if right_wrist_x - center_x : # порешать тут
                pygui.press('left')

            # return center_x, center_y основной вывод. комент в эксперименте
            return right_wrist_x - center_x
            