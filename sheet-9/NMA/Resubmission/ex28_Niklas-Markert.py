# ------------------------------------------------------------------------------

# Sheet 9 Exercise 28 - Resubmission

# Niklas Markert - 1611460 / bt709885

# ------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('ex28_data.csv', header=0, index_col='RespondentID', dtype={'RespondentID': 'Int64'})

# ------------------------------------------------------------------------------

# a) Plot a histogram of the age of all respondents who have seen at least one
# Star Wars film according to the seen_any_film column. Plot a histogram of the
# age of all respondents who have seen all of the latter episodes (IV to VI) but
# none of the first three (I to III). What observation do you make?

seen_any = df[df['seen_any_film'] == 'Yes']

seen_any['age'].hist()
plt.show()

seen_latter = df[
    (df['seen_ep1'] == 'No')
    & (df['seen_ep2'] == 'No')
    & (df['seen_ep3'] == 'No')
    & (df['seen_ep4'] == 'Yes')
    & (df['seen_ep5'] == 'Yes')
    & (df['seen_ep6'] == 'Yes')
]

seen_latter['age'].hist()
plt.show()

# Observation:

# We can observe that in all ages people have seen at least one movie (with
# a bit more mid-age people (45-60) than younger and older).
# But what we can observe that substantially less people in ages 18-29 have
# seen only episodes 4-6 which makes sense as ep 4-6 were the first ones that
# were released back in 1977-1983 which ago about 44 years ago.

# ------------------------------------------------------------------------------

# b) How many of those who have seen at least one of the six films according
# to the seen_any_film column are unfamiliar (“Unfamiliar (N/A)”) with at
# least one character? Give the absolute number and the percentage.

not_like_one_char = seen_any[
    (seen_any['like_char1'] == 'Unfamiliar (N/A)')
    | (seen_any['like_char2'] == 'Unfamiliar (N/A)')
    | (seen_any['like_char3'] == 'Unfamiliar (N/A)')
    | (seen_any['like_char4'] == 'Unfamiliar (N/A)')
    | (seen_any['like_char5'] == 'Unfamiliar (N/A)')
    | (seen_any['like_char6'] == 'Unfamiliar (N/A)')
    | (seen_any['like_char7'] == 'Unfamiliar (N/A)')
    | (seen_any['like_char8'] == 'Unfamiliar (N/A)')
    | (seen_any['like_char9'] == 'Unfamiliar (N/A)')
    | (seen_any['like_char10'] == 'Unfamiliar (N/A)')
    | (seen_any['like_char11'] == 'Unfamiliar (N/A)')
    | (seen_any['like_char12'] == 'Unfamiliar (N/A)')
    | (seen_any['like_char13'] == 'Unfamiliar (N/A)')
    | (seen_any['like_char14'] == 'Unfamiliar (N/A)')]

print("Number of people that have seen any film",
      "but are not familiar with at least on characters:",
      len(not_like_one_char))
print("In percent:", (len(not_like_one_char) / len(seen_any)) * 100, "%")

# ------------------------------------------------------------------------------

# c) How many respondents have seen all six films? Determine which film is the
# least favorite according to the respondents who watched all six films. To this
# end, calculate the column-wise mean and the median for the required columns
# (and rows). The respondents ranked the films from “1” (best) to “6” (worst).

seen_all = df[
    (df['seen_ep1'] == 'Yes')
    & (df['seen_ep2'] == 'Yes')
    & (df['seen_ep3'] == 'Yes')
    & (df['seen_ep4'] == 'Yes')
    & (df['seen_ep5'] == 'Yes')
    & (df['seen_ep6'] == 'Yes')
]

print("Number of people that have seen all six movies:", len(seen_all))

print("Mean of all six episodes' ranks:")
print('Ep. 1:', seen_all['rank_ep1'].mean())
print('Ep. 2:', seen_all['rank_ep2'].mean())
print('Ep. 3:', seen_all['rank_ep3'].mean())
print('Ep. 4:', seen_all['rank_ep4'].mean())
print('Ep. 5:', seen_all['rank_ep5'].mean())
print('Ep. 6:', seen_all['rank_ep6'].mean())

print("Median of all six episodes' ranks:")
print('Ep. 1:', seen_all['rank_ep1'].median())
print('Ep. 2:', seen_all['rank_ep2'].median())
print('Ep. 3:', seen_all['rank_ep3'].median())
print('Ep. 4:', seen_all['rank_ep4'].median())
print('Ep. 5:', seen_all['rank_ep5'].median())
print('Ep. 6:', seen_all['rank_ep6'].median())

# ------------------------------------------------------------------------------

# d) Which character is liked least by men (average score)? Which character is
# liked most by women (average score)? (Instead of the character name you may
# the column name, e.g., like_charN.)

res_male = df[df['gender'] == 'Male'].fillna(0)
res_female = df[df['gender'] == 'Female'].fillna(0)

avg_male = {}
avg_female = {}

for i in range(1, 15):
    char = 'like_char' + str(i)
    char_col = pd.to_numeric(res_male[res_male[char] != 'Unfamiliar (N/A)'][char], errors='coerce').fillna(0)
    mean = char_col.mean()
    if mean not in avg_male:
        avg_male[mean] = [char]
        continue
    avg_male[mean].append(char)

for i in range(1, 15):
    char = 'like_char' + str(i)
    char_col = pd.to_numeric(res_female[res_female[char] != 'Unfamiliar (N/A)'][char], errors='coerce').fillna(0)
    mean = char_col.mean()
    if mean not in avg_female:
        avg_female[mean] = [char]
        continue
    avg_female[mean].append(char)

lowest_score_male = np.array(list(avg_male.keys())).min()
highest_score_female = np.array(list(avg_female.keys())).max()

print("Least popular character amongst men:", avg_male[lowest_score_male])
print("Most popular character amongst women:", avg_female[highest_score_female])
