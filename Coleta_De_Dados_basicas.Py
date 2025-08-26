import request # type: ignore
from bs4 import BeautifulSoup
import pandas

print('Request:')
response = request.get('https: //br.financas.yahoo.com/quote/%5EBVSP/history')
print(response.text[:600])

print('BeautifulSoup: ')
soup =  BeautifulSoup(response.text, features= 'html,parser')
print(soup.prettify()[:1000])

print('pandas: ')
url_dados = pandas.read_html('https: //br.financas.yahoo.com/quote/%5EBVSP/history')
print(url_dados[0].head(10))