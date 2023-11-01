"""
CONSTANTEE = variáveis que não vão mudar
Muitas condições no mesmo if (ruim)
    <-  Contagem de Complexidade(ruim)
"""

velocidade = 61 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADA_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # A distãncia onde o radar pega

if velocidade > RADA_1 :
    print('velocidade ultrapassou o limite do radar')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <=(LOCAL_1 + RADAR_RANGE) and \
    velocidade > RADA_1 :
    print('carro multado em radar 1')
