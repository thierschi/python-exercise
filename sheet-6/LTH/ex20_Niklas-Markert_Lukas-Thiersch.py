# ------------------------------------------------------------------------------

# Sheet 6 Exercise 20

# Niklas Markert - 1611460 / bt70985
# Lukas Thiersch - 1607110 / bt708626

# ------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
# Important! If you are NOT using JupyterLab, comment the next line with #.
# %matplotlib inline


# explicit solution
def x_sol(t, x):
    x[0] = np.exp(-3*t/2000) * (125*np.sqrt(3)/9 * np.sin(np.sqrt(3)*t/2000) - 125/3*np.cos(np.sqrt(3)*t/2000)) + 125/3 + t/24
    x[1] = -250*np.sqrt(3)/9 * np.exp(-3*t/2000) * np.sin(np.sqrt(3)*t/2000) + t/24
    x[2] = np.exp(-3*t/2000) * (125/3*np.cos(np.sqrt(3)*t/2000) + 125*np.sqrt(3)/9 * np.sin(np.sqrt(3)*t/2000)) + t/24 - 125/3


h = 120
t = 1440
k = t // h + 1 # + 1 for t = 0
# => With until_time 1440 and step size 120 you need 13 steps (1440/120 + 1)

X_sol = np.zeros((3, k))
for steps in range(k):
     x_sol(steps * h, X_sol[:, steps])

print(X_sol)
# a)
A = np.array([[-1, 0, 1],
              [1, -1, 0],
              [0, 1, -1]]) * (1/1000)

b = np.array([[0.125, 0, 0]]).T

# b)
# Calc of steps k was moved up to be used from x_sol as well

step_results = [np.array([[0, 0, 0]]).T]
for i in range(1, k):
    res = step_results[i-1] + h * (np.dot(A, step_results[i-1]) + b)

    step_results.append(res)

X_expl = np.concatenate(step_results, 1)

# c)
step_results = [np.array([[0, 0, 0]]).T]
for i in range(1, k):
    left = np.identity(3) - h * A
    right = step_results[i-1] + h * b

    res = np.linalg.solve(left, right)

    step_results.append(res)

X_impl = np.concatenate(step_results, 1)

# d)
# The step-size denotes (because wa are talking about approximations) the precision
# with which the real values are approximated. The more frequent I try to approximate
# the real values the more precise they will get. And that is exactly what I observe:
#   With h = 60 the approximation is more precise => Closer to the plot of X_sol
#   With h = 120 the approximation is less precise => Farther away from the plot of X_sol

# Plots:
plt.plot(np.arange(k) * h, X_sol[0, :], color='r', label='x1')
plt.plot(np.arange(k) * h, X_sol[1, :], color='b', label='x2')
plt.plot(np.arange(k) * h, X_sol[2, :], color='g', label='x3')
plt.legend()
### Important: Activate the following lines once you have X_expl and X_impl
plt.plot(np.arange(k) * h, X_expl[0, :], color='r', linestyle='dashed')
plt.plot(np.arange(k) * h, X_expl[1, :], color='b', linestyle='dashed')
plt.plot(np.arange(k) * h, X_expl[2, :], color='g', linestyle='dashed')
plt.plot(np.arange(k) * h, X_impl[0, :], color='r', linestyle='dotted')
plt.plot(np.arange(k) * h, X_impl[1, :], color='b', linestyle='dotted')
plt.plot(np.arange(k) * h, X_impl[2, :], color='g', linestyle='dotted')
plt.show()
