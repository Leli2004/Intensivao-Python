# facilita esquematizar o passo a passo (a lógica) do que será feito

# importações
# pip install pyautogui
# pip install pandas numpy openpyxl
import pyautogui
import time
import pandas

pyautogui.PAUSE = 1  # a cada comando do pyautogui é feito uma pausa em segundos com o tempo definido aqui 
#############
## Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# abrir o navegador (chrome)
pyautogui.press("win") # pressionar tecla win
pyautogui.write("chrome") # escrever 'chrome'
pyautogui.press("enter") # dar enter

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link) # colar o link
# pyautogui.hotkey("crtl", "v")
pyautogui.press("enter") # dar enter
time.sleep(3)

#############
## Passo 2: Fazer login
# a posição da tela será pegada pelo arquivo pegar_posicao
pyautogui.click(x=500, y=404)
pyautogui.write("teste@gmail.com")

pyautogui.press("tab") # ir para próximo campo do form
pyautogui.write("senha aqui")

pyautogui.click(x=673, y=570) # botão logar
time.sleep(3)

#############
## Passo 3: Importar a base de produtos pra cadastrar
# ler arquivo formato csv = read_formato
tabela = pandas.read_csv("produtos.csv")  # para ler o arquivo

#############
## Passo 4: Cadastrar um produto

for linha in tabela.index:
    # clicar no 1° input do formulário
    pyautogui.click(x=630, y=286) 
    # pegar da tabela o valor do campo que a gente quer preencher
        # codigo = tabela.loc[linha, coluna] 
        # Forma mais longa:
        #codigo = tabela.loc[linha, "codigo"]  --> loc serve para ler 
        #pyautogui.write(codigo)
        #pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):     # se a obs não estiver vazia == preenche
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")

    #enviar
    pyautogui.press("enter")

    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)

    time.sleep(3)
