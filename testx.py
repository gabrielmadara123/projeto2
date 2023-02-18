import pandas as pd
#Criar um DataFrame vazio
df = pd.DataFrame(columns=["nome","descricao","quantidade","valor"])
## Dicionário a ser adicionado ao DataFrame
while True:
    novo_registro = {"nome":"","descricao":"","quantidade":"","valor":""}
    novo_registro["nome"] = input("Qual é o nome do produto? ")
    novo_registro["descricao"] = input("Por favor, insira a descrição do produto: ")
    novo_registro["quantidade"] = input("Por favor, insira a quantidade do produto: ")
    novo_registro["valor"] = input("Por favor, insira o valor do produto: ")
    
    ok = input("Deseja arquivar este produto? ")
    if ok == "sim":
        df = df.append(novo_registro, ignore_index=True)
        print(df)
        df.to_csv("./dado.csv")
