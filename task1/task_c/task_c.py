import numpy as np
import matplotlib.pyplot as plt

def task_c(a):
    # min_rows = np.amin(a)
    # print(min_rows)
    # print(a)
    # print(a.shape[0])
    # rows_count = a.shape[0]
    min_counts = []
    min_els = []
    for row in a:
        min_el = np.amin(row)
        min_els.append(min_el)
        min_indices = np.argwhere(row == min_el)
        min_counts.append(len(min_indices))
    print(min_els, min_counts)
    y_pos = np.arange(len(min_els))
    plt.bar(y_pos, min_counts, align='center', alpha=0.5)
    plt.xticks(y_pos, min_els)
    plt.ylabel('Count')
    plt.title('Minimum count per row')
    plt.show()
    # return min_counts
