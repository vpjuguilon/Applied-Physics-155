from numpy import exp, arange


def f(x):
    return 1 - exp(-2*x)


def fprime(x):
    return (2*exp(-2*x))


# Relaxation
counter1 = 0
x1 = 1
accuracy = 1e-6
error = 1
while error > accuracy:
    x1, x2 = f(x1), x1
    error = abs((x2-x1)/(1-1/(fprime(x2))))
    counter1 += 1
print("Relaxation method")
print("Solution is", x1)
print("Iterations:", counter1)
print()

#Overrelaxation
counter2 = 0
error = 1
x1 = 1
w = 0.5
while error > accuracy:
    x1, x2 = (1+w)*f(x1) - w*x1, x1
    counter2, counter3 = counter2 + 1, counter2
    error = abs((x2 - x1) / (1 - 1/((1+w)*fprime(x2)-w)))
print("Overrelaxation method (w=0.5)")
print("Solution is", x1)
print("Iterations:", counter2)


