import sys

#generator expression, iterables e iterators em python

iterable = ['Eu', 'Tenho', '__iter__']

iterator = iter(iterable) 

generator = (n for n in range(100000))
lista = [n for n in range(100000)]
print(sys.getsizeof(generator))
print(sys.getsizeof(lista))

for n in generator:
    print(n)