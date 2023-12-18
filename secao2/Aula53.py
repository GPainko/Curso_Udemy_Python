import os

caminho_arquivo = '/home/guilherme/Documentos/Curso_Udemy_Python/secao2/'
caminho_arquivo += 'Aula53.txt'

with open(caminho_arquivo,'w') as arquivo:
    arquivo.write('atenção\n')
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n')

#remover arquivo
#os.remove(caminho_arquivo)
#os.remove(caminho_arquivo)
    
#renomear ou mover arquivo
#os.rename(caminho_arquivo,'arquivotextoaula53.txt')