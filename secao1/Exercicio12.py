"""
    CPF: 746.824.890-70
    Colete a soma dos 9 primeiros digitos do CPF
    multiplicando cada uma dos valores por uma 
    contagem regressiva começando de 10

    ex: 746.824.890-70(746824890)

        10 9 8 7 6 5 4 3 2 
    *   7  4 6 9 2 4 8 9 0

    SOMAR TODOS OS RESULTADOS:
    70+36+48+66+12+20+32+27+0 = 301
    multiplicar o resultado anterior por 10
    301 * 10
    obter o resto da divisão da conta anterior por 11
    3010 % 11 = 7
    se o resultado anterior for maior que 9:
        resultado é 0 
    contrario disso:
        resultado é o valor da conta
    o primeirp valor é 7
"""

cpf = '74682489070'
nove_digitos = cpf[:9]
contador_regressivo_1 = 10
resultado_digito_1 = 0

for digito_1 in nove_digitos:
    resultado_digito_1 += (int(digito_1)*contador_regressivo_1)
    contador_regressivo_1 -=1

digito_1 = resultado_digito_1 * 10 % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

print(digito_1)

