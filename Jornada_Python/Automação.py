import pyautogui
import os

pyautogui.hotkey('alt', 'tab', interval=0.5)
pyautogui.hotkey('ctrl', 't')
pyautogui.write(
    'https://dlp.hashtagtreinamentos.com/python/intensivao/login', interval=0.1)
pyautogui.press('enter')







os.system('cls')
# Pra abrir o chrome:
# pyautogui.press('win')
# pyautogui.write('chrome')
# pyautogui.press('enter')