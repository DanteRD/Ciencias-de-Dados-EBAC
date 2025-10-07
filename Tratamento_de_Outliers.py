import pandas as pd 
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('clientes_limpeza.csv')

df_filtro_basico = df[df['idade'] > 100]

print('Filtro básico \n', df_filtro_basico[['nome','idade']])

# Identificar outliers com Z-score

z_scores = stats.zscore(df['idade'].dropna())
outliers = df[(z_scores > 3) | (z_scores < -3)]
print("outliers pelo Z-score: \n", outlies_z)

# Filtrar outliers com Z-score
df_zscore = df[(stats.zscore(df['idade'])< 3)]

# Identificar outliers com IQR
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_anferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

print("Limites IQR:", limite_anferior, limite_superior)

outliers_iqr = df[(df['idade'] < limite_anferior) | (df['idade'] > limite_superior)]
print("outliers pelo IQR: \n", outliers_iqr)

# Filtrar outliers com IQR
df_iqr = df[(df['idade'] >= limite_anferior) & (df['idade'] <= limite_superior)]

# Filtrar endereço invalidos 
df_endereco = df[df['endereco'].str.contains('\d+', na=False)]  

# Tratar campos de texto
df['nome'] = df['nome'].str.title().str.strip()
print('Qtd Registros com nomes grandes:', df[df['nome'].str.len() > 50].shape[0])
print('Qtd Registros com nomes pequenos:', df[df['nome'].str.len() < 3].shape[0])
print('Qtd Registros com nomes nulos:', df['nome'].isnull().sum())
      
Print('Dados com Outliers Removidos: \n', df)

# Salvar o arquivo DataFrame tratado
df.to_csv('clientes_tratado.csv', index=False)
