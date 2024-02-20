import os

caminho = os.path.join('/home', 'guilherme','Documentos','Curso_Udemy_Python')

for pasta in os.listdir(caminho):
    caminho_completo = os.path.join(caminho,pasta)
    if not os.path.isdir(caminho_completo):
        continue
    for item in os.listdir(caminho_completo):
        print(item)
