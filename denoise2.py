from filter import *

def median(data):
    order = sorted(data)
    med = order[len(order)/2]
    return med

img = open(sys.argv)
img.show()
imgup = filter(img,median)
imgup.show()




