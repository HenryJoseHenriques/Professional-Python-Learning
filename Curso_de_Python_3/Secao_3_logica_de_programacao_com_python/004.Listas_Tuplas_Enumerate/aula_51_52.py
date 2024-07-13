#Introdução ao desempacotamento + tuples(tuplas)

#Alunos = ["Joao", "Pedro", "Gabriel"]

#estudante1,estudante2,estudante3 = Alunos
estudante1,estudante2,estudante3 = ["Joao", "Pedro", "Gabriel"]
#estudante1,estudante2,estudante3 = ["Joao", "Pedro"] # dá erro
#estudante1,estudante2 = ["Joao", "Pedro", "Gabriel"] # dá erro também

# print(estudante2)
# print(estudante1)
# print(estudante3)

#Dempacotamento

_, _, alum1, *_ = ["Joao", "Pedro", "Gabriel"]
# _ = conversão entre devs para dizer que essa variável não será usada
print(alum1)
print(_)
print(type(_)) #lista

""" Tipo Tupla - uma lista IMUTÁVEL"""

trabalhadores = "Eletricista", "Engenheiro", "Médico" #não tem '[]'
#trabalhadores[2] = "Mecânico" <- Isso não funciona
print(trabalhadores)
print(type(trabalhadores)) #tupla