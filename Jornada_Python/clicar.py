import time
import pyautogui
import os

os.system('cls')

print('Posição do mouse: ', end='')
time.sleep(5)
print(pyautogui.position())

os.system('pause')
os.system('cls')