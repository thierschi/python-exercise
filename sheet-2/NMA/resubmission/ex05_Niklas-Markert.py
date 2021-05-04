# ------------------------------------------------------------------------------

# Sheet 2 Exercise 5 - Resubmission

# Niklas Markert - 1611460 / bt70985

# ------------------------------------------------------------------------------

X = float(input('Quantity of enzyme X:'))
Y = float(input('Quantity of enzyme Y:'))
Z = float(input('Quantity of enzyme Z:'))
epsilon = 1E-4
if abs(X-Y) < epsilon:
    print('Test passed.')
else:
    print('DANGER!')

# Changes:
# l.10 - 12: The input should only be cast to float and not to integer, because the exercise says '[..] not necessarily
#            integer [..]', so casting the values to integer would be wrong. And in this case it also makes no
#            difference if you first cast to float and than int or the other way round.
# l.13: Changed to 1E-4 because the Exercise says e:=10^-4 which is the same as 1E-4.
# l.14: Take the absolute amount [abs(..)] of X-Y, because otherwise you get an negative value, when Y is bigger than X.
# l.14: It has to be <, because you want to check if X and Y differ in less than e not in more than e.
# l.14: ':' was missing in the end, the python syntax requests the ':'.
# l.15: The code block after an 'if' statement has to be indented.
# l.16: ':' was missing after the 'else', the python syntax requests the ':'.
