num = input("Digite um número inteiro:\n")


if num.isdigit():
    numInt = int(num)
    if numInt % 2 == 0:
        print(f"{numInt} é par.\n")
    else:
        print(f"{numInt} é ímpar.\n")
else:
    print(f"{num} não é um número inteiro.\n")