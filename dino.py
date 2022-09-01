from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from pynput.keyboard import Key, Controller

button = Controller()

while keyboard.is_pressed('q') == False:
# to turn the program off press q

    e,f,v = pyautogui.pixel(1220, 318)

    if e == 83:
    
        while keyboard.is_pressed('q') == False:
            b = pyautogui.pixel(770, 419)

            if b == 83:
                button.press(Key.up)
                time.sleep(0.1)
                button.release(Key.up)
                print("far")
                # the program prints far when it's looking for a grey pixels far from the player character (for testing perposes)
            else:
                break

    else:
        r,g,b = pyautogui.pixel(750, 419)

        if b == 83:
            button.press(Key.up)
            time.sleep(0.2)
            button.release(Key.up)
            print("close")
            # the program prints close when it's looking for a grey pixels close to the player character (for testing perposes)
