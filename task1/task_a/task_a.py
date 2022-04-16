import numpy as np


def task_a():
    arr = np.linspace(10, 20, num=200, dtype='int')
    a = np.reshape(arr, (4, 50))
    return a
