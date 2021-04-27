# ------------------------------------------------------------------------------

# Sheet 3 Exercise 12

# Niklas Markert - 1611460 / bt70985
# Lukas Thiersch - 1607110 / bt708626

# ------------------------------------------------------------------------------

# a) What happens to variables in a local scope when the function call returns?

# When the function call returns the local scope variable is getting removed
# from memory, thus it is only accessible from the point where it gets
# declared until the point where the function returns.

# ------------------------------------------------------------------------------

# b)  Write a function collatz(int_number) that takes as parameter an integer
# int_number. If int_number is even, then the function should print and return
# int_number // 2. If int_number is odd, then the function should print and
# return 3 * int_number + 1. Then let a user type in an integer number and store
# it in a variable num. Call the collatz function on num and save the result in
# the variable num. Keep doing this until the collatz function returns the value
# 1. Hint: Use a while loop for the second part.

def collatz(int_number):
    new_number = 0

    if int_number % 2 == 0:
        new_number = int_number // 2
    else:
        new_number = 3 * int_number + 1

    print(new_number)
    return new_number


num = int(input("Type a number: "))

while num != 1:
    num = collatz(num)

# ------------------------------------------------------------------------------
