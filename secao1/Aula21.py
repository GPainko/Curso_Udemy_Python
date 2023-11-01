"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal(0123456789ABCDEF) 
"""

nome = 'luiz'
preco = 1000.956789
variavel = '%s, o preço total foi R$%.2f' %(nome,preco)
print(variavel)
print('o hexadecimal de %d é %04X'%(15,15))