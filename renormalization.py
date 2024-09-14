import numpy as np
import mpmath as mp

def matrix_normalizer(matrix):
    return matrix / np.amax(matrix)

def interaction(matrix):
    # Divide first element by last element of the first row
    n = matrix.rows
    return mp.log(matrix[0, 0] / matrix[0, n - 1]) / 2

def average_interaction(matrix_list):
    element_list = []
    for i in range(len(matrix_list)):
        element_list.append(interaction(matrix_list[i]))
    return np.mean(element_list)

def average_interaction_strength(matrix_list):
    element_list = []
    for i in range(len(matrix_list)):
        element_list.append(np.absolute(interaction(matrix_list[i])))
    return np.mean(element_list)

def transfer_matrix(spin, interaction):

    J = mp.mpf(interaction)

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
    n = len(spin_values)
    t = mp.matrix(n)
    counter = 0
    for i in range(n):
        for j in range(n):
            t[i, j] = mp.exp(energy[counter] - energy_max)
            counter = counter + 1

    return matrix_normalizer(t)

def mp_multiply(t1, t2):
    n = len(t1)
    t = mp.matrix(n)
    for i in range(n):
        for j in range(n):
            t[i, j] = t1[i, j] * t2[i, j]
    return matrix_normalizer(t)

def bond_moving(t1, t2):
    t = mp_multiply(t1, t2)
    t = matrix_normalizer(t)
    return t#np.array(t)

def decimation(t1, t2):
    t = t1 * t2
    t = matrix_normalizer(t)
    return t

# Renormalization procedure without symmetrization; works for any p
def renormalize(matrix_population, matrix_list, seed=None):

    np.random.seed(seed)

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