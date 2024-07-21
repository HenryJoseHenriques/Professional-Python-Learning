"""
Closure e funçoes que retornam outras funções
"""

def criar_saudacao(saudacao):
    def saudar(nome): 
        return f'{saudacao}, {nome}!'
    return saudar #retorna a função saudar

#Em python, é possível usar funções como um tipo de template para criar outras funções mais especifícas
falar_bom_dia = criar_saudacao('Bom dia') #Cria-se uma variável exclusiva para uso em 'bom dia'
falar_boa_noite = criar_saudacao('Boa noite')

for nomes in ['João','Pedro','Matheus']:
    print(falar_bom_dia(nomes)) #No parametros, colocamos uma variável que faz lembrar de saudar
    print(falar_boa_noite(nomes))