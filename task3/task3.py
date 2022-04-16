import pandas as pd
from sklearn.cluster import SpectralClustering
import matplotlib.pyplot as plt


def task3():
    print('START TASK 3')
    ds = pd.read_table('http://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tra', sep=',',
                       header=None)
    x = ds[ds.columns[0:6]].to_numpy()
    clustering = SpectralClustering(n_clusters=2, affinity='nearest_neighbors', random_state=0).fit(x)
    labels = clustering.labels_

    plt.scatter(x[:, 0], x[:, 1], c=labels)
    plt.show()
