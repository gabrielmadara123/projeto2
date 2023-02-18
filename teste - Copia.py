lista_de_jogo=[]
dic={'nome':''}
while True:
    dic['nome']=input("nome do jogo")
    ok=input("deseja postar o nome do jogo no o arquivo")
    if(ok=='sim'):
      lista_de_jogo.append(dic)
    else:
       print("e o produto nao foi adicionado")