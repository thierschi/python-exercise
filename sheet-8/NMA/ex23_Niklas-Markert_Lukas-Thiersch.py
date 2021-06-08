# ------------------------------------------------------------------------------

# Sheet 8 Exercise 23

# Niklas Markert - 1611460 / bt70985
# Lukas Thiersch - 1607110 / bt708626

# ------------------------------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------
# We interpreted the data so, that each row represents exactly one discovered planet
# ---------------------

# a)
data = pd.read_csv('ex23_data.csv')
print('----- a) -----')
print(data[:5])


# b)
plt.hist(data['year'], bins='auto')
plt.show()


# c)
print('\n----- c) -----')
amount_methods = len(data['method'].unique())
print('There are', amount_methods, 'different methods listed in the dataframe.')


# d)
print('\n----- d) -----')
largest_orb_period = max(data['orbital_period'])
print('The largest orbital period in the dataframe is:', largest_orb_period)


# e)
print('\n----- e) -----')
groups = data.groupby(by='method')
for name, group in groups:
    print(name + ':', len(group))

# f)
print('\n----- f) -----')
years = np.arange(1989, 1993)
print('The years between 1989 and 1992 where no new planets were discovered:')
print(years[np.logical_not(np.isin(years, data['year']))])

# g)
plt.scatter(data['year'], data['distance'])
plt.show()
# ---------------------
# The general trend is, that the distance to the new discovered planets increases over time.
# ---------------------
