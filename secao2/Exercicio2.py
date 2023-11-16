#crie uma função que mostre se um numero é par ou impar
#retorne se o número é par ou ímpar

def par(numero):
    return numero % 2 == 0
    
numero = 10

decisao = par(numero)

if decisao is True:
    print(f'{numero} é par')
else:
    print(f'{numero} não é par')