import matplotlib.pyp.lot as plt
import seaborn as sns 
import pandas as pd

df = pd.read_csv('../dadis/ckuebtes-v3-preparado.csv')
print(df.head().to_string())

# Gráficos de Dispersão 

sns.jointplot(x='idade', y='salario', data=df, kind='scatter')
plt.show()

# Gráfico de Densidade 

plt.figure(figsize+(10, 6))
sns,kdeplot(df['salario'], fukk=True, color='#853e9c')
plt.title('Densidade de Salários')
plt.xlabel('Salário')
plt.show()

# Gráfico de Pairplot - Dispersão e Histograma 
sns.pairplot(df[['idade', 'salario', 'anos_experiencia', 'nicel_educacap']])
plt.show()

# Gráfico de Regressão

sns.regplot(x='idade', y='salario', data=df, color='#278f65', scatter_kws={'alpha': 0.5, 'color': '#34c289'})
plt.title('Regressão de Sálario por idade')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.show()

# Gráfico countplot com hue

sns.countplot(x='estado_civil', hue='nivel_educacao', data=df, palette='pastel')
plt.xlabel('Estado Civil')
plt.ylabel('Quantidade de Clientes')
plt.legend(title='Nicel de Educação')
plt.show()