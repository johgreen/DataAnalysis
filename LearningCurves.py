from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt

import numpy as np

def plot_learning_curves(model , X , y):
    X_train , X_test, y_train , y_test = train_test_split(X, y, random_state = 42)
    train_err , test_err = [], []
    for m in range(1, len(X_train)):
        model.fit(X_train[:m] , y_train[:m])
        y_train_predict = model.predict(X_train[:m])
        y_test_predict = model.predict(X_test)
        train_err.append(mean_squared_error(y_train_predict, y_train[:m]))
        test_err.append(mean_squared_error(y_test_predict , y_test))
        plt.plot(np.sqrt(train_err) , label = 'Train')
        plt.plot(np.sqrt(test_err) , label = 'Test')
        plt.title('Learning Curve')
        plt.xlabel('Num of Samples')
        plt.ylabel('RMSE')
        plt.legend()
