import pandas as pd  
lista_de_produtos=pd.read_csv("./dado.csv")#lendo o caminho do arquivo
dic={
    'nome':'','QUANTIDADE':'','DESCRIÇAO':'','VALOR':'',
}
while True:
   dic['DESCRIÇAO']=input('coloque a descriçao')
   dic['nome']=input('coloque o nome do produto')
   dic['QUANTIDADE']=input('por favor coloque a quantidade de produto')
   dic['VALOR']=input('por favor coloque o valor do produto')
   ok=input('deseja armazenar este produto')
   if(ok=='sim'): 
     lista_de_produtos.append(str (dic),ignore_index=True)#eu estou adicionando comando no final da dataframe = e uma planilha que eu abaixei como variavel
   else:   
        print("o produto nao foi adicionado")
lista_de_produtos.to_csv("./dado.csv")