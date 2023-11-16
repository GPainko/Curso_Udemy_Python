"""
Higher Order Functions
Funções de primeira classe
"""

def saudacao(msg):
    return msg


def executa(funcao, msg):
    return funcao(msg)


v = executa(saudacao,'bom dia')

print(v)