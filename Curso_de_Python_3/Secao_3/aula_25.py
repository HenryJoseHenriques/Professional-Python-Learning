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