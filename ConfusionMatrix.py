import numpy as np
from sklearn.model_selection import train_test_split, cross_val_predict
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt


def normalized_confusion_matrix(model, X_train, y_train, class_names):
    '''
    Analyze how your model underperforms by class.
    Function variables:
        model: ML model
        X_train: Training data
        y_train: Training labels
        class_names: List of class names
    '''
    model.fit(X_train,y_train)
    y_train_pred = cross_val_predict(model, X_train , y_train, cv = 3)
    conf = confusion_matrix(y_train , y_train_pred)
    conf_sum = conf.sum(axis = 1 , keepdims = True)
    normed_conf = conf / conf_sum

    plt.imshow(normed_conf, aspect = 'auto')
    plt.colorbar()
    y_vals = [str(i) for i in class_names]
    x_vals = y_vals
    y_axis = np.arange(0,len(y_vals),1)
    plt.yticks(y_axis, y_vals)
    plt.xticks(y_axis , x_vals)
    plt.xlabel('Predicted', labelpad=13, fontsize = 15)
    plt.ylabel('Actual', labelpad=13, fontsize = 15)

    for (index1, index2), value in np.ndenumerate(normed_conf):
        plt.text(index1, index2, round(value,2) , ha = 'center', va = 'center')

    plt.show()


if __name__ == '__main__':
    iris = load_iris()
    X , y = iris.data , iris.target
    X_train , X_test, y_train , y_test = train_test_split(X, y, random_state=0)
    classes = iris.target_names
    model = RandomForestClassifier()
    print(normalized_confusion_matrix.__doc__)
    normalized_confusion_matrix(model, X_train , y_train, classes)

    








