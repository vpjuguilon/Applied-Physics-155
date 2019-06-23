import numpy as np

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

x1a = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a)
x2a = (-b - np.sqrt(b**2 - 4*a*c)) / (2*a)
solution1a = a*x1a**2 + b*x1a + c
solution2a = a*x2a**2 + b*x2a + c
print()
print("Method 1")
print("Root 1 is", x1a)
print("Accuracy rating of root 1 is", solution1a)
print("Root 2 is", x2a)
print("Accuracy rating of root 2 is", solution2a)
print()
x1b = 2*c / (-b - np.sqrt(b**2 - 4*a*c))
x2b = 2*c / (-b + np.sqrt(b**2 - 4*a*c))
solution1b = a*x1b**2 + b*x1b + c
solution2b = a*x2b**2 + b*x2b + c
print("Method 2")
print("Root 1 is", x1b)
print("Accuracy rating of root 1 is", solution1b)
print("Root 2 is", x2b)
print("Accuracy rating of root 2 is", solution2b)

if solution1a < solution1b:
    root1 = x1a
elif solution1b <= solution1a:
    root1 = x1b

if solution2a < solution2b:
    root2 = x2a
elif solution1b <= solution1a:
    root2 = x2b

print()
print("Lower accuracy rating = more accurate")
print("The roots are", root1, "and", root2)


