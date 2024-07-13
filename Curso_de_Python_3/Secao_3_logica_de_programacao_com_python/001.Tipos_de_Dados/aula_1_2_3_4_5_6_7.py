#Tipo de dados

texto = "Isso é um texto de string"

print(f"{texto}\n")

numInteiro = 7

print(f"{numInteiro}\n")

numFrancionado = 3.141592653

print(f"{numFrancionado}\n")

dadoBolean = 7 >= 8

print (f"{dadoBolean}\n")

#casting


boolToInt = int(True)
fraToInt = int(numFrancionado)
strToBolean = bool("")
floatToBolean = bool(1.5885614)

print(f"{boolToInt}\n")
print(f"{fraToInt}\n")
print(f"{strToBolean}\n")
print(f"{floatToBolean}\n")

#método type

print(f"{type(boolToInt)}\n")
print(f"{type(fraToInt)}\n")
print(f"{type(strToBolean)}\n")
print(f"{type(floatToBolean)}\n")