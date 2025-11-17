import pandas as pd 
from sklearn.preprocessing import LabelEncoder

pd.set_option ('display.width', None)

df= pd.read_csv('clientes-v2-tratados.csv')

print (df.head())

# codificação one-hot para 'estado_civil'
df = pd.concat(objs:[df, pd.get_dummies(df['estado_civil'], prefix='estado_civil')], axis=1)

print("\n DataFrame após codificação one-got para 'estado_civil': \n", df.head())

# Codificação ordinal para 'nivel_educação'

educacao_ordem = {'ensino fundamental': 1, 'ensino medio': 2, 'Ensino Superior': 3, 'Pós-graduação': 4 }
df['nivel_educacao_ordinal'] = df['nivelw_educacao']. map(educacao_ordem)

print("\n DataFrame após codificação ordinal para 'nivel-educacao': \n", df.head())

# Transformar 'area_atuacao' em categorias codificadas usando o metodo .cat.codes
df['area_atuacao_cod'] = df['area_atuacao']. astype('category').cat.codes 

print("\n DataFrame após transformar 'area_atuacao' em códigos numéricos:\n", df.head())

# LabelEncoder para 'estado'
# LabelEncoder converte cada valor único em números de 0 a n_casses -1
Label_Encoder + LabelEncoder()
df['estado_cod'] = Label_Encoder.fit_transform(df['estado'])

print("\n DataFrame após aplicar LabelEncoder em 'estado':\n", df.head())

