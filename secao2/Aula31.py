#yield from

def gen1():
    print("Começou gen 1")
    yield 1
    yield 2
    yield 3
    print("acabou gen 1")

def gen2(gen = None):
    
    print("Começou gen 2")
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print("acabou gen 2")

def gen3():
    print("Começou gen 3")
    yield 7
    yield 8
    yield 9
    print("acabou gen 3")



g = gen2(gen1())
g1 = gen2(gen3())
g2 = gen2()

for numero in g:
    print(numero)

for numero in g1:
    print(numero)

for numero in g2:
    print(numero)