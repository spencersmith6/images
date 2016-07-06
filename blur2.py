from filter import *

def avg(data):
    return sum(data) / len(data)

img = open(sys.argv)
img.show()
imgup = filter(img,avg)
imgup.show()