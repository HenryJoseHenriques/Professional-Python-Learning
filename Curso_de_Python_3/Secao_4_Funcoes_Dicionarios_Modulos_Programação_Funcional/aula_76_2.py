"""
Métodos úteis dos dicionários em Python
len -  quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave especifica (del)
popitem - o último item adicionado
update - Atualiza um dicionário com o outro
"""

pessoa = {
    'nome': 'Pedro',
    'sobrenome': 'Silva'
}

pessoa.setdefault('idade', None) #Caso a chave exista, isso é ignorado

print(len(pessoa))
print(list(pessoa.keys())) #dá para jogar em um for -> for chaves in pessoa.keys()
print(list(pessoa.values())) #mesma coisa do de cima
print(list(pessoa.items())) #mesma coisa do de cima 

