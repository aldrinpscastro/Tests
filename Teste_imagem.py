#!/usr/bin/env python3
from PIL import Image, ImageFont, ImageDraw
escrever = ['Aldrin', 'Matheus', 'Reginaldo', 'Ana']
for msg in escrever:
    im = Image.open("certificado-americana-1.jpg")
    largura, altura = im.size
    print(largura, altura)
    fonte = ImageFont.truetype("/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-B.ttf", 100)
    largtexto, altutexto = ImageDraw.Draw(im).textsize(msg, fonte)
    print(largtexto, altutexto)
    ImageDraw.Draw(im).text(((largura / 2) - (largtexto / 2), altura / 2.105), msg, (0,0,0), font=fonte)
    im.save("certificado-americana-1-" + msg + ".png")