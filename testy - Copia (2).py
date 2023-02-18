import pandas as pd
# Dicionário a ser adicionado ao DataFrame
df = pd.DataFrame(columns=["janeiro","fevereiro","marco","abriu"])
while True:
    lista_de_vendas={"janeiro:":"","fevereiro:":"","marco:":"","abriu:":"", }
    lista_de_vendas["janeiro"]=input["quantas vendas o usuario fez em janeiro "]
    lista_de_vendas["fevereiro:"]=input["quantas vendas o usuario fez em fevereiro "]
    lista_de_vendas["marco:"]=input["quantas vendas o usuario fez em marco "]
    lista_de_vendas["abriu:"]=input["quantas vendas o usuario fez em abriu "]

    ok=input("deseja arquivar suas vendas ? ")
    if ok == "sim":
        df.append(lista_de_vendas, ingnore_index=True)
        print(df)
        df.to_csv("/dada.csv")
        