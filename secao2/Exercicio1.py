"""
Exercicio com funções 

Crie uma função que multiplica todos os argumentos
não nomeados recebidos
retorne o total para uma variavel e mostre o valor
da variavel
"""

def multi(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

vartotal = multi(1,2,3,4,5,6,7,8,9)
print(vartotal)