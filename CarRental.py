# Necessary Imports
from numpy import matmul, array
from numpy.linalg import eig

# Parameters

p0 = 200  # Initial cars at P

q0 = 200  # Initial cars at Q

r0 = 200  # Initial cars at R

weeks = 10

# Variables

x1 = array([[p0, q0, r0]]).T  # Column vector built from initial conditions

M1 = array(([0.6, 0.1, 0.1], [0.1, 0.8, 0.2], [0.3, 0.1, 0.7]))  # Rental distribution matrix


# Main function

def main():
    # Run ratestep function and print to find cars at each location after n weeks
    print(ratestep(x1, M1, weeks))
    # Find eigenvalues and Eigenvectors of M
    w, v = eig(M1)
    # Find eigenvalue that describes our situation, then normalize it, then scale it be our number of cars
    xinf = 600 * v[:, 0] / sum(v[:, 0])
    # Print eigenvalue
    print(xinf)


# Rate function
def ratestep(x, M, t):
    # Run equation number of times equal to the number of weeks
    for k in range(t):
        # Calculate new x based on old x multiplied by our matrix
        x = matmul(M, x)
    return x


main()
