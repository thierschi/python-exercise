# ------------------------------------------------------------------------------

# a) Does the following code produce an error?
# If yes, why? If no, what is the output?
# 1 + 2 + - 3

# No it does not produce an error: Using + - is just like subtracting
# right away as in normal maths.
# Output is 0

# ------------------------------------------------------------------------------

# b) Does the following code produce an error?
# If yes, why? If no, what is the output?
# 1 + 2 + * 3

# Yes it does produce an error: The asterisk operator tries to unpack 3
# which is not possible. Furthermore is unpacking not possible in arithmetic
# expressions.

# ------------------------------------------------------------------------------

# c) What is the difference between 1 and 1.0?

# Python is not strongly typed, that means you do not have to declare the
# type of a variable. That implies that the compile has to guess or rather
# derive the type from the given value.
#   => 1 implies an integer
#   => 1.0 implies a floating point number

# ------------------------------------------------------------------------------

# d) What is the type of the variable tempvar?
# tempvar = 1 / 2.0 + 1

# The type of tempvar is float becaus division returns floating point numbers

# ------------------------------------------------------------------------------

# e) What does the variable temp contain after the following code runs and why?
# Hint: Output temp at the end.
# temp = 11
# temp *= 2
# temp - 2

# After execution of these instructions temp holds the value 22:
# temp = 11 <- temp is assigned 11
# temp *= 2 <- temp is assigned twice the value of temp (temp * 2)
# temp - 2 <- This has no effect on temp. The expression itself returns 20,
#             however the value is never assigned to anything

# ------------------------------------------------------------------------------
