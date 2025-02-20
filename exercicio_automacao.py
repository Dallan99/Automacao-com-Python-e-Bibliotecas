import pyautogui
import time

pyautogui.PAUSE = 0.5 # esperar 0.5 segundos a cada comando

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(1)

pyautogui.click(x=507, y=433)
pyautogui.write('https://www.hashtagtreinamentos.com')
pyautogui.press('enter')

time.sleep(1.5) # pausa de 1.5 segundos 
pyautogui.click(x=1006, y=47)
pyautogui.moveTo(x=359, y=169)
pyautogui.moveTo(x=640, y=279)
pyautogui.click(x=640, y=279)
time.sleep(2)
pyautogui.click(x=365, y=583)
pyautogui.write('Dallan')
pyautogui.press('tab')
pyautogui.write('Dallanr@gmail.com')
pyautogui.press('tab')
pyautogui.write('19999365777')
pyautogui.press('tab')
#pyautogui.press('enter')
time.sleep(2)