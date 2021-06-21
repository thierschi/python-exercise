# ------------------------------------------------------------------------------

# Sheet 8 Exercise 25 - Resubmission

# Niklas Markert - 1611460 / bt709885
# Lukas Thiersch - 1607110 / bt708626

# ------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import math

np.random.seed(0)
delta_t = 0.05


def random_walk_1(n, del_t):
    Z = np.random.randn(n)
    R_n = np.add.accumulate(Z) * math.sqrt(del_t)
    return R_n


def random_walk_2(n, del_t):
    Z = np.random.randn(n)
    R_n = np.add.accumulate(Z) * math.sqrt(0.75*del_t) + 4
    return R_n


# a)
walk = random_walk_1(365, delta_t)
plt.plot(walk)
plt.show()


# b)
amount = 150000
results = np.zeros(amount)
for i in range(amount):
    results[i] = random_walk_1(365, delta_t)[-1]

plt.hist(results, bins=101)
# plt.show()  # uncomment this line to see the 2 plots on separately
# ---------------
# The plot shows a normal distribution with values between around -15 and 15 with the mean of 0
# ---------------

results_2 = np.zeros(amount)
for i in range(amount):
    results_2[i] = random_walk_2(365, delta_t)[-1]
plt.hist(results_2, bins=101, color='red')
plt.show()
# ---------------
# The plot shifts around 4 units to the right and the spread slightly decreases.
# ---------------


# c)
walks = list()
for i in range(6):
    walks.append(np.insert(random_walk_1(20, delta_t), 0, 0))

plt.plot(walks[0], walks[1], color='blue')
plt.plot(walks[2], walks[3], color='red')
plt.plot(walks[4], walks[5], color='green')
plt.show()
