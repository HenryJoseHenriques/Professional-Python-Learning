# Enumerate - enumera itéraveis (índices)

vingadores = ["Homem de Ferro", "Capitão América", "Hulk", "Thor", "Viuva Negra", "Gavião Arqueiro"]

vingadores_enumerate = enumerate(vingadores)

print(vingadores_enumerate)
print(type(vingadores_enumerate)) #enumerate

for item in vingadores_enumerate: # Consome os valores a cada interação, até esvaziar a lista
    print(item) #Exibe o indice e o elemento

for indice, conteudo in vingadores_enumerate: # Consome os valores a cada interação, até esvaziar a lista
    print(indice, conteudo) #Exibe o indice e o elemento, separado por variaveis

#casting
print(list(vingadores_enumerate))
print(tuple(vingadores_enumerate))