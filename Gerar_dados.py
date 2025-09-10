import pandas as pd #importar pandas para liberar datafranes
import random 
from faker import Faker #importar faker para generar dados aleatorios

faker = Faker('pt_BR') #configurar faker para generar dados em portugues do brasil

dados_pessoas = [] #cruiar lista vazia para armazenar os dados das pessoas

for _ in range(10): #criar um loop para gerar 100 pessoas
    nome = faker.name() #gerar nome aleatorio
    cpf = faker.cpf() #gerar cpf aleatorio
    idade = random.randint(18, 80) #gerar idade aleatoria entre 18 e 80
    data = faker.date_of_birth(minimum_age=idade, maximum_age=idade).strftime("%d/%m/%Y") #gerar data de nascimento com base na idade
    endereco = faker.address().replace("\n", ",") #gerar endereço aleatorio e substituir quebras de linha por virgulas
    estado = faker.estado_sigla() #gerar estado aleatorio
    pais = 'Brasil' #definir pais como brasil

    #criar dicionario para armazenar os dados da pessoa
    pessoa =  {
        "nome": nome,
        "cpf": cpf,
        "idade": idade,
        "data_nascimento": data,
        "endereco": endereco,
        "estado": estado, 
        "pais": pais, 
    }
    
    dados_pessoas.append(pessoa) #adicionar o dicinario a lista de dados das pessoas 

df_pessoas = pd.DataFrame(dados_pessoas) #criar dataframe com os dados das pessoas 
print(df_pessoas) #imprimir o dataframe

pd.set_option('display.max_columns', None) #configurar pandas para mostrar todas as colunas
pd.set_option('display.max_rows', None) #configurar pandas para mostrar todas as linhas 
pd.set_option('display.max_colwidth', None) #configurar pandas para mostrar toda a largura 
pd.set_option('display.width', None) #configurar pandas para mostrar toda a largura do dataframe

print(df_pessoas.to_string()) #imprimir o dataframe como string para mostrar todo o conteudo

df_pessoas.to_csv('clientes.csv')