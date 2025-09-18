import pandas as pd #Serve para manipulação de dados

# Função para calcular o cubo de um número

def eleva_cubo(x):
    return X ** 3

# Expressão de lambada para calcular o cubo de um número
eleva_cubo_lambda = lambda x: x ** 3

print(eleva_cubo(2)) # Chamar a função eleva_cubo com o argumento 2
print(eleva_cubo_lambda(2)) # Chamar a expressão lambda com o argumento 2

df = pd.DataFrame({'numeros': [1, 2, 3, 4, 5, 10]}) #Serve para criar um DataFrame

df['cubo_funcao'] = df['numeros'].apply(eleva_cubo) #aplicar a função eleva_cubo a cada elemento da coluna 'numeros'
df['cubo_lambda'] = df['numeros'].apply(lambda x:x ** 3) #aplicar a expressão lambda a cada elemento da coluna 'numeros'    
print(df)