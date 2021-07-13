# ------------------------------------------------------------------------------

# Sheet 11 Exercise 31 - Resubmission

# Niklas Markert - 1611460 / bt709885

# ------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np


def f_eval(poly, z):
    """Evaluates a polynomial poly in z"""
    return sum(poly[j]*(z**j) for j in range(len(poly)))


# Setting up parameters
x = np.arange(0.0, 2.1, 0.1)
y = np.asarray([1, 5, 2, 3, 4, 1, 2, 5, 8, 10, 5, 4, 6, 1, 1, 3, 6, 9, 13, 8, 2])

n = 10


# ----- 1) -----
def create_A(degree, vector, transposed=False):
    A = np.zeros((len(vector), degree+1))
    for i in range(degree + 1):
        A[:, i] = vector**i
    if transposed:
        A = A.T
    return A


# ----- 2) -----
A = create_A(n, x)
AT = create_A(n, x, True)

ATA = np.dot(AT, A)
b = np.dot(AT, y)


# ----- 3) -----
a_direct = np.linalg.solve(ATA, b)

inv = np.linalg.inv(ATA)
a_via_inv = np.dot(inv, b)


# ----- 4) -----
def plot_polynomial(poly, x_fine, color):
    f_x = f_eval(poly, x_fine)
    plt.plot(x_fine, f_x, color=color)


my_plot = plt.plot(x, y, 'ro')

x_fine = np.arange(0.0, 2.01, 0.0005)
plot_polynomial(a_direct, x_fine, 'green')
plot_polynomial(a_via_inv, x_fine, 'blue')

plt.show()


# ----- 5) -----
print('----- 5) -----')

errors_direct = np.linalg.norm(np.dot(A, a_direct) - y, ord=2)
print(n, 'Error from a_direct:', errors_direct)

errors_via_inv = np.linalg.norm(np.dot(A, a_via_inv) - y, ord=2)
print(n, 'Error from a_via_inv:', errors_via_inv)


# ---------------------------------------------------
# Does the error for a_direct always decrease with higher n?
#
# No, with n=13 the error is 4.621.. but with n=14 the error increases to 4.674...
# In all other cases the error for a_direct decreases with higher n.
# ---------------------------------------------------
# Briefly describe your observations regarding the error for a_via_inv.
#
# From n=1 up to n=10 the error for a_via_inv is approximately the same as the error for a_direct.
# But beginning at n=12 the error for a_via_inv is rapidly increasing, with a peak at n=13 where the error is 85.707...
# ---------------------------------------------------
