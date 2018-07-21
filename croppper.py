
from PIL import Image

imgName = "./good.png"

sizeX, sizeY = 110, 110


img = Image.open(imgName)
imgWidth = img.size[0]
imgHeight = img.size[1]

x, y = 0, 0
i = 0

while (y + sizeY < imgHeight):
	x = 0
	while (x + sizeX < imgWidth):
		img.crop((x, y, x + sizeX , y + sizeY)).save("./img"+str(i)+".png")
		x += sizeX
		y += sizeY
		i += 1