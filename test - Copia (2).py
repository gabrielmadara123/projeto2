import pandas as pd
# Criar um DataFrame vazio
df = pd.DataFrame(columns=["nome","descricao","quantidade","valor"])
# Dicionário a ser adicionado ao DataFrame
while True:
 novo_registro = {"nome":"","descricao":"","quantidade":"","valor":""}
 novo_registro["nome"]=input("qual nome do produto")
 novo_registro["descricao"]=input("por favor colocar a descricao do produto")
 novo_registro["quantidade"]=input("por favor colocar a quantidade do produto")
 novo_registro["valo"]=input("por favor colocar o valor do produto")


 ok=input("deseja arquivar este produto") 
 if ok.lower=='sim':
# Adicionar o novo registro ao DataFrame
   df.append(novo_registro, ignore_index=True)
 print(df)
# Imprimir o DataFrame atualizado
 df.to_csv("./dado.csv")
