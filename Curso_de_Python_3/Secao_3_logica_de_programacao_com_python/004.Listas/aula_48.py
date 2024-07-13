"""
Lista em Python
Tipo list - mutável
Suporta vários valores de qualquer tipo
Conhecimento reutilizáveis - índice e fatiamento
Métodos úteis: 
    append - Adicona um item no final da lista
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice 
    clear - limpa a lista
    extend - entende a lista
    + - concatena a lista

Create, Read, Update, Delete
Criar, Ler,   Alterar, Deletar = lista[i] CRUD
"""

lista = ["Henry José", 20, 1.82, [], 15, 898, "Apple"]

print(type(lista))
print(lista[2])
print(type(lista[2]))
print(lista[1])
print(type(lista[1]))

del lista[3] # apaga e reogarniza os itens da lista
del lista[-1] #deleta o último item da lista, caso vc não saiba o fim dela

lista.append("Gato") #adiciona no final da lista
lista.append("Lucky") #adiciona no final da lista
lista.append("Max") #adiciona no final da lista

lista.pop() #remove e retona o último item
lista.pop(15) #remove e retona o último item, pelo indice
armazena = lista.pop() #remove e retona o último item

lista_2 = ["Homem de Ferro", "Capitão América", "Hulk", "Thor", "Viuva Negra", "Gavião Arqueiro"]

lista_2.insert(4, "Visão") #insere pela posição escohida no primeiro parâmetro
lista_2.insert(2, "Homem Aranha") #insere pela posição escohida no primeiro parâmetro

print(lista)

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b # é possível juntar duas listas em uma só no python 
print(lista_c)
lista_a = lista_a.extend(lista_b) #estende a lista A com a lista B
