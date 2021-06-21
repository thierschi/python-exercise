# ------------------------------------------------------------------------------

# Sheet 8 Exercise 23 - Resubmission

# Niklas Markert - 1611460 / bt709885
# Lukas Thiersch - 1607110 / bt708626

# ------------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------

# GENERAL NOTE regarding the question NMA asked in the e-learning forum:
# We interpret the data as only one discovered planet per row.

# ------------------------------------------------------------------------------

# a) Import the csv file and display only the first five elements.

df = pd.read_csv('ex23_data.csv')
print('a. First 5 elements of the data:\n', df[:5], '\n')

# ------------------------------------------------------------------------------

# b) Plot a histogram that displays the number of planets discovered (“y axis”)
# depending on the year of discovery (“x axis”). One bin should represent one year.

plt.hist(df['year'], bins='auto')
plt.show()

# ------------------------------------------------------------------------------

# c) How many different methods are listed in the data frame?

print('c. Count of unique methods:', len(df['method'].unique()), '\n')

# ------------------------------------------------------------------------------

# d) What is the largest orbital period?

print('d. Largest orbital period:', df['orbital_period'].max(), '\n')

# ------------------------------------------------------------------------------

# e) Display the number of planets that have been discovered by each method.

grouped_by_method = df.groupby(by='method')

print('e. Planets discovered by method:')
for name, group in grouped_by_method:
    print(len(group), 'planets were discovered by', name)
print()

# ------------------------------------------------------------------------------

# f)  Between 1989 and 1992, were there any years with no new planets discovered
# and if yes, which years?

years_between = df.loc[df['year'] >= 1989].loc[df['year'] <= 1992]
years_without = []
for i in range(1989, 1992):
    if len(df.loc[df['year'] == i]) == 0:
        years_without.append(i)

print('f. Years without discovery:\n', years_without, '\n')

# ------------------------------------------------------------------------------

# g) Create a scatter-plot that shows the distance of the planets with respect
# to the year of discovery.

plt.scatter(df['year'], df['distance'])
plt.show()

# What is the general trend?
# Over all more distant planets are being discovered as time progresses.

# ------------------------------------------------------------------------------
