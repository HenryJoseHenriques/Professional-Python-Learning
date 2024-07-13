"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

num = input()
try:
    num = float(num)
    print(f"O dobro de {num} é {num*2}")
except:
    print(f"Isso não é um número.")