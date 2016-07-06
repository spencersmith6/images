from filter import *

def laplace(data):
    p = data[1]+data[3]+data[5]+data[7]-(4*data[0])
    return p

def minus(A,B):
    width, height = img.size
    fin = A.copy()
    pixels = fin.load()
    pixelsA = A.load()
    pixelsB = B.load()
    for x in range(0, width):
        for y in range(0, height):
            pixels[x,y]= pixelsA[x,y] - pixelsB[x,y]
    return fin


img = open(sys.argv)
img.show()
imgup = filter(img,laplace)
minus(img,imgup).show()

