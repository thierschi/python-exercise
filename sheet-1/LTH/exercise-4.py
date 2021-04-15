# ------------------------------------------------------------------------------

# Sheet 1 Exercise 4

# Niklas Markert - 1611460 / bt70985
# Lukas Thiersch - 1607110 / bt708626

# ------------------------------------------------------------------------------

# a) What is []?

# In python square brackets denote a list. In particular [] is an empty list
# that is a list with length 0.

# ------------------------------------------------------------------------------

# b) Is this a valid list? Explain.
# LL = [1, 2, 3, 4, 'five', 6, 7]

# Yes this is a valid list. In python items in a list do not have to be the
# same data type.
# In this case we have a list with 6 integers and 1 string. This is valid.

# ------------------------------------------------------------------------------

# c) Consider the following list:
L = ['zz', 'yy', 'xx', 'ww', 'vv']

# 1) What does L[-1] evaluate to? What does L[:3] evaluate to?
L[-1] # evaluates to 'vv', because using a negative index returns the item
# at the position starting from the end of the list
L[:3] # evaluates to ['zz', 'yy', 'xx']:
#   You can slice with the [] operator in that case you can use it like so:
#   [start:end:step] -> start is the start of the slice
#                       end is the end of it (excluding)
#                       step is taking every nth element
# When writing :3 python assumes start to be 0.

# 2) How can you access the first element of the list?
# You can access the first item of a list with index 0:
L[0]

# 3) Delete the second last element.
# With del you can delete an item of a list. In this case it'd be:
del L[-2]

# 4) Add the element '11' at the beginning of the list.
# You can insert items to a list with {listname}.insert(index, item).
# In this case we would prepend the item '11' as follows:
L.insert(0, '11')

# ------------------------------------------------------------------------------
