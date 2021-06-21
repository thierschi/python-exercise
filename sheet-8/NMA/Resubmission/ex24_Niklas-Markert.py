# ------------------------------------------------------------------------------

# Sheet 8 Exercise 24 - Resubmission

# Niklas Markert - 1611460 / bt709885
# Lukas Thiersch - 1607110 / bt708626

# ------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2)


def plot_min_max(index_min, index_max, array):
    plt.plot(index_min, array[index_min], marker='o', markersize=8, color='green')
    plt.plot(index_max, array[index_max], marker='o', markersize=8, color='red')


# a)
data = np.load('ex24_data.npy')
plt.plot(data)


# b)
acc_min = np.minimum.accumulate(data)
profit = data - acc_min
largest_profit = max(profit)
print('----- b) -----')
print('The largest profit which could have been made with one transaction is: ', largest_profit)


# c)
t_sell = np.where(data-acc_min == largest_profit)[0][0]
t_buy = np.where(data == acc_min[t_sell])[0][0]
# print(t_buy, t_sell)
plot_min_max(t_buy, t_sell, data)
plt.show()


# d)
print('\n----- d) -----')
rnd = np.int_(np.random.rand(50) * 100)
print('Random array with 50 values between 0 and 100:')
print(rnd)
bigger_than_right = rnd > np.roll(rnd, -1)
bigger_than_left = rnd > np.roll(rnd, 1)
bigger_than_both = bigger_than_right & bigger_than_left

loc_max = (rnd[1:-1])[bigger_than_both[1:-1]]  # The slicing with [1:-1] is done to ignore the border cases
print('All local maxima of this array:')
print(loc_max)
