"""
Exercio
exiba os indices da lista 
"""

lista = ["Maria","Helena","Luiz"]

'''
indices = ranger(len(lista))

for incice in indices
    print(indice,lista[indice])
'''
indice = 0

lista.append("gui")

for nome in lista:
    print(indice, '-',nome)
    indice += 1
