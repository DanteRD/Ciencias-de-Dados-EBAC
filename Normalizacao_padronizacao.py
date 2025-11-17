import panda as pd
from sklearn.preprocessing import RobustScaler, MinMaxScaler, StandardScaler # Importando as bibliotecas necessárias

pd.set_option('display.width', None) # Configurando a largura máxima de exibição do DataFrame
pd.set_option('display.max_colwidth', None) # Configurando a largura máxima de exibição das colunas

df = pd.read_csv('clientes-v2-tratados.csv') # Carregando o arquivo CSV em um DataFrame

print(df.head()) # Exibindo as primeiras linhas do DataFrame

df = df.drop(labels: ['data', 'estado', 'nivel-educacao', 'numero_filhos', 'estado-civil', 'area_atuacao'], axis=1)

# Normalização do MinMaxScaler
scaler = MinMaxScaler()
df['idadeMinMaxScaler'] = scaler.fit_transform(df[['idade']]) # Aplicando MinMaxScaler na coluna 'idade'
df['salarioMinMaxScaler'] = scaler.fit_transform(df[['salario']])

min_max_scaler = MinMaxScaler(feature_range=(-1, 1)) # Normalização do MinMaxScaler com range personalizado
df['idadeMinMaxScalerRange'] = min_max_scaler.fit_transform(df[['idade']])
df['salarioMinMaxScalerRange'] = min_max_scaler.fit_transform(df[['salario']])

# padronização do StandardScaler
scaler = StandardScaler()
df['idadeStandardScaler'] = scaler.fit_transform(df[['idade']]) # Aplicando StandardScaler na coluna 'idade'
df['salarioStandardScaler'] = scaler.fit_transform(df[['salario']])

# padronização do RobustScaler
scaler = RobustScaler()
df['idadeRobustScaler'] = scaler.fit_transform(df[['idade']]) # Aplicando RobustScaler na coluna 'idade'
df['salarioRobustScaler'] = scaler.fit_transform(df[['salario']])   

print(df.head(15)) # Exibindo as primeiras linhas do DataFrame após a normalização e padronização

