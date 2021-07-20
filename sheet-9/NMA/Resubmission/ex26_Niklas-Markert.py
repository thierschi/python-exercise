# ------------------------------------------------------------------------------

# Sheet 9 Exercise 26 - Resubmission

# Niklas Markert - 1611460 / bt709885

# ------------------------------------------------------------------------------

import numpy as np
import pandas as pd

# a)
df = pd.read_csv('ex26_data.csv', index_col='RespondentID', dtype={'RespondentID': 'Int64'})


# b)
print('----- b) -----')
cols = ['seen_any_film', 'fan_sw']
for i in range(1, 7):
    cols.append('seen_ep' + str(i))
for i in range(1, 7):
    cols.append('rank_ep' + str(i))
for i in range(1, 15):
    cols.append('like_char' + str(i))
cols.extend(['first_shot', 'know_exp_univ', 'exp_univ_fan', 'fan_st', 'gender', 'age', 'h_income', 'education',
             'location'])
df.columns = cols

film_names = dict()
for i in range(1, 7):
    key = 'seen_ep' + str(i)
    film_names[key] = df.loc[:, key].iloc[0]
print('Dict for film names:')
print(film_names)

character_names = dict()
for i in range(1, 15):
    key = 'like_char' + str(i)
    character_names[key] = df.loc[:, key].iloc[0]
print('\nDict for character names:')
print(character_names)

df.drop(df.index[0], inplace=True)

# c)
print('\n----- c) -----')
respondents = len(df) 
print('Respondents in the data set:', respondents)
male = len(df[df['gender'] == 'Male'])
print('Amount of male respondents:', male)
female = len(df[df['gender'] == 'Female'])
print('Amount of female respondents:', female)
unknown = len(df.index[np.where(pd.isnull(df['gender']))[0]])
print('Amount of respondents who did not answer this question:', unknown)


