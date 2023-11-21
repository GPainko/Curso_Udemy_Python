#manipulando chaves e valores em dicionarios

pessoa = {}

chave = 'nome'

pessoa[chave] = 'luiz otavio'
pessoa['sobrenome'] = 'miranda'

del pessoa['sobrenome']
print(pessoa)
print(pessoa[chave])

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])