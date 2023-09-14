import pandas as pd
import win32com.client as win32

# Importar bases de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

# Visualizar bases de dados
# pd.set_option('display.max_columns', None) # para ler todas as colunas sem ocultar nenhuma
# print(tabela_vendas)

# Faturamento por lojas
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum() # [[filtro]] lista filtrada e .groupby serve para agrupar uma coluna especifica .sum exemplo do que fazer com as outras colunas, nesse caso somar
print(faturamento)

print('-' * 50)
# Quantidade de produtos vendidos por loja
qtdproduto = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(qtdproduto)

print('-' * 50)

# Ticket médio por produtos em cada loja
ticket_medio = (faturamento['Valor Final'] / qtdproduto['Quantidade']).to_frame() # ().to frame() serve para pegar informações e transformar em tabelas (usar qndo dividir ou multiplicar - dtype: float64)
ticket_medio = ticket_medio.rename(columns={0:'Ticket Médio'})
print(ticket_medio)

# Enviar um email  com o relatório
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'tamimmaciel@gmail.com'
mail.Subject = 'Relatório de Vendas por Loja'
mail.HTMLBody = f'''

<p>Prezados,</p>

<p>Segue relatório de Vendas  por  cada Loja.</p>

<p>Faturamento:</p>
{faturamento.to_html(formatters={'Valor Final':'R${:,.2f}'.format})}

<p>Quantidade Vendida:</p>
{qtdproduto.to_html(formatters={'Quantidade':'{:,.0f}'.format})}

<p>Ticket médio dos Produtos em cada Loja:</p>
{ticket_medio.to_html(formatters={'Ticket Médio':'R${:,.2f}'.format})}


<p>Á disposição</p>

<p>Atenciosamente,</p>

<p>Tamim Maciel</p>

'''

mail.Send()

print('''
E-mail enviado!
      ''')
