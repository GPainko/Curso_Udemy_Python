# Calculadora com While

while True:
    
    numero_1 = input('digite um número:')
    numero_2 = input('digite um número:')
    operador = input('digite o operado(+,-,*,/):')

    numero_validos = None

    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numero_validos = True

    except :
        numero_validos =None
        print('error')

    if numero_validos is None:
        print('Um ou ambos os numeros digitados não são validos')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('operador invalido')
        continue

    if len(operador) > 1:
        print('digite apenas um operador')
        continue

    print('Realiazando sua conta. Confira o resultado abaixo:')

    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)
    else:
        print('Nunca deveria chegar aqui')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair is True:
        break
