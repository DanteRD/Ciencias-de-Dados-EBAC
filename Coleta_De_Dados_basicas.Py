import requests
from bs4 import BeautifulSoup
import pandas as pd

# Simula um navegador para evitar bloqueio
headers = {'User-Agent': 'Mozilla/5.0'}

print('🔗 Request:')
url = 'https://br.financas.yahoo.com/quote/%5EBVSP/history'
response = requests.get(url, headers=headers)
print(response.text[:600])  # Mostra os primeiros 600 caracteres

print('\n🔍 BeautifulSoup:')
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify()[:1000])  # Mostra os primeiros 1000 caracteres do HTML formatado

print('\n📊 pandas:')
try:
    tabelas = pd.read_html(response.text)
    display(tabelas[0].head(10))  # Exibe como tabela no Jupyter
except ValueError as e:
    print(f"Nenhuma tabela encontrada. Erro: {e}")
