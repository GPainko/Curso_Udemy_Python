"""
split - join com list e str
split - divide uma string
join - une uma string
"""

frase = ' olha só que, coisa interessante '
lista_palavras = frase.split(', ')
lista_frase = []

for i, frase in enumerate(lista_palavras):
   lista_frase.append(lista_palavras[i].strip())
    #rstrip corta espaço da direita
    #lstrip corta espaço da esquerda

print(lista_palavras)
print(lista_frase)

frases_unidas = ', '.join(lista_frase)
print(frases_unidas)

