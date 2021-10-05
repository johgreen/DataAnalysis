# This is an alteration of documentation code meant to plot
# a decision boundary for scikit-learn classifiers.

import numpy as np
import matplotlib.pyplot as plt


def decision_surface(model, X, y, plot_step=0.02, xlabel='feature 0', ylabel='feature 1',
                     Title='Decision Surface'):
    '''
    Creates a plot of a decision surface from a scikit-learn classifying model. The parameters are -
    model: Classifier
    X: coordinates
    y: labeled data
    plot_step: a measure of how course the meshgrid is
    xlabel, ylabel: axes labels
    Title: plot suptitle
    '''

    # Train
    clf = model.fit(X, y)

    # Plot the decision boundary

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                         np.arange(y_min, y_max, plot_step))

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    cs = plt.contourf(xx, yy, Z, cmap='Greens')

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    new_arr = list(zip(X, y))
    cl0, cl1 = [], []
    for i in range(len(new_arr)):
        if new_arr[i][1] == 0:
            cl0.append(new_arr[i][0])
        else:
            cl1.append(new_arr[i][0])
    cl0_array = np.array(cl0)
    cl1_array = np.array(cl1)

    plt.scatter(cl0_array[:, 0], cl0_array[:, 1], label='0', color='k', marker='^')
    plt.scatter(cl1_array[:, 0], cl1_array[:, 1], label='1', color='tab:olive', marker='s')

    plt.suptitle(Title)
    plt.axis("tight")
    plt.show()

