
def Multi(*args):
    acum = 1
    for i in args:
        acum *=i
    return acum

def ParImpar(x):
    if x % 2 == 0:
        return "É par."
    else:
        return "É ímpar."

res = Multi(3,3,3)

print(res)

y = int(input("Digite um número: \n"))

print(f"{y} é {ParImpar(y)}")    

