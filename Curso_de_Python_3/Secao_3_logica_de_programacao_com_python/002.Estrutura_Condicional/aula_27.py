"""
Fatiamento de Strings
 012345678
 Olá mundo
-987654321

Fatiamento [i:f:p] [::]
p = passo, de quanto em quanto ele vai pular
OBS.: a função len retorna a quantidade de caracteres de um str.

"""

var = 'Olá mundo'
print(var[4:])
print(var[:6])
print(var[:2]) #pula de dois em dois
print(var[:-1]) #inverte
print(len(var))