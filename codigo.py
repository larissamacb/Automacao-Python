import pyautogui
import time
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)

pyautogui.PAUSE = 1

# Iniciar o Chrome
pyautogui.click(x=758, y=1050)
pyautogui.write("chrome")
pyautogui.press("enter")

# Ir para a página que será utilizada e logar
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=940, y=509)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("minha senha")
pyautogui.click(x=946, y=706)

# Preencher os dados
for linha in tabela.index:
    pyautogui.click(x=901, y=368)

    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(tabela.loc[linha, "obs"])

    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(1000)
