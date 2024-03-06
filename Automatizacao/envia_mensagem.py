import pyautogui
import time
import pandas

pyautogui.PAUSE = 1 

# Por WhatsApp:
'''
pyautogui.press("win") 
pyautogui.write("WhatsApp") 
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("Lela")
pyautogui.click(x=201, y=181)
pyautogui.write("Mensagem automática com pyautopy :)")
pyautogui.press("enter")
'''

##### Por Email
'''
pyautogui.press("win") 
pyautogui.write("chrome") 
pyautogui.press("enter") 

link = "https://mail.google.com/mail/u/0/#inbox"
pyautogui.write(link) 
pyautogui.press("enter") 
time.sleep(2)

dados = pandas.read_csv("envia-email.csv")

for linha in dados.index:

    pyautogui.click(x=84, y=219)

    pyautogui.write(str(dados.loc[linha, "email"]))
    pyautogui.press("enter")
    pyautogui.press("tab")

    pyautogui.write(str(dados.loc[linha, "assunto"]))
    pyautogui.press("tab")

    pyautogui.write("Oi,")
    pyautogui.press("enter")
    pyautogui.write("Segue seu arquivo.")
    pyautogui.press("enter")
    pyautogui.write("Atenciosamente, Leli :)")
    pyautogui.press("enter")

    pyautogui.click(x=958, y=686)
    pyautogui.write(str(dados.loc[linha, "arquivo"]))
    pyautogui.press("down")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press("tab")
    pyautogui.press("enter")

    time.sleep(2)
'''