# ------------------------------------------------------------------------------

# Sheet 1 Exercise 3

# Niklas Markert - 1611460 / bt70985
# Lukas Thiersch - 1607110 / bt708626

# ------------------------------------------------------------------------------

# a) Why does this expression cause an error? How can you fix it?
# 'I have eaten ' + 25 + ' peas.'

# In this example an error occurs because you can only concat string but 25 is
# an integer. The easiest fix would be to write '25' but that wont aid you
# if you want to concat strings with dynamic values. In this case we can use
# str() like so:
# 'I have eaten ' + str(25) + ' peas.'

# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
