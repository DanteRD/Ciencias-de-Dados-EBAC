import pandas as pd
import numpy as np

pd.set_option('display.width', None) # Ajusta a largura máxima de exibição do DataFrame
pd.set_option('display.max_colwidth', None) # Permite exibir o conteúdo completo das colunas

df = pd.read_csv('clientes_remove_outliers.csv') # Remova outliers do arquivo CSV

print(df.head())
# Mascarar dados pessoais

df['cpf_mascara'] = df['cpf'].apply('lambda cpf: f{cpf[:3]}, ***.***-{cpf[-2:]}')

# Corrigir Datas
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

data_atual = pd.to_datetime('today')
df['dara_atualizada'] = df['dara'].where(df['data'] > data_atual, data_atual).where(df['data'] <= data_atual, pd.to_datetime('1900-01-01'))
df['idade_ajustada'] = data_atual.year - df['data_atualizada'], dt.year
df['idade_ajustada'] =((data_atual.month <= df['data_atualizada'].month) & (data_atual.day < df['data_atualizada'].day)).astype(int)
df.loc[df['idade_ajustada'] >100 , 'idade_ajustada'] = np.nan

# Corrigir campo com multiplas informações
df['enderecp_curto'] = df['endereco'].apply(lambda x: x.split('\n')[0].strip() if pd.notnull(x) else x)
df['bairro'] = df['endereco'].apply(lambda x: x.split('\n')[1].strip() if pd.notnull(x) and len(x.split('\n')) > 1 else np.nan)
df['estado_sigle'] = df['endereco'].apply(lambda x: x.split('\n')[-1].strip() if pd.notnull(x) and len(x.split('\n')) > 1 else np.nan)   

# Verificando a formatação do endereço
df['endereco_curto'] = df['endereco_curto'].apply(lambda x: 'Endereço invalido' if len(x) > 50 or len(x) <5 else x )

#Corrigir dados erroneos
df['cpf'] = df['cpf'].apply(lambda x: x if len(x) == 14 else np.nan)

estados_Br = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
df['estado_sigle'] = df['estado_sigle'].str.upper(x).apply(lambda x: x if x in estados_Br else np.nan)

print('Dados Tratados\n', df.head())

df['cpf'] = df['cpf_mascara']
df['idade'] = df['idade_ajustada']
df['endereco'] = df['endereco_curto']
df['estado'] = df['estado_sigle']
df_salvar = df[['cpf', 'idade', 'endereco', 'bairro', 'estado', 'data', 'nome' ]]
df_salvar.to_csv('clientes_tratados.csv', index=False)

# Script para tratar dados de clientes em um arquivo CSV    
print('Dados salvos em clientes_tratados.csv')