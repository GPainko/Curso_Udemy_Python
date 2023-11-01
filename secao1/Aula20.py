# Operadores in e not in
# Strings são iteáveis
# 0 1 2 3 4 5 
# O t á v i o
#-6-5-4-3-2-1

nome = 'Otávio'
print(nome[2])
print(nome[-2])
print(10 * '-')

print('á' in nome)
print('b' in nome)
print(10 * '-')

print('á' not in nome)
print('b' not in nome)
print(10 * '-')

nome = input('digite seu nome:')
encontrar = input('digite o que quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')


