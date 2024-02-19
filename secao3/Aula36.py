import enum

#Direcoes = enum.Enum('Direcoes',['ESQUERDA','DIREITA'])

class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    CIMA = enum.auto()
    BAIXO = enum.auto()

print(Direcoes(1),Direcoes['ESQUERDA'],Direcoes.ESQUERDA)

def mover(direcao: Direcoes):
    if not isinstance(direcao,Direcoes):
        raise ValueError('Direção não encontrada')
    
    print(f'Movendo para {direcao.name} ({direcao.value})')


mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.CIMA)
mover(Direcoes.BAIXO)
#mover('lado')