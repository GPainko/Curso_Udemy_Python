"""
Argumento nomeados e não nomeados em funções Python
Argumentos nomeados tem nome com sinal igual
Argumentos não nomeados recebe apenas o argumento(valor)
"""

def soma(x,y):
    #definição
    print(f'{x=} y={y}','|',x + y)


soma(y=2,x=3)