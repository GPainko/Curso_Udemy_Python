"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo local e global.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local 
pode ser alcançados.
"""

x = 2

def escopo():
    x = 1
    print(x)

print(x)

escopo() 