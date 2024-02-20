from collections import namedtuple

Carta = namedtuple(
    'carta',['valor','naipe'],
    defaults=['VALOR','NAIPE']
    )
as_espadas = Carta('A','Espadas')
print(as_espadas)
#print(as_espadas[0])
print(as_espadas.naipe)
print(as_espadas.valor)
#print(as_espadas[1])

print()
print(as_espadas._fields)
print(as_espadas._field_defaults)
print()

for valor in as_espadas:
    print(valor)

print(as_espadas._asdict())