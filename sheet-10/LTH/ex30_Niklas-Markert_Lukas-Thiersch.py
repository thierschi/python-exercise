# ------------------------------------------------------------------------------

# Sheet 10 Exercise 30

# Niklas Markert - 1611460 / bt709885
# Lukas Thiersch - 1607110 / bt708626

# ------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------

# a)

def f(w, b):
    return (1 - w) ** 2 + 100 * (b - w ** 2) ** 2

# ------------------------------------------------------------------------------

# b)

def propagate(w, b):
    cost = f(w, b)
    dw = np.sum(400 * w ** 3 - 400 * b * w + 2 * w - 2)
    db = np.sum(-200 * w ** 2 + 200 * b)
    grads = {'dw': dw,
             'db': db}
    return grads, cost

# ------------------------------------------------------------------------------

# c)

def optimize(w, b, num_iter, learning_rate):
    costs = []

    for i in range(num_iter):
        grads, cost = propagate(w, b)

        w = w - learning_rate * grads['dw']
        b = b - learning_rate * grads['db']

        costs.append(cost)

    params = {'w': w,
              'b': b}

    return params, grads, costs

# ------------------------------------------------------------------------------

# Do not change the following 5 lines - they are needed for the contour plot.
N = 250
lin = np.linspace(-0.2, 1.2, N)
wlin, blin = np.meshgrid(lin, lin)
f_values = f(wlin, blin)
plt.contour(wlin, blin, f_values.reshape(N, N), levels=np.logspace(-1,3,8))

# ------------------------------------------------------------------------------

# d) Find the parameters w and b that minimize f(w,b) and print these parameters
# as well as the corresponding function value.
params, grads, costs = optimize(0, 0, 7500, 0.001)
print('----- d) -----')
print('w:', params['w'])
print('b:', params['b'])
print('f(w,b):', f(params['w'], params['b']))

# Plot (w,b) as a single red point (or red star 'r*').
plt.plot(params['w'], params['b'], '.', color='red')
plt.show()


# Plot the costs
plt.plot(costs)
plt.show()

# ------------------------------------------------------------------------------

# e)

# Out of the values 0.001 to 0.009 (0.001 * i, with i element of [1,9]) only
# 0.001 and 0.002 seem to work well. Higher learning rates (observable starting
# at 0.003) produce massive spikes in the costs plot.
# Also a learning rate of 0.008 produces overflows in our code.

# ------------------------------------------------------------------------------

