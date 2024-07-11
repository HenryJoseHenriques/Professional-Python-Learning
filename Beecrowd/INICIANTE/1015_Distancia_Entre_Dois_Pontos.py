#https://judge.beecrowd.com/pt/problems/view/1015

import math

x1,y1 = map(float,input().split())
x2,y2 = map(float,input().split())

distancia = math.sqrt((x1-x2)**2+(y1-y2)**2)
print(f"{distancia:.4f}")