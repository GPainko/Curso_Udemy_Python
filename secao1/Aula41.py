"""
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update Delete
Criar , ler, alterar, apagar - lista[i](CRUD)
"""

lista = [1,2,3,4]
numero = lista[2]
print(numero)
lista[2] = 300
print(lista)
del lista[2]
print(lista)
lista.append(50)
print(lista)
ultim_valor = lista.pop(3)
print(lista, 'Removido,' , ultim_valor)