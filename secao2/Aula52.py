#Criando arquivos em pyhton

caminho_arquivo = '/home/guilherme/Documentos/Curso_Udemy_Python/secao2/'
caminho_arquivo += 'Aula52.txt'

with open(caminho_arquivo,'w+') as arquivo:
    arquivo.write('linha 1\n')
    arquivo.write('linha 2\n')
    arquivo.writelines(
        ('linha 3\n','linha 4\n')
        )
    arquivo.seek(0,0)
    print(arquivo.readline(),end ='')
    print(arquivo.readline().strip())
    print(arquivo.readline())
    print('ReadLines')
    arquivo.seek(0,0)
    for linha in arquivo.readlines():
        print(linha.strip())


print('-'*30)
with open(caminho_arquivo,'r') as arquivo:
    print(arquivo.read())
