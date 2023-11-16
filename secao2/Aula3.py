"""
VAlores padrão para parametro
ao definir uma função os parametros 
podem ter valores padrão. Caso o valor 
não seja enviado para o parametro
o valor parão será usado.
refatorar: editar o seu codigo.
"""

def soma(x,y, z = None):
    if z is not None:
        print(f'{x=} {y=} {z=}',x+y+z)
    else:
        print(f'{x=} {y=}',x+y)

soma(3,2,1)
soma(3,2)