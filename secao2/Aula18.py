#função lambda em python

lista = [
    {'nome':'luiz','sobrenome':'miranda'},
    {'nome':'maria','sobrenome':'silva'},
    {'nome':'miros','sobrenome':'vals'},
    {'nome':'antonio','sobrenome':'zeliskis'},
]

def exibir (lista):
    for item in lista:
        print(item)
    print()

lista.sort(key=lambda item: item['nome'])

l1 = sorted(lista,key=lambda item: item['sobrenome'])

exibir(lista)
exibir(l1)