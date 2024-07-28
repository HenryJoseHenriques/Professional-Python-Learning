"""
TIPO set -> conjuntos em python
São representados graficamente pelo diagrama de Venn
Sets em python são mutáveis, porém aceitam apenas tipos imútaveis como valores internos.
"""

#pode ser criado pela classe set() ou por meio de '{}'

diagram = set("Pedrinho")
diagram2 = {1,2,3}

print(diagram,type(diagram))
print(diagram2, type(diagram2))

"""
Sets são eficientes para remover valores duplicados de interáveis
- Seus valores serão sempre únicos
- Não aceitam valores mútaveis(listas, dicionários e sets)
- Não tem índexes
- Não garantem ordem
- São iteráveis (for, in, not in)
"""

diagram3 = {1,1,1,1,2,2,2,2,2,2,3,3,3,3,4,4,4,4}
print(diagram3)

"""Sets podem ser convertidos para outros tipos como listas e tuplas"""

lista = list(diagram3)
#lista = tuple(diagram3)

print(lista)

"""
Métodos úteis:
add, update, clear, discard
"""

diagram.add("João") #Adicona "João" ao conjunto
diagram.add("Kevin") #Adicona "João" ao conjunto
diagram.update("Alice") #Adciona de forma iterável
diagram.discard("Kevin") #Descarta o parâmetro
diagram.clear() #Limpa o set

"""
Operadores úteis:
união | união (union) - Une
intersecção & (intersection) - itens presentes em ambos
diferença - Itens presentes apenas no set da esquerda
diferença simétrica ^ - Itens que não estão em ambos
"""

s1 = {0,1,2,3}
s2 = {2,3,4,5,6}
s3 = s1 | s2 #União
s3 = s1 & s2 #Interseção
s3 = s1 - s2 #Diferença, retornará somente 0 e 1
s3 = s2 - s1 #Diferença, retornará somente 0 e 4,5 e 6
print(s3)