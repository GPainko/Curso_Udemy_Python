"""
Faça um programa que pergunte a hora ao usuário e, baseado no hórario 
descrito, exiba a saudação apropriada. Ex
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horas_str = input('informe as horas:(valor inteiro,sem os minutos) ')
horas_int = int(horas_str)

bom_dia = (0 <= horas_int <= 11 or horas_int == 24)
boa_tarde = (12 <= horas_int <= 17)
boa_noite = (18 <= horas_int <= 23)

if bom_dia:
    print('Bom Dia')
elif boa_tarde:
    print('Boa Tarde')
elif boa_noite:
    print('Boa Noite')
else:
    print('informou um valor invalido')
