"""
Introdução ao tipo dicionário
Dicionários são estruturas de dados do tipo par de 'chave' e 'valor'

Chaves podem ser consideradas como indices que são nomeados e podem assumit tipos imutáveis
como: str, int, float, bool, tuple, etc

O valor pode ser de qualquer tipo, incluindo outro dicionário

Usamos as chaves '{}' ou a classe dict para criar dicionários

Imutáveis: str, int float, bool, tuple
Mutável: dict, list
"""

pessoa = {
    #Chave  Valor
    'nome': 'Henry',
    'sobrenome': 'José',
    'idade': 20,
    'altura': 1.83,
    'endereco': [
        {'rua':'tal tal', 'numero': 123},
        {'OutraRua':'Tal tal', 'numero': 456}
    ]
}

# print(type(pessoa))

# for chave in pessoa:
#     print(chave, pessoa[chave])

#é possível criar novas chave dentro de um dicionario

ficha = {}

    #Chave      Valor
ficha['Carro'] = 'Gol'
ficha['Marca'] = 'Volks'

print(ficha['Carro'])

del ficha['Carro'] #Deleta a chave

#get retorna None por padrão caso a chave não exista, mas é possível adicionar um segundo parâmetro definindo o que será retornado
if ficha.get('sobrenome') is None:
    print("Não existe")
else:
    print(pessoa['sobrenome'])