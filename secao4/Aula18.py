import csv
from pathlib import Path

CAMINHO_CSV =Path(__file__).parent /'Aula18.csv'

lista_clientes = [
    {'Nome':'Guilherme Painko','Endereço':'Av 3, 22'},
    {'Nome':'João Snow','Endereço':'Av 5, 20'},
    {'Nome':'Maria Sol','Endereço':'Av 5, 22'}
] 

print(lista_clientes[0].keys())

with open(CAMINHO_CSV,'w')as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.writer(arquivo)

    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )

    escritor.writeheader()

    for cliente in lista_clientes:
        escritor.writerow(cliente)