"""
split e join com lista e str
split - divide uma string
join - une uma string 

strip -> strip(), lstrip(), rstrip() #corta os espaços
"""

frase = "          Quem não tem cão, caça com gato         "
lista_frase = frase.split(',') #divive um astring conforme um parâmetro, se estiver vazia, é o espaço
lista_frase_corrida = []

for i, frase in enumerate(lista_frase):
    lista_frase_corrida.append(lista_frase[i].strip())

print(lista_frase)
print(lista_frase_corrida)

frases_unidas = '***'.join(lista_frase_corrida)
print(frases_unidas)