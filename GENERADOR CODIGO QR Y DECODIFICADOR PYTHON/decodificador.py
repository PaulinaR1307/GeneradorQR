from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/LENOVO/Desktop/GENERADOR CODIGO QR Y DECODIFICADOR PYTHON/mynewqr/mynewqr2.png')

result = decode(img)

print(result)
