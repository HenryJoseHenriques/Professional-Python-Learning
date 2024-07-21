"""
Crie uma função que duplicam, triplicam e quadriplicam o número recebido como parametro
"""

#Abordagem tradicional

# def duplicar(num):
#     return num*2

# def triplicar(num):
#     return num*3

# def quadruplicar(num):
#     return num*4

#-----------------------

#Usando Closure

def multiplicar(qtd):
    def qualNum(num):
        return num*qtd
    
    return qualNum

dobro = multiplicar(2)
triplo = multiplicar(3)
quadruplo = multiplicar(4)

print(dobro(4))
print(triplo(4))
print(quadruplo(4))