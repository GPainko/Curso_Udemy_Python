#recarregando modulos
import importlib

import Aula37_m

print(Aula37_m.variavel)

for i in range(10):
    importlib.reload(Aula37_m)
    print(i)

print('fim')