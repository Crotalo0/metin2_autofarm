# autoclicker test
import pydirectinput
from time import sleep
import threading
import win32gui
import keyboard
import os


def callback(hwnd):
    if win32gui.IsWindowVisible(hwnd):
        print(f"window text: '{win32gui.GetWindowText(hwnd)}'")


def corpo_forte():
    while True:
        pydirectinput.keyDown('4')
        sleep(0.2)
        pydirectinput.keyUp('4')
        sleep(0.3)
        pydirectinput.keyDown('4')
        sleep(0.2)
        pydirectinput.keyUp('4')
        sleep(103)


def green_and_violet_pots():
    while True:
        pydirectinput.keyDown('2')
        sleep(0.19)
        pydirectinput.keyUp('2')
        sleep(1.49)
        pydirectinput.keyDown('3')
        sleep(0.19)
        pydirectinput.keyUp('3')
        sleep(10 * 60)


def loot_and_pots():
    while True:
        sleep(0.08)
        pydirectinput.keyDown('z')
        sleep(0.16)
        pydirectinput.keyDown('1')
        sleep(0.04)
        pydirectinput.keyUp('z')
        sleep(0.03)
        pydirectinput.keyUp('1')


def main():
    # win32gui.EnumWindows(callback, None)

    print('Get metin2 focus in 3 seconds and wait...')
    sleep(3)
    test = win32gui.GetForegroundWindow()
    window = win32gui.GetWindowText(test)

    s1 = threading.Thread(target=corpo_forte)
    s2 = threading.Thread(target=loot_and_pots)
    s3 = threading.Thread(target=green_and_violet_pots)

    if window == 'METIN2':
        print('starting!')
        s1.start()
        s2.start()
        s3.start()
        print('everything started.')


if __name__ == "__main__":
    main()
    while True:
        if keyboard.is_pressed('p'):
            print(' p key pressed, preparing to shutdown.')
            os._exit(getattr(os, "_exitcode", 0))
