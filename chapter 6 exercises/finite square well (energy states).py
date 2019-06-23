from numpy import log2, sqrt, tan
from scipy.constants import m_e, e, hbar


def even(E):
    w = 1e-9
    V = 20 * e
    me = m_e
    return tan(sqrt((w**2 * me * E) / (2*hbar**2))) - sqrt((V-E)/E)  # Find root to solve for E


def odd(E):
    w = 1e-9
    V = 20 * e
    me = m_e
    return tan(sqrt((w**2 * me * E) / (2*hbar**2))) + sqrt(E / (V - E))   # Find root to solve for E


error = 0.001 * e   # Accuracy of 0.001 eV
delta = 0.02*e  # Distance between initial points x1 and x2 is 0.01
N = int(log2(delta/error))


# Energy estimates: 5.08164e-20 J, 2.02169e-19 J, 4.57206e-19 J, 8.09338e-19 J, 1.25793e-18, 1.79522e-18, 2.41458e-18
# E_0
E_estimates = [5.08164e-20, 2.02169e-19, 4.57206e-19, 8.09338e-19, 1.25793e-18, 1.79684e-18, 2.41458e-18]
for estimate_counter in range(len(E_estimates)):
    if estimate_counter % 2 == 0:
        E0_guess = E_estimates[estimate_counter]
        x1 = E0_guess - (delta/2)
        x2 = E0_guess + (delta/2)
        for i in range(N):
            E0 = (x1+x2)/2
            if even(x1)*even(E0) < 0:    # If x1 and E are opposite signs
                x2 = E0
            elif even(x2)*even(E0) < 0:  # If x2 and E are opposite signs:
                x1 = E0

        print("E" + str(estimate_counter), "is", E0/e, "eV.")
        print(even(E0))
        print()
    elif estimate_counter % 2 == 1:
        E1_guess = E_estimates[estimate_counter]
        x1 = E1_guess - (delta/2)
        x2 = E1_guess + (delta/2)
        for i in range(N):
            E1 = (x1+x2)/2
            if odd(x1)*odd(E1) < 0:    # If x1 and E are opposite signs
                x2 = E1
            elif odd(x2)*odd(E1) < 0:  # If x2 and E are opposite signs:
                x1 = E1

        print("E" + str(estimate_counter), "is", E1/e, "eV.")
        print(odd(E1))
        print()

