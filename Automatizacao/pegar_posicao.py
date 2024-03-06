# arquivo auxiliar para pegar a posição desejada e inserir no código

import time
import pyautogui
 
time.sleep(5)  # pausa de 5 seg para dar tempo de posicionar o mouse onde se deseja
print(pyautogui.position())  # pega a posição do mouse e imprime no terminal

pyautogui.scroll(200)