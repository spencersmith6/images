from filter import *

def laplace(data):
    p = data[1]+data[3]+data[5]+data[7]-(4*data[0])
    return p

img = open(sys.argv)
img.show()
imgup = filter(img,laplace)
imgup.show()