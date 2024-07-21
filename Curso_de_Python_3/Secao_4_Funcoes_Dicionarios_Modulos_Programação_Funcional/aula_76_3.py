"Continuação da anterior"

fichaTecnica = {
    'nome': 'Henry',
    'sobrenome': 'José',
    'Idade' : 20,
    'l1': [0,1,2] # O método copy ainda apontaria para o endereço de memória de l1
}

#novaFicha = fichaTecnica #Apontam para o mesmo endereço, se alterar um, altera o outro
novaFicha = fichaTecnica.copy() #Cria uma cópia, apontando para um endereço diferente porém, é uma Shallow copy
#Pois não copia valores mútaveis, apenas imutáveis

# para resolver esse problema, importe o dicionário 'copy' e uso o método deepcopy(<dicionário que deseja copiar>)    

novaFicha['l1'][0] = 9999

print(fichaTecnica)
print(novaFicha)

fichaTecnica.pop('l1')

fichaTecnica.update({ #Atualiza um dicionário, é possível modificar chaves antigas e adicionar novas
    'nome': 'Marcelo',
    'altura': '2.0',
})

#Outro jeito

fichaTecnica.update(nome= 'Fabio', altura= 1.80)

#Também é possível fazer com tuplas, mas não parece muito prático