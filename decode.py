import sys
from PIL import Image

filename = sys.argv[1]

image = Image.open(filename)

bytes = bytearray()

pixels = list(image.getdata())

i = 0
for pixel in pixels:
  byte_i = int(i / 4)
  shift_amount = (3 - (i % 4)) * 2
  if (i % 4 == 0):
    bytes.append(0)
  bytes[byte_i] = bytes[byte_i] + ((pixel[0] & 0x03) << shift_amount)
  if (i % 4 == 3 and bytes[byte_i] == 0):
  	break
  i += 1

print(bytes.decode("UTF-8"))