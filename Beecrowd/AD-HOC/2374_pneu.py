#https://judge.beecrowd.com/pt/problems/view/2374

while True:
    pressaoDesejada = input()
    pressaoDesejada_int = int(pressaoDesejada)
    if pressaoDesejada_int <= 0 or pressaoDesejada_int >= 40:
        continue

    pressao_lida = input()
    pressao_lida_int = int(pressao_lida)
    if  pressao_lida_int <= 0 or pressao_lida_int >= 40:
        continue

    dif_pressao = pressaoDesejada_int - pressao_lida_int
    print(dif_pressao)