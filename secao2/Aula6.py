"""
args - Argumentos não nomeados
* - * args(empacotamento e desempacotamento)
"""

#lembre-te de desempacotamento
x,y, *resto = 1,2,3,4

print(x,y,resto)
print('-' * 30)

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma = soma(1,2,3,4,5,6)
print(soma)

print(sum((1,2,3,4,5,6,7)))