import pyautogui
import time

comments = ["hello", "hi"]

time.sleep(5)

for i in range(100):
    pyautogui.typewrite(comments[i%2])
    pyautogui.typewrite("\n")
