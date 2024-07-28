#Exercício - Sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quem descobriu o Brasil',
        'Opções': ['Pedro Álvares Cabral','Dom João VI','Américo Vespôcio','Zumbi dos Palmares'],
        'Resposta': 'Pedro Álvares Cabral' 
    },
    {
        'Pergunta': 'Qual o maior país do mundo?',
        'Opções': ['Rússia', 'China', 'Estados Unidos da América', 'Canadá'],
        'Resposta': 'China'
    },
    {
        'Pergunta': 'Quantos continentes há no mundo?',
        'Opções': ['6','4','5','7'],
        'Resposta': '5' 
    }
]

def jogoDePerguntas():
    i = 0
    acertos = 0
    qtdPerguntas = len(perguntas)
    while i < qtdPerguntas:
        for chave in perguntas[i].keys():
            chave_pergunta = chave
            valor_pergunta = perguntas[i][chave] 
            if chave_pergunta == 'Opções': 
                print(f"{chave_pergunta}:\n")
                n = 0
                for j in valor_pergunta: 
                    print(f'{n}) {j}')
                    n = n + 1 

            elif chave_pergunta == 'Resposta':
                r = input(f"{chave_pergunta}:")
                if r.isdigit():
                    r_int = int(r)
                    intevalo_valido = r_int >= 0 and r_int < qtdPerguntas
                else:
                    print("Entrada inválida. Tente novamente")
                    continue
                
                if r_int is not None:
                    if intevalo_valido:
                        if perguntas[i]['Opções'][r_int] == valor_pergunta:
                            print("Você acertou! Parabéns!")
                            acertos = acertos + 1
                            i = i + 1
                        else:
                            print("Reposta errada. Tente novamente")
                            continue
                    else:
                        print("Você digitou um valor fora do intervalo de alternativas. Tente novamente")
                        continue
            
            else:    
                print(f'{chave_pergunta}: {valor_pergunta}\n')

    print(f'Obrigado por jogar\n Você acertou {acertos} perguntas')

jogoDePerguntas()