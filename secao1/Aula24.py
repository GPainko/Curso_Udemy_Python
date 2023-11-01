"""
Introdução ao try/except
Try-> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('vou dobrar o numero que voce digitar: ')

try:
    numero_float = float(numero_str)
    print(f' O dobro de {numero_str} é {numero_float * 2}')
except:
    print('Isso não é um numero')