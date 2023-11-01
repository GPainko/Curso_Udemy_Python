# Operadores lógicos
# and (a) or (ou) not (não)
# and - Todas as condições precisam
# ser verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerado falsy(que vc já viu)
# 0 0.0 '' false
# Também existe o tipo None que é
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('senha: ')
senha_permitida = '123456'
#if True:
#    ...
if entrada == 'E'and senha_digitada == senha_permitida:
    print('entrar')
else:
    print('sair')

print(True and False and True)
print(bool(0))
print(bool(0.0))
print(bool(""))