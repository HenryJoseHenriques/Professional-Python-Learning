username = input("Escreva seu nome:\n")
idade = input("Escreva sua idade:\n")

if username and idade:
    print(username)
    print(username[::-1])
    if ' ' in username:
        print("Sim")
    else:
        print("Não")
    print(f"Seu nome contém {len(username)}")
    print(f"A primeira letra do seu nome é {username[0]}")
    print(f"A última letra do seu nome é {username[-1]}")
else:
    print("Desculpe, você deixou campos vazios")