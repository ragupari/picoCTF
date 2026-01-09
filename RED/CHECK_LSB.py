from PIL import Image

img = Image.open("red.png")
pixels = img.load()
w, h = img.size

bits = ""
for y in range(h):
    for x in range(w):
        r, g, b, a = pixels[x, y]
        bits += str(r & 1)  # try g & 1, b & 1, a & 1 as well

# Convert bits to bytes
data = []
for i in range(0, len(bits), 8):
    byte = bits[i:i+8]
    if len(byte) == 8:
        data.append(int(byte, 2))

print(bytes(data))
