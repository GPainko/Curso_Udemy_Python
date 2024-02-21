from pathlib import Path
from shutil import rmtree

caminho_projeto = Path()

print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
print(caminho_arquivo)

print(caminho_arquivo.parent)

ideias = caminho_arquivo.parent /'ideias'
print(ideias / 'trabalho.txt')

print(Path.home())

arquivo = caminho_arquivo.parent /'Aula23.txt'
arquivo.touch()
print(arquivo)
arquivo.write_text('Olá Mundo\n')
print(arquivo.read_text())
# arquivo.unlink() - apaga arquivo

with arquivo.open('a+')as file:
    file.write('Ola\n')
    file.write('Corre\n')

caminho_pasta = caminho_arquivo.parent /'Aula23'
caminho_pasta.mkdir(exist_ok=True)
sub_pasta = caminho_pasta /'sub_pasta'
sub_pasta.mkdir(exist_ok=True)
outra_pasta = sub_pasta/'outra_pasta'
outra_pasta.mkdir(exist_ok=True)

outro_arquivo = outra_pasta/'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Hey')

outro_arquivo = sub_pasta/'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Hey')

#caminho_pasta.rmdir()
files = caminho_pasta/'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files/ f'file_{i}.txt'
    file.touch()

    if file.exists():
        file.unlink
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write('Ola mundo\n')
        text_file.write(f'file_{i}.txt')

def rmtree(root,remove_root=True):
    for file in root.glob("*"):
        if file.is_dir():
            print('Dir:', file )
            rmtree(file,False)
            file.rmdir()
        else:
            print('file:', file )
            file.unlink()

    if remove_root:
        root.rmdir()

rmtree(caminho_pasta)    
            
