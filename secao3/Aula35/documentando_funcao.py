""" titulos

    descrição da documentação
"""

variavel_1 = 1

#def soma(x,y):

def soma(x:int|float, y:int|float)-> int|float:
    """
    soma x e y

    este modulo contem a função exemplos de documentção de função
    a função soma voce ja conhece bastante.

    :param x: Número 1
    :type x: int or float
    :param y: Número 2
    :type y: int or float

    :return: A soma entre x e y
    :rtype: int or float
    """
    return x + y

def multiplicar(
        x: int|float,
        y: int|float,
        z: int|float |None = None
)-> int|float:
    """
    Multiplica x,y,z

    multiplica x e y. Se z for enviado,multiplica x,y,z
    """
    if z is None:
        return x * y
    return x * y * z

variavel_2 = 2
variavel_3 = 3
variavel_4 = 4