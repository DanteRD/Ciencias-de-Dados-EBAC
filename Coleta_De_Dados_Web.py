from urllib import request
import requests
from bs4 import BeautifulSoup

url = 'https://wiki.python.org.br/AprendaMais'
requisocao = request.get(url)
extracao = BeautifulSoup(requisocao.text, features='html.parser')

# Exibir o Texto
print(extracao.text.strip())

# Filtrar a exibição pela tag
for linha_texto in extracao.find_all("h2", "p"):
	titulo = linha_texto.name.strip()
	print('titulo: ', titulo)
	
    # Contar qtd de ttulos e paragrafos
	qtd_titulos = len(extracao.find_all("h2"))
	qtd_paragrafos = len(extracao.find_all("p"))
	
for linha_texto in extracao.find_all("h2","p"):
    if linha_texto.name == 'h2':
           contar_titulos +=1 #contar_titulos = contar_titulos + 1
        elif linha_texto.nome == 'p':
           contar_paragrafos +=1 #contar_paragrafos = contar_paragrafos + 1

           print('Quantidade de titulos' , qtd_titulos)
           print('Quantidade de parágrafos' , qtd_paragrafos)
           
# exibir somente o texto das tag h2 e p
for linha_texto in extracao.find_all("h2", "p"):
     if linha_texto.nome == 'h2':
            print('titulo: /n', linha_texto.text.strip())
    if linha_texto.nome == 'p':
            print('parágrafo: /n', linha_texto.text.strip())

# exibir somente tag h2 e p
for linha_texto in extracao.find_all("h2", ):
     if linha_texto.name == 'h2':
            print('titulo: /n', linha_texto.text.strip())
            for link in titulo.find_next_siblings('p'):
                  for a in link.find_all('a', href=True)
                  print('texto link:', a.text.strip(), ' - Url:', a[href]) # type: ignore