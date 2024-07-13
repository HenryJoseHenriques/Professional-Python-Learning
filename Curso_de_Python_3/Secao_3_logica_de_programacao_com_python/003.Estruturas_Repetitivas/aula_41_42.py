#while / else <- bizarro

#Algotirmo de Contagem

frase = "Qual foi a letra que apareceu mais vezes nessa frase?"

i = 0
quantidadeMaisVezes =  0
letraQueMaisSeRepete = ''

while i < len(frase):
    letraAtual= frase[i]

    if letraAtual == ' ':
        i += 1
        continue

    quantidadeAtual = frase.count(letraAtual)

    if quantidadeMaisVezes < quantidadeAtual:
        quantidadeMaisVezes = quantidadeAtual
        letraQueMaisSeRepete = letraAtual
    
    i +=1

print(f"A letra que mais se repete é '{letraQueMaisSeRepete}', que apareceu {quantidadeMaisVezes}x vezes")
