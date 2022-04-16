import numpy as np


def task_b(matrix_a):
    a_transposed = matrix_a.transpose()
    b = a_transposed.dot(matrix_a[:, -1])
    return np.insert(matrix_a, 2, b, axis=0)
