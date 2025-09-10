import pandas as pd 

import pandas as pd  # Import necessário para usar DataFrame

# Lista: Uma coleção ordenada de elementos que podem ser de qualquer tipo.
lista_nomes = ["Daniel", "Ramon", "Gustavo", "Givanildo", "Matheus", "Maurilio", "Joaquim"]
print('Lista de nomes:\n', lista_nomes)
print('Primeiro nome da lista:\n', lista_nomes[0])

# Dicionário: coleção de pares chave-valor
dicionario_pessoas = {
    'nome': 'Daniel',
    'idade': 23,
    'cidade': 'Esperança',
    'altura': 1.80,
}
print('Dicionário de pessoas:\n', dicionario_pessoas)
print('Atributo do Dicionário (nome):\n', dicionario_pessoas.get('nome'))

# DataFrame: Estrutura de dados que combina lista e dicionários.
dados = [
    {'nome': 'Daniel', 'idade': 23, 'cidade': 'Esperança', 'altura': 1.82},
    {'nome': 'Ramon', 'idade': 21, 'cidade': 'Esperança', 'altura': 1.75},
    {'nome': 'Gustavo', 'idade': 20, 'cidade': 'Esperança', 'altura': 1.70},
    {'nome': 'Givanildo', 'idade': 22, 'cidade': 'Esperança', 'altura': 1.75},
    {'nome': 'Matheus', 'idade': 22, 'cidade': 'Esperança', 'altura': 1.80},
    {'nome': 'Maurilio', 'idade': 23, 'cidade': 'Esperança', 'altura': 1.78},
    {'nome': 'Joaquim', 'idade': 24, 'cidade': 'Esperança', 'altura': 1.76},
    {'nome': 'Miqueias', 'idade': 25, 'cidade': 'Esperança', 'altura': 1.66 }
]

# Criar DataFrame
df = pd.DataFrame(dados)
print('DataFrame:\n', df)

# Selecionar coluna
print('\nColuna "nome":\n', df['nome'])

# Selecionar várias colunas
print('\nColunas "nome" e "idade":\n', df[['nome', 'idade']])

# Selecionar linha pelo índice
print('\nPrimeira linha:\n', df.iloc[0])

# Atualizar coluna "altura" com novos valores
df['altura'] = [1.82, 1.75, 1.70, 1.75, 1.80, 1.78, 1.76]
print('\nDataFrame com nova coluna de altura:\n', df)

# Salvando o DataFrame em um arquivo CSV
df.to_csv(path_or_buf='dados_pessoas.csv', index=False)

# Lendo um arquivo CSV em um DataFrame
df_lido = pd.read_csv('dados_pessoas.csv')  # CORRIGIDO aqui!
print('\nLeitura do CSV:\n', df_lido)