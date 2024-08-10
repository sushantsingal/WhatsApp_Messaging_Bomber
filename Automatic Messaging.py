import pyautogui
import os
import time
os.system("start whatsapp://")
time.sleep(4)

message = "Lund"
for i in range(200):
    pyautogui.typewrite(message)
    pyautogui.press("enter")