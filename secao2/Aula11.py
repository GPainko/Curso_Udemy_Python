pessoa = {
    'nome': 'luiz otavio',
    'sobrenome' : 'Miranda',
    #'idade' : 900,
}

pessoa.setdefault('idade',18)

print(len(pessoa))

print(tuple(pessoa.keys()))

for chave in pessoa.keys():
    print(chave)

print(list(pessoa.values()))

for valor in pessoa.values():
    print(valor)

print(list(pessoa.items()))

for chave,valor in pessoa.items():
    print(chave, valor)


