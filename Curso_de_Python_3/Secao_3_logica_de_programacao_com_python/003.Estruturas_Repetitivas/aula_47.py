import os

palavraSecreta = "pamonha"
vezes = 0
letrasCertas = ''

while True:
    tentativa = input("Descobra a palavra secreta: ").lower()
    vezes += 1
    if len(tentativa) != 1: 
        print("Entrada inválida. Digite apenas uma letra")
        continue
        
    if tentativa in palavraSecreta:
        letrasCertas += tentativa

    palavraDica = ""
    for e in palavraSecreta:
        if e in letrasCertas:
            palavraDica += e
        else:
            palavraDica += "*"
    
    
    if palavraDica == palavraSecreta:
        os.system('cls')
        print(f"Meus parabéns, você acertou a palavra!\n A palavra era {palavraSecreta}. \n Tentativas: {vezes}")
        letrasCertas = ''
        palavraDica = ""
        
    print(palavraDica)

