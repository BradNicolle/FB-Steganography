import sys
import os
from PIL import Image

filename = sys.argv[1]

text = input()
text += "\0"
bytes = text.encode('utf-8')
result = []
for c in bytes:
  for i in range(8, 0, -2):
  	result.append((c >> (i-2)) & 0x03)

image = Image.open(filename)

pixels = list(image.getdata())
pixels = [((pixel[0] & 0xFC) + bits, pixel[1], pixel[2]) for pixel, bits in zip(pixels, result)]
image.putdata(pixels)
image.save(os.path.splitext(os.path.basename(filename))[0] + "_encoded.png", "PNG")
