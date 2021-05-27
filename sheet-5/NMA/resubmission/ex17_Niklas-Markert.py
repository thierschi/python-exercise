# ------------------------------------------------------------------------------

# Sheet 5 Exercise 17 - Resubmission

# Niklas Markert - 1611460 / bt70985

# ------------------------------------------------------------------------------
import numpy as np
# ------------------------------------------------------------------------------

# a)

a_matrix = np.array([[9, 5], [4, 2]])
a_result = 3 * a_matrix
print("Result from a):\n", a_result)
print()

# ------------------------------------------------------------------------------

# b)

b_matrix1 = np.array([1, 2, 3])
b_matrix2 = b_matrix1.reshape(3, 1)
b_result = np.dot(b_matrix1, b_matrix2)
print("Result from b):\n", b_result)
print()

# ------------------------------------------------------------------------------

# c)

c_matrix = np.arange(1, 7).reshape(3, 2).T
c_result = 2 * c_matrix * 3
print("Result from c):\n", c_result)
print()

# ------------------------------------------------------------------------------

# d)

d_matrix1 = np.arange(4, 7).reshape(3, 1)
d_matrix2 = np.arange(7, 10).reshape(1, 3)
d_result = np.dot(d_matrix1, d_matrix2)
print("Result from d):\n", d_result)
print()

# ------------------------------------------------------------------------------

# e)

e_matrix1 = np.array([[9, 5], [4, 2]])
e_matrix2 = np.array([[1, 0], [0, 1]])
e_result = e_matrix1 - e_matrix2
print("Result from e):\n", e_result)
print()

# ------------------------------------------------------------------------------

# f)

try:
    f_matrix1 = np.rot90(np.arange(1, 7).reshape(3, 2))
    f_matrix2 = np.array([[7, 2], [3, 4]])
    f_result = f_matrix1 + f_matrix2
    print("Result from f):\n", f_result)
    print()
except ValueError:
    # This error is expected because you cannot
    # add an 2x3 Matrix onto an 2x2 matrix
    print("Result from f) cannot be calculated!")
    print()

# ------------------------------------------------------------------------------

# g)

g_matrix1 = np.array([[9, 4], [4, 2]])
g_matrix2 = np.array([[6, 2], [3, 4]])
g_result = np.dot(g_matrix1, g_matrix2)
print("Result from g):\n", g_result)
print()

# ------------------------------------------------------------------------------

# h)

h_matrix1 = np.arange(1, 7).reshape(3, 2)
h_matrix2 = np.array([[2, 4, 6],
                      [1, 3, 5]])
h_result = np.dot(h_matrix1, h_matrix2)
print("Result from h):\n", h_result)
print()

# ------------------------------------------------------------------------------
