"""
Formatação básica de strings 
s - string
d - int
f - float
.<número de figitos>f
x ou X - hexadecimal
(caractere)(><^)(quantidade)
> - esquerda
< - direita
^- centro
sinal - + ou -
Ex.: 0>-100,1.f
Conversuion flags -!r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{variavel:-^10}')
print(f'{-1000.22345678:.1f}')
print(f'{1000.22345678:0=+10,.1f}')
print(f'o hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')