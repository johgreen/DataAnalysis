
#logistic regression from scratch

import numpy as np


def sigmoid(x):
    sigmoid = (1 + np.exp(-x))**(-1)
    return sigmoid

class LogisticRegression:

    def __init__(self , learn_rate = 0.001 , n_iters = 1000):
        self.learn_rate = learn_rate 
        self.n_iters = n_iters
        self.weights = None
        self.bias = None
        self.y_predict = None
        self.y_predict_test = None

    def fit(self , X , y):
        n_samples , n_features = X.shape

        self.weights = np.zeros(n_features)

        #gradient descent
        for _ in range(self.n_iters):

            y_predict = np.dot(X , self.weights)
            y_predict = sigmoid(y_predict)

            #gradient 
            dw = (1 / n_samples) * np.dot(X.T , (y_predict - y))

            #update parameter
            self.weights -= self.learn_rate * dw
    
    def predict(self, X):
            
        self.y_predict = np.dot(X , self.weights)
        self.y_predict = sigmoid(self.y_predict)

        prediction = np.array([1 if i > 0.5 else 0 for i in self.y_predict])

        return prediction
        
    def score(self , X , y):
    
        '''
        Returns 2 scores. The Brier score is good for True/False situations, whereas the 
        accuracy_score is a generic fraction of correct predictions.
        '''

        n_samples , n_features = X.shape

        #probability predictions on new data
        self.y_predict_test = np.dot(X , self.weights)
        self.y_predict_test = sigmoid(self.y_predict_test)

        #score 1 (smaller scores are better)
        brier_score = np.sum((self.y_predict_test - y)**2) / n_samples

        #score 2
        test_prediction = np.array([1 if i > 0.5 else 0 for i in self.y_predict_test])
        accuracy_score = np.sum([y == test_prediction])/n_samples
        
        return brier_score , accuracy_score


#test the algorithm

#artificial data
from sklearn.datasets import make_blobs
X , y = make_blobs(n_samples = 1000 , centers = 2 , cluster_std = .5  , center_box = (-5,5))


if __name__ == '__main__':
    model = LogisticRegression()
    model.fit(X , y)
    predictions = model.predict(X)
    print(model.score(X , y))

    #plot the predictions
    import matplotlib.pyplot as plt
    plt.scatter(X[:,0] , X[:,1], c = predictions)
    plt.show()

    
    













