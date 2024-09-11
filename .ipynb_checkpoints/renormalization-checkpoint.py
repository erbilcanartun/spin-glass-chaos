import numpy as np
import mpmath as mp

def matrix_normalizer(matrix):
    return matrix / np.amax(matrix)

def element_ratio(matrix):
    return mp.log(matrix[0, 0] / matrix[0, -1])

def average_element_ratio(matrix_list):
    element_list = []
    for i in range(len(matrix_list)):
        element_list.append(element_ratio(matrix_list[i]))
    return np.mean(element_list)

def average_element_ratio_strength(matrix_list):
    element_list = []
    for i in range(len(matrix_list)):
        element_list.append(np.absolute(element_ratio(matrix_list[i])))
    return np.mean(element_list)

def transfer_matrix(spin, interaction):

    """
    Transfer-matrix for spin-s: [.. exp(J.SiSj/S^2) ..], spin_s = S of spin-S
    """
    J = interaction

    # Generate a list of spin values for spin-s system
    # e.g. spin-3/2 = [3/2, 1/2, 0, -1/2, -3/2]
    s = spin
    spin_values = []
    while s >= -spin:
        spin_values.append(s)
        s = s - 1

    # Generate a list of energy values that will be the arguments of exp functions in transfer matrix
    energy = []
    for i in range(len(spin_values)):
        for j in range(len(spin_values)):
            energy.append(J * spin_values[i] * spin_values[j] / spin**2)

    # Choose the maximum term to normalize the matrix
    energy_max = np.amax(energy)

    # Construct transfer matrix
    t = []
    counter = 0
    for i in range(len(spin_values)):
        row = []
        for j in range(len(spin_values)):
            row.append(mp.exp(energy[counter] - energy_max))
            counter = counter + 1
        t.append(row)

    return np.array(t)

def bond_moving(t1, t2):
    t = np.multiply(t1, t2)
    t = matrix_normalizer(t)
    return t#np.array(t)

def decimation(t1, t2):
    t = np.dot(t1, t2)
    t = matrix_normalizer(t)
    return t

# Renormalization procedure without symmetrization; works for any p
def renormalize(matrix_population, matrix_list):

    np.random.seed(19)

    N = len(matrix_list)

    renormalized = []
    for k in range(matrix_population):

        # Randomly select 27 matrices:
        # b^(d-1) matrices for b=3 and d=3
        bondmoved = []
        for i in range(3):
            # Bond-moving operation
            t = matrix_list[np.random.randint(1, N)]
            for j in range(8):
                t = bond_moving(t, matrix_list[np.random.randint(1, N)])

            bondmoved.append(t)

        # Decimation operation
        t = decimation(bondmoved[0], bondmoved[1])
        t = decimation(t,     bondmoved[2])

        renormalized.append(t)

    return renormalized


