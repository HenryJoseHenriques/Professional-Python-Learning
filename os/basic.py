import os

#informações do sistema e variáveis do ambiente formato de dicionário
sistema = os.environ

print(sistema)

#verifica o diretório atual
caminho = os.getcwd()
    
print(caminho)

#Muda o diretório
os.chdir('C:\\Users\\BI0013\\Documents')

novo_caminho = os.getcwd()

print(novo_caminho)

#Cria uma nova pasta
os.mkdir("TesteOS")

#lista o diretório atual
print(os.listdir()) 

#cria ditórios consecutivos a partir do diretório atual
os.makedirs('pasta1/pasta2/pasta3', exist_ok=True) #caso o  diretório já exista

## Trabalhando com arquivos

#Abre o arquivo
os.startfile('Engenharia de Software.txt')

#Renomeia
os.rename('Engenharia de Software.txt','Software Engineer.txt')

#Remove
os.remove('Software Engineer.txt')

## Caminhos


#O método os.path.commonpath() retorna o caminho comum mais longo a partir de uma lista de caminhos fornecidos.
caminhos = [r"C:\Users\BI0013\Documents\My Web Sites\WebSite1",r"C:\Users\BI0013\Documents\MinecraftSG"] #vetor de caminhos
comum = os.path.commonpath(caminhos)
print(comum)

#O método os.path.dirname() retorna o diretório pai de um caminho.
caminho1 = r"C:\Users\BI0013\Pictures\Screenshots\Captura de tela 2024-09-16 161357.png"
diretorio = os.path.dirname(caminho1)
print(diretorio)

#O método os.path.basename() retorna a última parte (arquivo ou diretório) de um caminho.
arquivo = os.path.basename(caminho1)
print(arquivo)

#O método é semelhante ao os.path.commonpath(), mas ele retorna o prefixo comum mais longo baseado em simples comparação de caracteres (não necessariamente caminhos válidos). 
arquivo = os.path.commonpath(caminho1)
print(arquivo)

