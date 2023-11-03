"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str,int,float,bool
"""
string = 'guilherme painko scalcon'
outra_variavel = f'{string[:3]}abc{string[4:]}'
#string[3] = 'abc' -> não é possivel mudar valor da string
print(string[3])
print(string.zfill(25))
print(outra_variavel)
print(string.capitalize())
