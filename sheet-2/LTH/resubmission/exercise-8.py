# ------------------------------------------------------------------------------

# Sheet 2 Exercise 8

# Niklas Markert - 1611460 / bt70985
# Lukas Thiersch - 1607110 / bt708626

# ------------------------------------------------------------------------------

# 1) Ask the user for an integer number between 1 and 100 and store the
# information in an integer variable z. (You do not have to verify
# whether a valid number was entered.) Multiply z by 9 and store the
# result in z.

z = int(input('Please input a number between 1 and 100: '))
z *= 9

# ------------------------------------------------------------------------------

# 2) Calculate the sum of digits of z and save the result in a variable.
# Hint: To do this, you can cast z to a string. Then iterate over that string
# to get the respective digits.
# (If you cannot solve this part, assume that the sum of digits is 9 in
# the following.)

z_as_str = str(z)

sum_of_digits = 0
for c in z_as_str:
    sum_of_digits += int(c)

# ------------------------------------------------------------------------------

# 3) Check whether the sum of digits is odd. If it is, do nothing. If it is not,
# divide the sum of digits by 2.

if sum_of_digits % 2 == 0:
    sum_of_digits /= 2

# ------------------------------------------------------------------------------

# 4)  Square the result of step 3), then add 14 and finally, divide by 5.
# Print the final result to screen.

sum_of_digits_final = (sum_of_digits ** 2 + 14) / 5
print(sum_of_digits_final)

# ------------------------------------------------------------------------------

# Observation: The result is always 19.
# Explanation: If the sum of all digits of a number is divisible by 9 the number
# itself is divisible by 9, thus the sum of digits calculated in 2) is always
# divisible by 9. The highest sum of digits we could get (not necessarily
# divisible by 9) is the sum of the digits 9, 9, and 8, because 100*9=900 is
# the biggest number than can result in 1) and thus 999 is not possible.
# The sum of 8, 9 and 9 is 26, which is smaller then 27 (3*9), thus the only
# possible results of 2) are 9 and 18. 18 is filtered out in 3) because it is
# not odd and gets divided by 2. So in the end we always end up with 9 after
# step 3).
# In step 4) we just calculate a result with 9 ((9^2 + 14) / 5) and get 19.

# ------------------------------------------------------------------------------

