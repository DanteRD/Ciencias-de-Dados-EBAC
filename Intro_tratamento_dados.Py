import pandas as pd #serve para manipulação de dados

df = pd.read_csv("c:\\Users\\Daniel Tavares\\Downloads\\clientes.csv") # Lé o arquivo CSV e armazena em um DataFrame

# Verificar os primeiros registros
print(df.head(). to_string()) # Exibe os Primeiros registros do DataFrame

# Verificar qtd de linhas e colunas 
print('Qtd: ', df.shape) # Exibe a quantidade de linhas e colunas

# Verificar os tipos de dados
print('tipagem: \n', df.dtypes) # Exibe os tipos de dados de cada coluna

# Checar valores nulos
print('valores nulos: \n', df.isnull().sum()) # Exibe a soma de valores nulos por coluna
print('valores nulos: \n ', df.info()) # Exibe informações sobre o DataFrame, incluindo valores nulos