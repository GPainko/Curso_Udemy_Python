import locale
import string
from datetime import datetime
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'Aula21.txt'

locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(numero: float) -> str:
    brl = 'R$ ' + locale.currency(numero, symbol=False, grouping=True)
    return brl


data = datetime(2024, 2, 21)
dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (00) 0000-0000'
)


class MyTemplate(string.Template):
    delimiter = '%'


with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    texto = arquivo.read()
    template = MyTemplate(texto)
    print(template.safe_substitute(dados))