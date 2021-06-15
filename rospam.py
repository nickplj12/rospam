import pyautogui
import time
import pydirectinput

prompt = pyautogui.prompt('text to be spammed')

while(True):
	pyautogui.press('/')
	pyautogui.write(prompt)
	pydirectinput.press('enter')
	print('Printed')
	time.sleep(1)