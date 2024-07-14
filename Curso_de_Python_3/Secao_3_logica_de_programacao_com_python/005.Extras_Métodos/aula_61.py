"""
https://www.macoratti.net/alg_cpf.htm
Algoritmo de validação do CPF

Gerador de CPF: https://www.4devs.com.br/gerador_de_cpf

CPF Falso: 385.950.870-91
"""

"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

#cpf = "385.950.870-91"
#cpf = "012.843.220-92"
#cpf = "269.230.420-97"
#cpf = "111.111.111-11"

import sys
import random

cpf = ''

for i in range(11):
    cpf += str(random.randint(0,9))

cpf_num = cpf.replace(".","").replace("-","").replace(" ","") #o método replace subtitui partes específicas de uma string por outra replace(<parte que deseja remover>, <parte que deseja substituir>)
entradaSequencial = cpf_num[0]*len(cpf_num) == cpf_num 
if entradaSequencial:
    print("Entrada inválida")
    sys.exit()
digitos = [] #Lista para armazena os 9 primeiros digitos
c = 0 #contador para breakar o código para a lista não armazer os dois últimos digitos
for i in cpf_num: # itenera o cpf_num e armazena na lista digitos
    if c >= 9:
        break  #quebra o for quando os primeiros 9 digitos forem armazenados
    c +=1
    digitos.append(int(i)) #armazena o i(caractete do cpf_num armazenado em i) e faz o casting para int 

digitosMulPrimeiro = [] #digitos múltiplicados por valores de uma contagem de regressiva de 10
indicePrimeiro = 0 #indicePrimeiro dos digitos
for j in range(10,1,-1): #faz uma contagem regressiva de 10 a 1
    digitosMulPrimeiro.append(digitos[indicePrimeiro]*j) #multiplica o valor contido na lista de digitos por j, que é o valor da contagem de 10 a 1
    indicePrimeiro += 1 #atualiza o indicePrimeiro

sumDigitosPrimeiro = 0 #armazena a soma dos indicePrimeiros
for k in digitosMulPrimeiro: #O k percorre e armazena o valores da lista
    sumDigitosPrimeiro += k #E soma em sumDigitosPrimeiro

sumDigitosPrimeiro = (sumDigitosPrimeiro * 10) % 11 #multiplica o resultado alterior por 10

primeiroDigito = 0 if sumDigitosPrimeiro > 9 else sumDigitosPrimeiro #Verifica se o sumDigitosPrimeiro é maior que 9, caso sim, ele troca por 0

verificaPrimeiroDigito = int(cpf[-2])
if primeiroDigito == verificaPrimeiroDigito:
    print(f"O primeiro digito do CPF: {cpf} é valido")
else:
    print(f"O primeiro digito do CPF: {cpf} não é valido")

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""

digitos.append(primeiroDigito)
digitosMulSegundo = []
indiceSugundo = 0

for j in range(11,1,-1):
    digitosMulSegundo.append(digitos[indiceSugundo]*j)
    indiceSugundo +=1
segundoDigito = 0

for k in digitosMulSegundo:
    segundoDigito += k

segundoDigito = (segundoDigito * 10) % 11
segundoDigito = 0 if segundoDigito > 9 else segundoDigito

verificaSegundoDigito = int(cpf[-1])

if segundoDigito == verificaSegundoDigito:
    print(f"O segundo digito do CPF: {cpf} é valido")
else:
    print(f"O segundo digito do CPF: {cpf} não é valido") 
CPF_valido = primeiroDigito == verificaPrimeiroDigito and segundoDigito == verificaSegundoDigito

if CPF_valido:
    print(f"O CPF: {cpf} é válido!")
else:
    print(f"O CPF: {cpf} NÃO é válido!")