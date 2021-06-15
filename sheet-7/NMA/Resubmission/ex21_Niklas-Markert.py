# ------------------------------------------------------------------------------

# Sheet 7 Exercise 21 - Resubmission

# Niklas Markert - 1611460 / bt709885

# ------------------------------------------------------------------------------
import pandas as pd
import numpy as np

## 0) Import the associated csv file as a Pandas DataFrame and call it "df". Do not change the name of the csv file or its contents.
df = pd.read_csv('ex21_data.csv', index_col=0)

## 1) Display the number of valid elements (no NaN elements), the average, the standard deviation, and minima and maxima for each column.
# What is problematic about the column "z"?

print('Count of valid elements:\n', df.count())
print('Average per col:\n', df.mean())
print('Standard deviation per col:\n', df.std())
print('Min. of each col:\n', df.min())
print('Max. of each col:\n', df.max())

# Problematic about column z is that it contains inf values which produces a possibly meaningless average,
# because for that calculation an inf number has to be divided by a number which gives us infinity again.
# Also we cannot calculate a deviation.

## 2) Replace all +/-infinite values with NaN.
df = df.replace(np.inf, np.nan)
df = df.replace(np.NINF, np.nan)

## 3) Calculate (not by hand) how often NaN occurs in the DataFrame.
print('Count of NaN per col:\n', df.isna().sum())

## 4) Delete all rows that contain a NaN.
df = df.dropna()

## 5) Display the number of elements, the average, the standard deviation, and minima and maxima for each column.
# What has changed compared to 1)?
print('Count of valid elements:\n', df.count())
print('Average per col:\n', df.mean())
print('Standard deviation per col:\n', df.std())
print('Min. of each col:\n', df.min())
print('Max. of each col:\n', df.max())

# In contrast to 1) we now get usable (or rather values other than inf or NaN) as results for the standard deviation
# and average in column z because we dropped the cols that contained inf / nan values

## 6) Sort the DataFrame by the z column (descending).
df = df.sort_values(by='z', ascending=False)

## 7) For each column, output the row that contains the maximum of the column.
print('Dataframe sorted by z:\n', df)
print('Rows with max. x:\n', df[df['x'] == df['x'].max()])
print('Rows with max. y:\n', df[df['y'] == df['y'].max()])
print('Rows with max. z:\n', df[df['z'] == df['z'].max()])

## 8) Delete the z column in the DataFrame.
del df['z']

## 9) Add a new column with the value x+y and the label 'x+y' to the DataFrame.
df['x+y'] = df['x'] + df['y']
