from barcode import EAN13
from barcode.writer import ImageWriter

codigo_barra = EAN13("123123123123", writer= ImageWriter())
codigo_barra.save("codigo_barra")

codigo_produtos = {
    "feijão": "551746511111",
    "arroz": "665789011111",
    "Macarrao": "665887111111",
    "Azeite": "998556211111",
}

for produto in codigo_produtos:
    codigo= codigo_produtos[produto]
    codigo_barra = EAN13(codigo, writer=ImageWriter())
    codigo_barra.save(f"codigo_barra_{produto}")

import qrcode

imagem_qrcode = qrcode.make("https://github.com/ORenatoBarbosa")
imagem_qrcode.save("qrcode_python.png")

links_produtos = {
    "Facebook": "https://www.facebook.com/Orenatobarbosa",
    "Github": "https://github.com/ORenatoBarbosa",
    "Youtube": "https://www.youtube.com/channel/UCl43MsmlrBMkCcOCmtABnNQ",
    "Linkedin": "https://www.linkedin.com/in/orenatobarbosa/",
    "Twitter": "https://twitter.com/Orenato_barbosa",
}
for produto in links_produtos:
    link = links_produtos[produto]
    imagem_qrcode = qrcode.make("link")
    imagem_qrcode.save(f"qrcode_{produto}.png")

# Renato Barbosa
