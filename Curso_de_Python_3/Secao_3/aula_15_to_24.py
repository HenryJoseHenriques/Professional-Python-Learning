#jogo de Pedra-Papel-Tesoura

import random

print("Vamos jogar Pedra, Papel e Tesoura\n")
usuario = input("Escolha entre 1-Pedra, 2-Papel e 3-Tesoura\n")
usuarioConvert = int(usuario)
computador = random.randint(1,3)

empate = (usuarioConvert == 1 and computador == 1) or (usuarioConvert == 2 and computador == 2) or (usuarioConvert == 3 and computador == 3)
VitoriaPC = (usuarioConvert == 1 and computador == 2) or (usuarioConvert == 2 and computador == 3) or (usuarioConvert == 3 and computador == 1)
VitoriaUsuario = (usuarioConvert == 2 and computador == 1) or (usuarioConvert == 3 and computador == 2) or (usuarioConvert == 1 and computador == 3)

print(f"Escolha do PC: {computador}")

if empate:
    print("Empate entre usuário e computador\n")
elif VitoriaPC:
    print("Vitória do PC.\n")
elif VitoriaUsuario:
    print("Vitória do usuário.\n")
else:
    print("Entrada inválida, reinicie o problema.\n")

#Adicone um brekpoint onde vc deseja para a depuração do código.