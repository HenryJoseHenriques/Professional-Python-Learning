"""
for + range
range -> range(start, stop, step)

"""

# palavra = 'onomatopeia'

# for letra in palavra:
#     print(letra)


numeros = range(0,10,2) #começa do 0, vai até o 9, e pula de 2 em dois

for numero in numeros:
    print(numero)

print("\n")

numeros = range(0,100,5) 

for numero in numeros:
    print(numero)

print("\n")

numeros = range(0,100,7)

for numero in numeros:
    print(numero)

print("\n")

numNegativos = range (0,-10,-2) #também funciona com números negativos

for numero in numNegativos:
    print(numero)