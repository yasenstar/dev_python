# Created by Mouhammad Hamsho

# pip3 install pyautogui

import pyautogui as py
import time

loc = py.locateOnScreen('buttomIcon.PNG',)
c = py.center(loc)
py.moveTo(c[0], c[1])
py.click()
time.sleep()