import os
from itertools import count

caminho = os.path.join('/home', 'guilherme','Documentos','Curso_Udemy_Python')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter,'pasta atual',root)

    for dir_ in dirs:
        print('  ', the_counter,'Dir:',dir_)
    
    for file_ in files:
        print('  ', the_counter,'File:',file_)