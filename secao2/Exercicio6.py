from Modulo import produtos
# copy, sorted, produtos.sort
import copy
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

novos_produtos = [
    {**p,'preco':round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

print('Produtos')
print(*novos_produtos, sep='\n')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p:p['nome'],
    reverse = True
)

print()
print('Produtos ordenados por nome')
print()
print(*produtos_ordenados_por_nome, sep='\n')

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p:p['preco']
)

print()
print('Produtos Ordenados por preço crescente')
print()
print(*produtos_ordenados_por_preco, sep='\n')
