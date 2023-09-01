import pandas as pd
import os
from twilio.rest import Client

# Encontre o SID da sua conta e o token de autenticação em twilio.com/console
# e defina as variáveis de ambiente. Veja http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# Passo a passo de solução:
# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

# Para cada arquivo:
# 1- Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000
# 2 - Se for maior do que 55.000 -> Envia um SMS com Nome, o mês e as vendas do vendedor
# 3 - Caso não seja maior do que 55.000 não fazer nada

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any(): # .any() para mostrar dentro da tabela que se trata de algum valor na coluna 'Vendas'
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0] # .loc[] para localizar dentro da coluna 
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]     # e .values[0] pra não trazer a tabela só o valor
        print(f'No mês de {mes} alguém bateu a meta: Vendedor: {vendedor}, Venda: {vendas}')

        # Configuração do Twilio para enviar o SMS
        message = client.messages \
                .create(
                     body=f'No mês de {mes} alguém bateu a meta: Vendedor: {vendedor}, Venda: {vendas}'
                     from_='+15017122661',
                     to='+5511982338948'
                 )

        print(message.sid)

# Bibliotecas baixadas através do "pip install" :
# - pandas  (Para integração do Python com Excel)
# - openpyxl (Para integração Python com Excel)
# - twilio (Para integração Python com SMS)
