#Empacotamento e desempacotamento de dicionarios

a,b = 1,2
a,b = b,a
print(a,b)

pessoa = {
    'nome':'Aline',
    'sobrenome':'Souza'
}

a,b = pessoa.values()
print(a,b)

(a1,a2),(b1,b2) = pessoa.items()
print(a1,a2)
print(b1,b2)

for chave,valor in pessoa.items():
    print(valor)


dados_pessoa = {
    'idade': 16,
    'altura' : 1.5,
}

pessoa_completa = {**pessoa, **dados_pessoa}

print(pessoa_completa)
