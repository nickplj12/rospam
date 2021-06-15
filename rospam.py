import pyautogui
import time
import pydirectinput

prompt = pyautogui.prompt('text to be spammed')
delay = 1 #the delay feature. this is how many seconds until the next chat should be sent.


while(True):
	pyautogui.press('/')
	pyautogui.write(prompt)
	pydirectinput.press('enter')
	print('Printed')
	time.sleep(delay)
