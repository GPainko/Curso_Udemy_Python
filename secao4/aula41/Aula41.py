# Pillow: Redimensionando imagens com Python

from PIL import Image
from pathlib import Path

ROOT_FOLDE = Path(__file__).parent
ORIGINAL = ROOT_FOLDE / 'imagem.jpg'
NEW_IMAGE = ROOT_FOLDE / 'new.jpg'

pil_imagem = Image.open(ORIGINAL)

width, height = pil_imagem.size

# width     new_width
# height    new_height

new_width = 640
new_height = round(height * new_width / width)

new_image = pil_imagem.resize(size=(new_width, new_height))

new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70,
)
