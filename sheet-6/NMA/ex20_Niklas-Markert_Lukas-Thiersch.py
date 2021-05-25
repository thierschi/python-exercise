# ------------------------------------------------------------------------------

# Sheet 6 Exercise 20

# Niklas Markert - 1611460 / bt70985
# Lukas Thiersch - 1607110 / bt708626

# ------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt


# explicit solution
def x_sol(t, x):
    x[0] = np.exp(-3*t/2000) * (125*np.sqrt(3)/9 * np.sin(np.sqrt(3)*t/2000) - 125/3*np.cos(np.sqrt(3)*t/2000)) + 125/3 + t/24
    x[1] = -250*np.sqrt(3)/9 * np.exp(-3*t/2000) * np.sin(np.sqrt(3)*t/2000) + t/24
    x[2] = np.exp(-3*t/2000) * (125/3*np.cos(np.sqrt(3)*t/2000) + 125*np.sqrt(3)/9 * np.sin(np.sqrt(3)*t/2000)) + t/24 - 125/3


h = 120
t = 1440


# a)
A = np.array([[-1, 0, 1],
              [1, -1, 0],
              [0, 1, -1]]) * (1/1000)

b = np.array([[0.125, 0, 0]]).T


# b)
steps = t // h + (1 if t % h == 0 else 0)  # Calculation amount of steps, used in all following calculations
print("You need", steps, "steps.")  # -- With t = 1440 and h = 120 you need 13 Steps.

X_expl = np.zeros((3, steps))
for i in range(1, steps):
    x = X_expl[:, i-1].reshape(3, 1) + h * (np.dot(A, X_expl[:, i-1].reshape(3, 1)) + b)
    X_expl[0, i] = x[0, 0]
    X_expl[1, i] = x[1, 0]
    X_expl[2, i] = x[2, 0]

print('\n Explicit Solution')
print(X_expl)


# c)
# Using k from exercise b)
X_impl = np.zeros((3, steps))
for i in range(1, steps):
    bi = X_impl[:, i-1].reshape(3, 1) + h * b
    Ai = np.identity(3) - h * A
    x = np.linalg.solve(Ai, bi)
    X_impl[0, i] = x[0, 0]
    X_impl[1, i] = x[1, 0]
    X_impl[2, i] = x[2, 0]

print('\n Implicit Solution')
print(X_impl)


# d)
# If you change h to 60 the plots of the approximations are getting closer to the plot of the exact solution.
# -> That means the lower h is, the better the approximations get.
#
# If you change h to 120 the plots of the approximations differ more from the plot of the exact solution.
# -> That means the higher h is, the worse the approximations get.



# Calculation Exact Solution
X_sol = np.zeros((3, steps))
for i in range(steps):
    x_sol(i * h, X_sol[:, i])

print('\n Exact Solution:')
print(X_sol)


# Plots:
#
plt.plot(np.arange(steps) * h, X_sol[0, :], color='r', label='x1')
plt.plot(np.arange(steps) * h, X_sol[1, :], color='b', label='x2')
plt.plot(np.arange(steps) * h, X_sol[2, :], color='g', label='x3')
plt.legend()

plt.plot(np.arange(steps) * h, X_expl[0, :], color='r', linestyle='dashed')
plt.plot(np.arange(steps) * h, X_expl[1, :], color='b', linestyle='dashed')
plt.plot(np.arange(steps) * h, X_expl[2, :], color='g', linestyle='dashed')
plt.plot(np.arange(steps) * h, X_impl[0, :], color='r', linestyle='dotted')
plt.plot(np.arange(steps) * h, X_impl[1, :], color='b', linestyle='dotted')
plt.plot(np.arange(steps) * h, X_impl[2, :], color='g', linestyle='dotted')
plt.show()