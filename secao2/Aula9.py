# dicionario

pessoa = {
    'nome':'luiz otavio',
    'sobrenome':'miranda',
    'idade':18,
    'altura':1.8,
    'endereços':[
        {'rua':'taltal','numero':123},
        {'rua':'taltal','numero':123}
    ]
}

#pessoa = disct(nome='luiz otavio')

#print(pessoa,type(pessoa))

print(pessoa['nome'])

for chave in pessoa:
    print(chave , pessoa[chave])