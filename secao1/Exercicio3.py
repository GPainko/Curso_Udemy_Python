primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite um valor: ')

if primeiro_valor > segundo_valor:
    print(f'o primeiro_valor({primeiro_valor}) é maior que o segundo({segundo_valor})')
elif segundo_valor > primeiro_valor:
    print(f'o segundo_valor({segundo_valor}) é maior que o primeiro({primeiro_valor})')
else:
    print('os valores são iguais')