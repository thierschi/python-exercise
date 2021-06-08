# ------------------------------------------------------------------------------

# Sheet 8 Exercise 25

# Niklas Markert - 1611460 / bt70985
# Lukas Thiersch - 1607110 / bt708626

# ------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import math

np.random.seed(0)
delta_t = 0.05


def random_walk_1(n, del_t):
    Z = np.random.rand(n)
    R_n = np.add.accumulate(Z) * math.sqrt(del_t)
    return R_n


def random_walk_2(n, del_t):
    Z = np.random.rand(n)
    R_n = np.add.accumulate(Z) * math.sqrt(0.75*del_t) + 4
    return R_n


# a)
walk = random_walk_1(365, delta_t)
plt.plot(walk)
plt.show()


# b)
amount = 1500
results = np.zeros(amount)
for i in range(amount):
    results[i] = random_walk_1(365, delta_t)[-1]

plt.hist(results, bins=101)
# ---------------
# The histogram shows that the most values are between 40 and 42.
# ---------------

results_2 = np.zeros(amount)
for i in range(amount):
    results_2[i] = random_walk_2(365, delta_t)[-1]
plt.hist(results_2, bins=101, color='red')
plt.show()
# ---------------
# When using formula 2 instead of 1 the plot shifts left, so that the
# most values are around 39.
# ---------------


# c)
walks = list()
for i in range(6):
    walks.append(np.insert(random_walk_1(20, delta_t), 0, 0))

plt.plot(walks[0], walks[1], color='blue')
plt.plot(walks[2], walks[3], color='red')
plt.plot(walks[4], walks[5], color='green')
plt.show()
