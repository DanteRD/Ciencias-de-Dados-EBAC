# Análise Exploratória de Dados ou AED em python
import pandas as pd

df = pd.read_csv('. . /dados/clientes-v2.csv')

print(df.head().to_string())
print(df.tail().to_string())
df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

print('Verificação inicial:')
print(df.info())

print('Analise de dados nulos> \n', df.isnull().sum())
print('% de dados nulos> \n', df.isnull().mean() * 100)
df = df.dropna(inplace=True)
print('Confirmar remoção de dados nulos \n', df.isnull().sum().sum())

print('Analide de dados duplicados: \n', df.duplicated().sum())

print ('Analise de dados únicos \n', df.nunique())

print('Estatísticas dos dados: \n', df.describe(include='all').to_string())

df = df[['odade', 'estado', 'salario', 'nivel educação', 'numero_filhos', 'Estado_civil', 'area_atuação']]
print(df.head().to_string())

df.to_csv('. . /dados/clientes-v3.csv', index=False)
