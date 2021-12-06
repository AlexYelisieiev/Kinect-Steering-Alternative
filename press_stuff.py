from threading import Thread
from time import sleep
import keyboard as k
import config


def turn_right():
    while True:
        if config.IF_CONTINUE_THREAD:
            k.press('right')
            sleep(config.TIME_TO_PRESS)
            k.release('right')
        else:
            break


def turn_left():
    while True:
        if config.IF_CONTINUE_THREAD:
            k.press('left')
            sleep(config.TIME_TO_PRESS)
            k.release('left')
        else:
            break


def press_decision(angle):
    if angle <= -23:
        thread = Thread(target=turn_left)
        thread.start()
    if angle >= 23:
        thread = Thread(target=turn_right)
        thread.start()
