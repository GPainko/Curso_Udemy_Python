"""
Cuidados com dados mutáveis
= - copiando o valor (imutaveis)
= - aponta para o mesmo valor na mémoria(mutavel)
"""

lista_a = ['luiz','joao',1,True,1.2]
lista_b= lista_a.copy()

lista_a[0] = 'qualquercois'

print(lista_a)
print(lista_b)