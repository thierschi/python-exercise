# ------------------------------------------------------------------------------

# a) What does inf mean? When does it occur in Python?

# The abbreviation inf stands for infinity. While it is technically possible
# represent infinity because integers or data stored in a length of bits
# is limited by the length of bits and is therefore not infinite, you can
# represent infinity in python with float('inf') or float('-inf').
# Pythons maths module contains a value for it too: math.inf

# ------------------------------------------------------------------------------

# b) The expression 3 != 3 is of boolean type.
# Which values can boolean variables have?

# Boolean values in python have two possible values that they can hold:
#   - true
#   - false

# ------------------------------------------------------------------------------

# c) Write a Python script that asks for two numbers and stores them in the
# variables x and y, respectively. Make sure that x and y are of type float.
# The script should then check whether x equals y. Why is the following code
# not a good idea to do so? Provide a better solution.
# x == y

# Comparing twi floats with == is generally not a good idea, because floating
# point numbers are represented as approximations of real numbers (IEEE)
# Comparing the numbers with == would only ever return true if both numbers
# are exactly equal.
# The problem is that when you do arithmetic with floating points you can get
# some weird results. For example:
#   The result of the expression 60.34 - 28.58 is 31.760000000000005
# If we would check for equality with 31.76 with == we would get false, although
# we can consider them equal for most cases.
#
# The following script checks 'near equality'

def are_floats_nearly_equal(a, b):
    # We check if the percentage of the deviation between a, b
    # is less than the tolerated deviation
    tolerated_deviation = 0.0001
    return abs((a - b) / b) < tolerated_deviation


f1 = float(input('Please provide the first floating point number: '))
f2 = float(input('Please provide the second floating point number: '))

print("Result of comparison: ", are_floats_nearly_equal(f1, f2))

# ------------------------------------------------------------------------------
