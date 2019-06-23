from math import sqrt

hbar = 1.0545718e-34
me = 9.11e-31
E = float(input("Enter particle energy in eV: ")) * 1.60217662e-19
V = float(input("Enter potential step in eV: ")) * 1.60217662e-19
k1 = sqrt(2*me*E)/hbar
k2 = sqrt(2*me*(E-V))/hbar

T = 4*k1*k2 / (k1+k2)**2
R = ((k1-k2)/(k1+k2))**2

print("Transmission is", T, "and Reflections is", R)
print(T+R)
