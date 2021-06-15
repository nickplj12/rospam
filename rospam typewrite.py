import pyautogui
import time
import pydirectinput

prompt = pyautogui.prompt('text to be spammed')
delay = 0 #the delay feature. this is how many seconds until the next chat should be sent. set to 0 to disable delay.


while(True):
	pyautogui.press('/')
	pyautogui.typewrite(prompt)
	pydirectinput.press('enter')
	print('Printed')
	time.sleep(delay)