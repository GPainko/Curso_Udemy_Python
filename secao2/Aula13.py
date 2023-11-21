p1 = {
    'nome' : 'Luiz',
    'sobrenome' : 'Miranda',
}

nome = p1.popitem()
#nome = p1.pop()

p1.update({
    'nome': 'novo valor',
    'idade': 30,
})
#p1.update(nome='novo valor,idade = 30)

tupla = ('nome','novo valor'),('idade',30)
lista = ['nome','novo valor'],['idade',40]
p1.update(tupla)
p1.update(lista)

print(p1.get('nome','não existe'))
print(p1)