import pandas as pd  # Importa a biblioteca pandas com o apelido 'pd'

# Leitura do arquivo CSV
df = pd.read_csv('c: //Users//Daniel Tavares//Donwload//clientes.csv')  # Lê o arquivo 'clientes.csv' e armazena o conteúdo no DataFrame 'df'

# Configurações de exibição
pd.set_option('display.width', None)  # Ajusta a largura máxima para exibir o DataFrame completo
print(df.head())  # Mostra as primeiras linhas do DataFrame

# Remover dados
df.drop(labels='pais', axis=1, inplace=True)  # Remove a coluna 'pais'
df.drop(labels=2, axis=0, inplace=True)  # Remove a linha com índice 2

# Normalizar campos de texto 
df['nome'] = df['nome'].str.title()  # Coloca a primeira letra de cada palavra em maiúsculo
df['endereco'] = df['endereco'].str.lower()  # Coloca todo o texto da coluna 'endereco' em minúsculo
df['estado'] = df['estado'].str.strip().str.upper()  # Remove espaços em branco e coloca todo o texto em maiúsculo

# Converter tipos de dados
df['idade'] = df['idade'].astype(int)  # Converte a coluna 'idade' para o tipo inteiro

# Tratar valores nulos (ausentes)
df_fillna = df.fillna(0)  # Cria uma cópia do DataFrame substituindo valores nulos por 0
df_dropna = df.dropna()  # Cria uma cópia do DataFrame removendo linhas com qualquer valor nulo
df_dropna4 = df.dropna(thresh=4)  # Cria uma cópia mantendo linhas com pelo menos 4 valores não nulos
df = df.dropna(subset=['cpf'])  # Remove registros com valores nulos na coluna 'cpf'

# Exibir informações sobre valores nulos
print('Valores nulos: \n', df.isnull().sum())  # Mostra a quantidade de valores nulos por coluna
print('Qtd de registros nulos com fillna:', df_fillna.isnull().sum().sum())  # Total de nulos após o fillna
print('Qtd de registros nulos com dropna:', df_dropna.isnull().sum().sum())  # Total de nulos após o dropna
print('Qtd de registros nulos com dropna4:', df_dropna4.isnull().sum().sum())  # Total de nulos após o dropna com thresh
print('Qtd de registros após dropna cpf:', df.isnull().sum().sum())  # Total de nulos após remoção com base no CPF

# Preenchendo valores nulos com valores personalizados
df.fillna(value={'estado': 'Desconhecido'}, inplace=True)  # Substitui valores nulos na coluna 'estado' por 'Desconhecido'
df['endereco'] = df['endereco'].fillna('Endereço não informado')  # Substitui valores nulos na coluna 'endereco'
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean())  # Cria nova coluna substituindo nulos pela média de idade

# Tratar formato de dados 
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')  
# Converte a coluna 'data' para o formato datetime; datas inválidas se tornam NaT

# Tratar dados duplicados
print('Qtd de registros atual:', df.shape[0])  # Mostra a quantidade de registros antes da remoção de duplicados
df.drop_duplicates(inplace=True)  # Remove registros completamente duplicados
df.drop_duplicates(subset=['cpf'], inplace=True)  # Remove duplicados com base apenas na coluna 'cpf'
print('Qtd de registros removendo as duplicadas:', len(df))  # Mostra o número de registros após remoção

print('Dados limpos:\n', df)  # Mostra o DataFrame limpo

# Atualizar colunas com dados corrigidos
df['data'] = df['data_corrigida']  # Substitui a coluna 'data' original pela corrigida
df['idade'] = df['idade_corrigida']  # Substitui a coluna 'idade' original pela corrigida

# Criar novo DataFrame apenas com as colunas desejadas
df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'estado']]  # Seleciona colunas específicas

# Salvar o novo DataFrame em um arquivo CSV
df_salvar.to_csv('clientes_limpeza.csv', index=False)  # Salva o DataFrame no arquivo 'clientes_limpeza.csv' sem o índice

# Verificar se salvou corretamente
print('Novo DataFrame: \n', pd.read_csv('clientes_limpeza.csv'))  # Lê o novo arquivo e exibe o conteúdo
