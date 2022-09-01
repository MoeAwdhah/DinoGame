from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from pynput.keyboard import Key, Controller

button = Controller()

while keyboard.is_pressed('q') == False:

    e,f,v = pyautogui.pixel(1220, 318)

    if e == 83:
    
        while keyboard.is_pressed('q') == False:
            r,g,b = pyautogui.pixel(770, 419)

            if b == 83:
                button.press(Key.up)
                time.sleep(0.1)
                button.release(Key.up)
                print("far")

            else:
                break

    else:
        r,g,b = pyautogui.pixel(750, 419)

        if b == 83:
            button.press(Key.up)
            time.sleep(0.2)
            button.release(Key.up)
            print("close")
