import pyautogui
import time

pyautogui.PAUSE = 0.3


pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("Enter")
time.sleep(1)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("Enter")
time.sleep(1)

pyautogui.click(x=426, y=378)
pyautogui.write("emailteste@gmail.com")
pyautogui.press("Tab")
time.sleep(1)
pyautogui.write("senhateste123")
pyautogui.click(x=642, y=531)
time.sleep(1)

import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)




