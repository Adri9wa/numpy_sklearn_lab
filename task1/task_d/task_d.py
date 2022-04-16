import matplotlib.pyplot as plt
import numpy as np


def task_d(a):
    columns_mean = np.mean(a, axis=0)
    x_scatter = np.arange(0, a.shape[1])
    print(np.amax(a[0]))
    y1 = np.arange(0, len(a[0]))
    y2 = np.arange(0, len(a[1]))
    plt.plot(a[0], a[0], label='first row')
    plt.plot(a[1], a[1], label='second row')

    higher = np.where((columns_mean > np.amax(a[1])) & (columns_mean > np.amax(a[0])), 'r', 'b')
    plt.scatter(x_scatter, columns_mean, c=higher)
    plt.legend()
    plt.show()
