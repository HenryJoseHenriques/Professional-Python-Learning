off = False

print("Calculadora")
while off != True:

    num1 = input("Digite o primeiro número:\n")
    num2 = input("Digite o segundo número:\n")
    opr = input("Escolha a operação:\n")

    num_valido = None
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        num_valido = True
    except:
        num_valido = None

    if num_valido is None:
        print("Um ou ambos números são inválidos.")
        continue

    opr_permitidos = "+-*/"

    if opr not in opr_permitidos or len(opr) > 1:
        print("Operador inválido")
        continue


    if opr == '+':
        r = num1_float + num2_float
    elif opr == '-':
        r = num1_float - num2_float
    elif opr == '*':
        r = num1_float * num2_float
    elif opr == '/':
        r = num1_float / num2_float
    else:
        print("ERRO")
    
    print(f"{num1}{opr}{num2} = {r}")

    sair = input("s para sair").lower().startswith('s')
    if sair is True:
        off = True