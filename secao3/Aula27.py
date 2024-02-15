class A:
    def __new__(cls):
        print('Antes de terminar a instancia')
        instancia = super().__new__(cls)
        print('Depois')
        instancia.x = 123
        return instancia

    def __init__(self):
        print('Sou o init')

    def __reper__(self):
        return 'A()'
    

a = A()
#a = object.__new__(A)
#a.__init__()
print(a.x)