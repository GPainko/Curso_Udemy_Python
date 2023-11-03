# while ultilizado quando não sabemos o final.

texto = 'python'

novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto+ '*')
