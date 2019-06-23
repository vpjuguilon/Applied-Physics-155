from numpy import loadtxt, zeros, shape, exp
from matplotlib.pyplot import plot, show, xlabel, ylabel, imshow, colorbar, gray

def fpointspread():
    blur = loadtxt("blur.txt", float)
    pointspread = zeros(shape(blur))
    sigma = 25

    for x in range(-512, 512):
        for y in range(-512, 512):
            pointspread[x, y] = exp(-(x**2 + y**2)/(2*sigma**2))

    return pointspread


#imshow(pointspread())
#gray()
#show()


