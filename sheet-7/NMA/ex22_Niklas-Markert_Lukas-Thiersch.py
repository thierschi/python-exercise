# ------------------------------------------------------------------------------

# Sheet 7 Exercise 20

# Niklas Markert - 1611460 / bt70985
# Lukas Thiersch - 1607110 / bt708626

# ------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### Important! If you are NOT using JupyterLab, comment the next line with #.
#%matplotlib inline

# a)

df = pd.read_csv('./ex22_data.csv', index_col='order')



# b)

df['sum'] = df[['Problem 1', 'Problem 2', 'Problem 3', 'Problem 4', 'Problem 5', 'Problem 6']].sum(axis=1)

print('--------- a) / b) ---------')
print('The head of the dataframe df, after the column sum got add:')
print(df.head())

# Plot
L = [17,24,23,23,22,21,31,17,25,16,30,20,21,20,30,14,16,28,10,11,20,
     16,26,27,31,26,19,12,12,19,23,17,24,19,12,24,25,15,33,23,13,23,
     25,21,18,15,25,13,18,18,18,28,19,24,24,14,19,15,20,30,21,12,17,
     14,20,15,14,24,28,27,24,25,12,17,18,18,18,18,26,23,22,27,22,15,
     32,30,18,22,28,18,11,7,15,24,23,27,24,24,17,22]

plt.hist(df['sum'])
plt.title('Point distribution')
plt.xlabel('points')
plt.ylabel('number (of persons)')
plt.show()


# c)

best_five_perc = df[df['sum'] >= df['sum'].quantile(.95)]
best_five_perc = best_five_perc.sort_values(by='sum', ascending=False)[['First name', 'Last name']]

print('\n----------- c) -----------')
print('The best 5% students:')
print(best_five_perc)


# d)

error_lines = df[(df['Problem 1'] > 8) | (df['Problem 2'] > 7) | (df['Problem 3'] > 7) | (df['Problem 4'] > 6)
                 | (df['Problem 5'] > 8) | (df['Problem 6'] > 7)]

print('\n----------- d) -----------')
print('The rows in which at least one cell contains more points than attainable:')
print(error_lines)


# e)

perc_less_33 = len(df[df['Problem 1']/8 < 0.33]) / len(df)

print('\n----------- e) -----------')
print('The percentage of students with less than 33% of points in Problem 1 is:')
print(perc_less_33)
