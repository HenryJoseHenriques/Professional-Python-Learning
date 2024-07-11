"""
operadores de atribuição:

= += -= *= /= //= **= %=

No python, todos os operadores podem ser combinados com o sinal de =
"""
#continue = pula parte do código e volta para o ínicio do while em que ele estava

contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print("Não vou mostar o seis")
        continue #esse comando faz o código voltar ao ínicio, ignorando os códigos restantes.
    if contador == 12:
        print("Não vou mostar o doze")
        continue #esse comando faz o código voltar ao ínicio, ignorando os códigos restantes.
    if contador == 18:
        print("Não vou mostar o dezoito")
        continue #esse comando faz o código voltar ao ínicio, ignorando os códigos restantes.

    print(contador)