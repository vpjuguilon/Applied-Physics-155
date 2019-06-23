from numpy import pi, cos, sin, sqrt
r = float(input("Enter r: "))
theta = float(input("Enter theta (degrees): ")) * pi/180

x = r*cos(theta)
y = r*sin(theta)

print("X is", x, "and Y is", y)