# super() é a super classe na sub classe
# classe principal (Pessoa)
#  -> super class, base class, parent class
# classes filhas( cliente)
#  -> sub class, child class, derived class

# class MinhaString(str):
#     def upper(self):
#         print('Chamou UPPER')
#         retorno =  super().upper()
#         print( 'Depois do UPPER')
#         return retorno


# string = MinhaString('Luiz')
# print(string.upper())

class A:

    atributo_a = 'valor a'

    def metodo(self):
        print('A')


class B(A):

    atributo_b = 'valor b'

    def metodo(self):
        super().metodo()
        print('B')


class C(B):

    atributo_c = 'valor c'

    def metodo(self):
        super().metodo()
        print('C')
        super(B,self).metodo()


c = C()
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()