import webbrowser
from time import sleep
import pyautogui

webbrowser.open('https://www.worten.pt/')

sleep(3)

cartao_credito = pyautogui.locateCenterOnScreen('cartao_credito.png')
pyautogui.click(cartao_credito[0], cartao_credito[1])
