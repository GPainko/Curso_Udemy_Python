"""
Metodos Úteis:
    append -> adiciona uma item ao final
    insert -> adiciona um item no indice escolhido
    pop -> Remove do final ou do indice escolhido
    del -> apaga um indice
    clear -> limpa a lista
    extend -> estende a lista
    + -> concatena a lista
"""

lista = [0,1,2,3,4,5,6,7,8,9]
lista.append(10)
ultimo_numero = lista.pop()
lista.append(11)
del lista[-1]
print(lista, ultimo_numero)
lista.insert(0,-1)
#lista.clear()
print(lista)
