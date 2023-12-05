#Combinations, Permutations e Product - Itertools
#Combinação - Ordem não importa - iteravel + tamaho do grupo
#Permutação - Ordem importa
#Produto - Ordem importa e repete valores únicos

from itertools import combinations,permutations,product

def print_iter(iterator):
    print(*list(iterator),sep='\n')
    print()

pessoas = [
    'João','Joana','Luiz','Letícia',
]
camisetas = [
    ['preta','branca'],
    ['p','m','g'],
    ['masculino','feminino','Unisex'],
    ['algodão','poliester',],
]
#print('Combinação')
#print_iter(combinations(pessoas,2))
#print('Permutação')
#print_iter(permutations(pessoas,2))
print_iter(product(*camisetas))


