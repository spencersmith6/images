import sys
from PIL import Image

# define your flip function here

def flip(img):
	width, height = img.size
	imgup = img.copy()
	m = img.load()
	m2 = imgup.load()

	for x in range(0, width):
		for y in range(0, height):
			m2[x, y] = m[width - x - 1, y]

	imgup.show()


if len(sys.argv)<=1:
	print ("missing image filename")
	sys.exit(1)
filename = sys.argv[1]
img = Image.open(filename)
img = img.convert("L")
img.show()

# call your flip function here
flip(img)



