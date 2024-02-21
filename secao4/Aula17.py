#csv
import csv
from pathlib import Path

CAMINHO_CSV =Path(__file__).parent /'Aula17.csv'

# with open(CAMINHO_CSV,'r') as arquivo:
#     leitor = csv.reader(arquivo)
#     for linha in leitor:
#         print(linha)

with open(CAMINHO_CSV,'r') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        print(linha)
        print(linha['Nome'])