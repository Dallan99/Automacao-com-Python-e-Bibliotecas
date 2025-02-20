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

time.sleep(3) # pausa de 3 segundos 
pyautogui.click(x=2389, y=66)
pyautogui.moveTo(x=1711, y=177)
pyautogui.moveTo(x=1969, y=276)
pyautogui.click(x=1969, y=276)
time.sleep(2)
pyautogui.click(x=1549, y=590)
pyautogui.write('Dallan')
pyautogui.press('tab')
pyautogui.write('Dallanr@gmail.com')
pyautogui.press('tab')
pyautogui.write('19999365777')
pyautogui.press('tab')
#pyautogui.press('enter')
time.sleep(3)