import matplotlib,pyplot as plt
import pandas as pd

df = pd.read_csv ('../dados/clientes-v3-preparado.csv')
print(df.head(20).to_string())

# Gráfico de Barras
plt.figure(figsize=(10,6))
df['nivel_educacao'].value_counts().plot(kind='bar', color="#90f070") #https://pandas.pydata.org/docs/reference/api/pandas.data
plt.title('Divisão de Escolaridade - 1')
plt.xlabel('Nivel de Educação')
plt.ylabel('Quantidade')
plt.xticks(rotation=0)
plt.show()

x = df['nivel_educacao'].value_counts().index 
y = df['nivel_educacao'].value_counts().values

plt.figure(figsize=(10, 6))
plt.bar(x, y, color="#b83131")
plt.title('Divisão de Escolaridade -2')
plt.xlabel('Nivel de Educação')
plt.ylabel('Quantidade')

# Gráfico de pizza

plt.fugure(figsize=(10, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Distribuição de Nivel ed Educação')
plt.show()

# Gráfico de Dispersão 

plt.hexbin(df['idade'], df['salario'], gridsize=40, cmap='Blues') # https://matplotlib.org/stable/users/explain/colors/colormaps.html
plt.colorbar(label='Contagem dentro do bin')
plt.xlabel('idade')
plt.ylabel('Salário')
plt.title('Dispersão de Idade e salário')
plt.show()

# Criar o Gráfico de pizza
plt.figure(figsize=(8, 8))