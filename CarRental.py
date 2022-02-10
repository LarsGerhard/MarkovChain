# Necessary Imports
from numpy import matmul, array, eig

# Parameters

p0 = 200

q0 = 200

r0 = 200

weeks = 10

# Variables

x1 = array([[p0, q0, r0]]).T

M = array(([0.6, 0.1, 0.1], [0.1, 0.8, 0.2], [0.3, 0.1, 0.7]))


# Main function

def main():
    print(ratestep(x1, weeks))


# Rate function
def ratestep(x, t):
    for k in range(t):
        x = matmul(M, x)
    return x


main()
