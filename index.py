import pyautogui
import time

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("Enter")
time.sleep(1)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("Enter")
time.sleep(1)
pyautogui.click(x=426, y=378)


