#valores truthy e falsy, tipos Mutaveis e umutaveis
#mutaveis []{} set()
#Imutáveis 9 "" 0 0.0 None False range(0,10)

lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy(valor):
    return 'falsey' if not valor else 'truthy'

print(f'TESTE', falsy('Teste'))
print(f'{lista=}',falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{conjunto=}', falsy(conjunto))
print(f'{inteiro=}', falsy(inteiro))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nada=}', falsy(nada))
print(f'{falso=}', falsy(falso))
print(f'{intervalo=}', falsy(intervalo))
