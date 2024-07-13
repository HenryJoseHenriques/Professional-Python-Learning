"""
Cuidado com tipos mutáveis

= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""

#Aponta para o mesmo endereço de memória
lista_a = ["A", 25, True]
lista_b = lista_a
print(id(lista_a))
print(id(lista_b))

print("\n")

# Faz uma copia(endereços de memória diferentes)
lista_c = ["B", 26, False]
lista_d = lista_c.copy()
print(id(lista_c))
print(id(lista_d))