from numpy import loadtxt, zeros, shape, exp
from numpy.fft import rfft2, irfft2
from matplotlib.pyplot import imshow, gray, show

blur = loadtxt("blur.txt", float)

pointspread = zeros(shape(blur))
sigma = 25
for x in range(-512, 512):
    for y in range(-512, 512):
        pointspread[x, y] = exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))



cblur = rfft2(blur)
cpoint = rfft2(pointspread)
ca = zeros(shape(cblur))
eps = 1e-3


for y in range(0, 1024):
    for x in range(0, 513):
        if cpoint[y, x] < eps:
            ca[y, x] = 0
        else:
            ca[y, x] = cblur[y, x] / cpoint[y, x]

a = irfft2(ca)
imshow(a)
gray()
show()


