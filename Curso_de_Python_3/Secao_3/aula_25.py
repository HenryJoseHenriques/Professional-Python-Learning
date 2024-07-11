#operador in e not in

palavra = "Onomatopeia"

if "peia" in palavra:
    print("OK")
else:
    print("NO")


palavra = input("Digite uma palavra que termina com 'ção'.\n")

if "ção" not in palavra:
    print("Essa palavra não possui 'ção'.\n")
else:
    print("Essa palavra possui ção.\n")

#Interpolação

# %s = string
# %.2f = float
# %d = inteiro
# %x = hexadecimal 

    nome = "Caio"
    preco = 1234.56789
    variavel = '%s, o preço é R$ %.2f' %(nome, preco)
    print(variavel)