#lista  comprehension em python

lista = []

for numero in range(10):
    lista.append(numero)

print(lista)

lista = [numero for numero in range(10)]
print(lista)