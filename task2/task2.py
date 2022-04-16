import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split


def task2():
    print('START TASK 2')
    ds = pd.read_table('http://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tra', sep=',', header=None)
    x = ds[ds.columns[0:6]].to_numpy()
    y = ds[ds.columns[-1]].to_numpy()

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, shuffle=True)

    clf = svm.SVC()
    clf.fit(x_train, y_train)

    gram_train = np.dot(x_train, x_train.T)
    clf.fit(gram_train, y_train)
    gram_test = np.dot(x_test, x_train.T)

    predicted = clf.predict(gram_test)
    print(predicted)
    print('Train score:', clf.score(gram_train, y_train))
    print('Test score:', clf.score(gram_test, y_test))