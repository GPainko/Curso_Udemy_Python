# Operação ternárias(condicional de uma linha)
# <valor> if <condicao> else <outro valor>

condicao = 10==11

var = 'valor' if condicao else 'outro valor'

print(var)

digito = 9
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(digito)



