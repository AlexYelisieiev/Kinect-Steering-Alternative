from time import sleep
import cv2
import img_processing as img_proc
import press_stuff as ps
import config


cap = cv2.VideoCapture(0)
previous_angle = 0


while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame")
        continue
    
    answer = img_proc.process_img(image)
    # left is minus, right is plus

    if answer != None:
        angle, gas_lengh = answer
        angle = round(angle[0], 1)
        if abs(angle - previous_angle) <= 2:
            previous_angle = angle
        else:
            config.IF_CONTINUE_THREAD = False
            sleep(config.TIME_TO_STOP_THREAD)
            config.IF_CONTINUE_THREAD = True
            previous_angle = angle
            ps.press_decision(angle)

cap.release()