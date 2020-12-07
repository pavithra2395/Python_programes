import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize as opt

def load_data(path, header):
    marks_df = pd.read_csv(path, header=header)
    return marks_df

if __name__ == "__main__":
    
    data = load_data("marks.csv",None)
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    admitted = data.loc[y == 1]
    not_admitted = data.loc[y == 0]
    
    plt.scatter(admitted.iloc[:, 0], admitted.iloc[:, 1], s=10, label='Eligible')
    plt.scatter(not_admitted.iloc[:, 0], not_admitted.iloc[:, 1], s=10, label='Not eligible')
    plt.legend()
    plt.show()

    X = np.c_[np.ones((X.shape[0], 1)), X]
    y = y[:, np.newaxis]
    theta = np.zeros((X.shape[1], 1))

def sigmoid(x):
  
    return 1 / (1 + np.exp(-x))

def total_input(theta, x):
   
    return np.dot(x, theta)

def probability(theta, x):
   
    return sigmoid(total_input(theta, x))

def cost_function( theta, x, y):
    
    m = x.shape[0]
    total_cost = -(1 / m) * np.sum(y * np.log(probability(theta, x)) + (1 - y) * np.log(1 - probability(theta, x)))
    return total_cost

def gradient( theta, x, y):
    
    m = x.shape[0]
    return (1 / m) * np.dot(x.T, sigmoid(total_input(theta, x)) - y)

def fit(x, y, theta):
    opt_weights = opt.fmin_tnc(func=cost_function,x0=theta,fprime=gradient,args=(x, y.flatten()))
    return opt_weights[0]

parameters = fit(X, y, theta)

x_values = [np.min(X[:, 1] - 5), np.max(X[:, 2] + 5)]
y_values = - (parameters[0] + np.dot(parameters[1], x_values)) / parameters[2]

plt.plot(x_values, y_values, label='Decision Boundary')
plt.xlabel('Marks in 1st Exam')
plt.ylabel('Marks in 2nd Exam')
plt.legend()
plt.show()

def predict( x):
    theta = parameters[:, np.newaxis]
    return probability(theta, x)

def accuracy( x, actual_classes, prob_threshold=0.5):
    predicted_classes = (predict(x) >= prob_threshold).astype(int)
    predicted_classes = predicted_classes.flatten()
    accuracy = np.mean(predicted_classes == actual_classes)
    return accuracy * 100

accuracy(X, y.flatten())