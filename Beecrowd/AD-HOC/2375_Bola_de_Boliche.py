PI = 3.14
while True:
    diametro_bola = input()
    diametro_bola_int = int(diametro_bola)
    if diametro_bola_int < 1 or diametro_bola_int > 10000:
        continue
    A,L,P = map(int,input().split())
    if A  < 1 or A > 10000:
        continue
    if L  < 1 or L > 10000:
        continue
    if P  < 1 or P > 10000:
        continue

    if (diametro_bola_int > A) or (diametro_bola_int > L ) or (diametro_bola_int > P):
        print("N")
    else:
        print("S")

