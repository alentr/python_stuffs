from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import re

# Caminho para o ChromeDriver (atualize para o caminho correto no seu sistema)
driver_path = '/caminho/para/seu/chromedriver'

# Caminho do arquivo .txt com as mensagens
file_path = 'C:\\Users\\telles-alexandre\\Desktop\\mensagens.txt'

# Nome do grupo do WhatsApp
group_name = 'teste'

# Função para enviar a mensagem
def enviar_mensagem(message):
    # Encontrar o campo de texto para enviar a mensagem
    campo_mensagem = driver.find_element(By.XPATH, '(//div[@contenteditable="true"])[2]')
    campo_mensagem.send_keys(message + Keys.ENTER)

# Configurar o navegador
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=/tmp/chrome_user_data')  # Manter sessão logada

# Iniciar o driver do navegador
driver = webdriver.Chrome(options=options)

# Abrir o WhatsApp Web
driver.get("https://web.whatsapp.com/")

# Aguardar o tempo suficiente para fazer login manualmente (escaneando o QR code)
print("Por favor, escaneie o QR Code para fazer login no WhatsApp Web.")
time.sleep(5)  # Aumente o tempo se necessário para escanear o QR code

# Buscar o grupo específico
def selecionar_grupo():
    try:
        grupo = driver.find_element(By.XPATH, f'//span[@title="{group_name}"]')
        grupo.click()
    except Exception as e:
        print("Erro ao tentar encontrar o grupo:", e)

# Função para interpretar as mensagens no formato desejado
def interpretar_mensagem(linha):
    # Regex para capturar o padrão da linha
    padrao = r'\[(.*?)\] (.*?): (.*)'
    match = re.match(padrao, linha.strip())
    if match:
        data_hora = match.group(1)  # Captura a data e hora
        pessoa = match.group(2)     # Captura o nome da pessoa
        conteudo = match.group(3)   # Captura o conteúdo da mensagem
        # Formatar a mensagem como solicitado
        return f"[{data_hora}] {pessoa}: {conteudo}"
    return None  # Retorna None se a linha não estiver no formato esperado

# Ler as mensagens do arquivo .txt
with open(file_path, 'r', encoding='utf-8') as file:
    linhas = file.readlines()

# Selecionar o grupo no WhatsApp
selecionar_grupo()

# Aguardar o carregamento do grupo
time.sleep(3)

# Enviar as mensagens uma por uma
for linha in linhas:
    if '\u2002' in linha:
        continue  # Pula para a próxima mensagem
    
    mensagem_interpretada = interpretar_mensagem(linha)
    if mensagem_interpretada:  # Apenas envia mensagens válidas
        enviar_mensagem(mensagem_interpretada)
        time.sleep(1)  # Aguardar 2 segundos entre o envio de cada mensagem

# Fechar o navegador
driver.quit()
