# ------------------------------------------------------------------------------

# Sheet 9 Exercise 27

# Niklas Markert - 1611460 / bt709885
# Lukas Thiersch - 1607110 / bt708626

# ------------------------------------------------------------------------------

import numpy as np
import pandas as pd

df = pd.read_csv('ex27_data.csv', index_col='RespondentID', dtype={'RespondentID': 'Int64'})

# a)
for i in range(1, 7):
    key = 'seen_ep' + str(i)
    df[key] = np.where(pd.isnull(df[key]), 'No', 'Yes')


# b)
char_rating = {'Very unfavorably': -2,
               'Somewhat unfavorably': -1,
               'Neither favorably not unfavorably (neutral)': 0,
               'Somewhat favorably': 1,
               'Very favorably': 2}

for i in range(1, 15):
    key = 'like_char' + str(i)
    for desc, rating in char_rating.items():
        df[key] = np.where(df[key] == desc, rating, df[key])


# c)
print('----- c) -----')
# In this solution only respondents which answered both questions (fan_sw and fan_st) are considered
answered_both = df.dropna(axis=0, how='any', subset=['fan_sw', 'fan_st'])
fan_of_sw = answered_both['fan_sw'] == 'Yes'
fan_of_st = answered_both['fan_st'] == 'Yes'
no_fan = answered_both[np.logical_not(fan_of_sw | fan_of_st)]
print('Amount of respondents which are neither fan of the StarWars franchise nor the StarTrek franchise:', len(no_fan))
per_no_fan = len(no_fan)/len(answered_both)*100
print('Therefore are ' + str("%.2f" % per_no_fan) + '% of the respondents who answered both questions '
      'neither a fan of the StarWars nor the StarTrack franchise.')


# d)
print('\n----- d) -----')


def amount_of_films_seen(row):
    amount = 0
    for j in range(1, 7):
        amount += 1 if row['seen_ep'+str(j)] == 'Yes' else 0
    return amount


df['amount_films_seen'] = df.apply(amount_of_films_seen, axis=1)
sw_fans = df[df['fan_sw'] == 'Yes']
fan_exactly_one_film = sw_fans[sw_fans['amount_films_seen'] == 1]
per_one_film = len(fan_exactly_one_film)/len(sw_fans)*100
print(str("%.2f" % per_one_film) + '% of the StarWars fans have seen exactly one film.')
