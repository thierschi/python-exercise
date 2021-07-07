# ------------------------------------------------------------------------------

# Sheet 11 Exercise 32

# Niklas Markert - 1611460 / bt709885
# Lukas Thiersch - 1607110 / bt708626

# ------------------------------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics

# ------------------------------------------------------------------------------

np.random.seed(0)

# ------------------------------------------------------------------------------
# a)

df = pd.read_csv('ex32_data.csv')

y = df['Outcome']
x = df
del x['Outcome']

shape = df.shape[0]
test_data = int(shape * 0.25)
indices = np.arange(shape)

indices_of_test_data = np.random.choice(shape, test_data, replace=False)
indices_of_train_data = np.setdiff1d(indices, indices_of_test_data)

train_set_x = x.loc[indices_of_train_data, ('Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age')].to_numpy().T
train_set_y = y.loc[indices_of_train_data].to_numpy().T

test_set_x = x.loc[indices_of_test_data, ('Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age')].to_numpy().T
test_set_y = y.loc[indices_of_test_data].to_numpy().T

# ------------------------------------------------------------------------------
#b)


def initialize_parameters(dim):
    w = np.random.randn(dim, 1)
    b = 0.
    return w, b


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def propagate(w, b, X, y):
    m = X.shape[1]
    # Calculate a
    z = np.dot(w.T, X) + b
    a = sigmoid(z)
    cost = - 1 / m * np.sum(y * np.log(a) + (1 - y) * np.log(1 - a))
    if(cost == np.NaN):
        cost = np.inf
    # Calculate dw, db
    dw = 1 / m * np.dot(X, (a - y).T)

    db = 1 / m * np.sum(a - y)
    cost = np.squeeze(cost)
    grads = {'dw': dw,
             'db': db}

    return grads, cost


def optimize(w, b, X, y, num_iter, learning_rate):
    costs = []
    for i in range(num_iter):
        grads, cost = propagate(w, b, X, y)

        w = w - learning_rate * grads['dw']
        b = b - learning_rate * grads['db']

        if i % 10000 == 0:
            costs.append(cost)
            print('Euclidean norm of the gradient:',np.sum(grads['dw']**2) + np.sum(grads['db']**2))

    params = {'w': w,
              'b': b}
    return params, grads, costs


def predict(w, b, X):
    a = sigmoid(np.dot(w.T, X) + b)
    a[a >= 0.5] = 1.
    a[a < 0.5] = 0.
    return a


def model(x_train, y_train, x_test, y_test, num_iter, learning_rate):
    n = x_train.shape[0]
    w, b = initialize_parameters(n)
    params, grads, costs = optimize(w, b, x_train, y_train, num_iter, learning_rate)

    y_hat_train = predict(params['w'], params['b'], x_train)
    y_hat_test = predict(params['w'], params['b'], x_test)

    print('training error: ', np.mean(np.abs(y_hat_train - y_train)))
    print('test error: ', np.mean(np.abs(y_hat_test - y_test)))
    return params, costs

# ------------------------------------------------------------------------------
# c)

params, costs = model(train_set_x, train_set_y, test_set_x, test_set_y, 1000001, 0.00025)
plt.plot(costs)
plt.show()

# ------------------------------------------------------------------------------
# d)

y_reshaped = test_set_y.shape[0]
w, b = initialize_parameters(y_reshaped)
params, grads, costs = optimize(w, b, test_set_x, test_set_y, 1000001, 0.00025)
test_set_y = test_set_y.reshape(-1, 1)
test_y = predict(params['w'], params['b'], test_set_y)
cnf_matrix = metrics.confusion_matrix(test_set_y, test_y)
print(cnf_matrix)

