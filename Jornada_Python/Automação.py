import pyautogui
import time
import os

os.system('cls')

pyautogui.hotkey('alt', 'tab', interval=1)
pyautogui.hotkey('ctrl', 't')
pyautogui.write(
    'https://dlp.hashtagtreinamentos.com/python/intensivao/login', interval=0.1)
pyautogui.press('enter', interval=10)
pyautogui.click(x=653, y=394)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write('seuemailaqui@gmail.com', interval=0.1)
pyautogui.press('tab', interval=1)
pyautogui.write('sua_senh@AQUI', interval=0.1)
time.sleep(2)
pyautogui.click(x=675, y=557)



os.system('pause')
os.system('cls')
# Pra abrir o chrome:
# pyautogui.press('win')
# pyautogui.write('chrome')
# pyautogui.press('enter')