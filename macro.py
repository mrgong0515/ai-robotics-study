import time
import pyautogui

time.sleep(1)
pyautogui.hotkey("win", "r")
time.sleep(0.5)
pyautogui.write("notepad")
pyautogui.press("enter")
time.sleep(0.5)
# Hello World!! 입력하고
pyautogui.typewrite(list("Hello World!!"), interval=0.1)
# 그 글씨를 최대로 키우는 프로그램\
for _ in range(20):
    pyautogui.hotkey("ctrl", "=")
    time.sleep(0.05)