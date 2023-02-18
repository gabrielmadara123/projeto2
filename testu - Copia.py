lista_de_produto=[]
dic={
    'NOME:','','QUANTIDADE:','VALOR','',
    }
while True:
    dic["NOME"]=input("QUAL EO SEU NOME")
    dic["QUANTIDADE"]=input("QUAL E A QUANTIDADE")
    dic["VALOR"]=input("QUAL E O CALOR")
    OK=input("DESEJA COLACAR NO ARQUIVO")
    if(OK=="sim"):
        lista_de_produto.append(dic)