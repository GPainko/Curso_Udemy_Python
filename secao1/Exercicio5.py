"""
Faça um programa qye peça ao usuário para digitar um número inteiro,
informe se este numero é par ou impar. caso usuario não digite um número
inteiro,informe que não é um número inteiro.
"""

numero = input("Digite um número inteiro: ")

if numero.isdigit():
    num_inteiro = int(numero)
    if (num_inteiro % 2 == 0):
        print('o número é par')
    else:
        print('o numero é impar')
else:
    print('voce nao digitou um numero inteiro')
