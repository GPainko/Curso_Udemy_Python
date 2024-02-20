import os

caminho = os.path.join('/home/Documentos','Curso_Udemy_Python','Aula4.py')
print(caminho)
diretorio,arquivo = os.path.split(caminho)
nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print(arquivo)
print(extensao_arquivo)
print(os.path.exists('/home/guilherme/Documentos/Curso_Udemy_Python'))
print(os.path.basename(caminho))
print(os.path.basename(diretorio))
print(os.path.dirname(diretorio))