# Operadores lógicos
# and (a) or (ou) not (não)
# or - Qualquer condição verdadeira.
# toda a expressão como verdadeira.
# se qualquer valor for considerado verdadeiro.
# a expressão inteira será avaliada naquele valor.
# São considerados falsy(que vc já viu)
# 0 0.0 "" False
# Também existe o tipo None que é
#usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('senha: ')
senha_permitida = '123456'
#if True:
#    ...
if (entrada == 'E'or entrada == 'e') and senha_digitada == senha_permitida:
    print('entrar')
else:
    print('sair') 

print(True or False or True)   

senha = input('senha:') or 'sem senha'
print(senha)