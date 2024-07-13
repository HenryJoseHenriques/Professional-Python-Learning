"""
Iterável -> str, range, ect
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador


# for por baixo dos panos:

"""
# for letra in palavra
palavra = "Henry José" # iterável
iteratador = iter(palavra) # iterator

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break

"""
for funciona com continue, break e else da mesma maneira que o while
"""