import pyautogui
import time
import pandas as pd

# pyautogui.click # Para clicar com Mouse / para definir quantidade de cliques 'pyautogui.click(x=441, y=396, clicks=2)' botão direito e esquerdo button='right' ou 'left'
# pyautogui.write # Para escrever um texto
# pyautogui.press # Para pressionar uma tecla
# pyautogui.hotkey # Para teclas de atalhos (combinação de teclas) exe: pyautogui.hotkey('ctrl', 'c')

# Abrir o Chrome
pyautogui.PAUSE= 1 # Pausa a cada comando
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# Entrar no sistema da empresa
    #  https://dlp.hashtagtreinamentos.com/python/intensivao/login
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

# Esperar o site carregar
time.sleep(3) # Executa uma unica vez

# 2. Fazer login
pyautogui.PAUSE= 1
pyautogui.click(x=441, y=396)
pyautogui.write('tamimmaciel@gmail.com')
pyautogui.press('tab')
pyautogui.write('1234')
pyautogui.press('tab')
pyautogui.press('enter')

# esperar o site carregar
time.sleep(3)

# 3. Importar a base de dados de produtos
tabela = pd.read_csv('produtos.csv')

for linha in tabela.index:

    # 4. Cadastrar 1 produto
    pyautogui.click(x=453, y=266)

    codigo = tabela.loc[linha, 'codigo'] # Defiinir a variavel fora da linha de código
    
    # Preencher campos
    pyautogui.write(str(codigo)) # Defiinir a variavel fora da linha de código
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'marca'])) # Ou defiinir a variavel dentro da linha de código (ideal para escrever menos)
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):          # if not "se não" .isna "sem valor ou vazio", nesse caso le-se (Se não estiver vazio escrever o texto da OBS)
        pyautogui.write(str([obs]))

    # Enviar formulario
    pyautogui.press('tab')
    pyautogui.press('enter')

    # Voltar formulário para o topo
    pyautogui.scroll(1000)

# 5. Repetir o cadastro para todos o produtos
# Utiizando for linha in tabela.index: