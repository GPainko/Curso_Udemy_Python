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

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_c)
print(lista_a)

