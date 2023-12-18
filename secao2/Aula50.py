# funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# toda funções  recursiva deve ter:
# - um problema que possa ser dividido em partes menores
# - um caso recursivo que resolve o pequeno probelma 
# - um caso bse que para a recursão
# - fatorial - n! = 5* 4 * 3 * 2 * 1 = 120

import sys

sys.setrecursionlimit(1004)

def recursiva(inicio = 0, fim =10):
    
    print(inicio,fim)
    
    #caso base
    if inicio >= fim:
        return fim
    
    #caso recursivo
    #contar até chegar ao final
    inicio += 1
    return recursiva(inicio,fim)

print(recursiva(0,1000))