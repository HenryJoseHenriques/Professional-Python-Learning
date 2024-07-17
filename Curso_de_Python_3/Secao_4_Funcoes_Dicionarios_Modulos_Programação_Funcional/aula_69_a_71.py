listaDeCompras = []

def Mercado(*x):
    for i in x:
        listaDeCompras.append(input("Digite um item para a lista:\n"))

Mercado(1,2,3,4,5,8,6,7,8,9)

num = 10,20,30,40,50,60,70,80,90,100 #empacotamento

Mercado(*num) #desempacotamento