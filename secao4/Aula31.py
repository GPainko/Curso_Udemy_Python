from pathlib import Path

from PyPDF2 import PdfReader

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20240223-1.pdf'
PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BACEN)

# print(len(reader.pages))
# for page in reader.pages:
#     print(page)
#     print()

page0 = reader.pages[0]
print(page0.extract_text())

