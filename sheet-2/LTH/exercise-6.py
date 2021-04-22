# ------------------------------------------------------------------------------

# Sheet 2 Exercise 6

# Niklas Markert - 1611460 / bt70985
# Lukas Thiersch - 1607110 / bt708626

# ------------------------------------------------------------------------------

# The management of your company wishes to redesign workflows. There are four
# tasks A, B, C, and D. Task C cannot be completed until task A is completed.
# The management wants you to list all possible work sequences that take this
# into account. For example, (A, B, C, D) means that first task A, then B,
# then C, and finally D will be executed. An invalid sequence would be,
# e.g., (C, B, D, A).

# ------------------------------------------------------------------------------

# a) Check whether the script provided on e-Learning really only outputs
# valid workflows. If it does not, adjust the script accordingly.
# Comment on your changes.

# The changes that were made are marked with a comment "CHANGE A"
# The problem in the given code is that we are removing elements
# of a list whilst iterating over that list. That leads to
# undesired behaviour. In this case we were not iterating over
# all elements and that gave us wrong results in the end.
# The fix for this bug is that we iterate over a copy of the
# list and remove the elements of the original list.

# The code for both answers is below.

# ------------------------------------------------------------------------------

# b) Extend the script such that all valid workflows are not only printed on
# screen but also written to a file called valid_combinations.txt.

# Python gives us an easy way to write and read to files in the FS.
# We just have to open a file with open() and then we can write to it with write().
# After finishing our write operations, we can close the file again with close()

# Implementation: See write_list_to_file().

# ------------------------------------------------------------------------------

import itertools  # Required for generating all permuations


# Procedure that outputs all elements of a list one below the other:
def print_list(mylist):
    """Prints all elements of a list."""
    assert type(mylist) == list
    print('List has', len(mylist), 'elements:')
    for x in mylist:
        print(x)


def write_list_to_file(mylist):
    """Write list elements to file"""
    assert type(mylist) == list
    # Open file in 'append' mode
    file = open("valid_combinations.txt", 'a')
    file.write('List has ' + str(len(mylist)) + ' elements:\n')
    for x in mylist:
        file.write(str(x) + '\n')
    file.close()


# The following command creates a list of all possible permutations. Each element of this list is a tuple.
L = list(itertools.permutations(['A', 'B', 'C', 'D']))

print_list(L)  # Output list for checking purposes

L_copy = L.copy() # CHANGE
for x in L_copy: # CHANGE
    aIndex = x.index('A')  # position of 'A'
    cIndex = x.index('C')  # position of 'C'
    print(cIndex < aIndex, x)
    if cIndex < aIndex:  # If 'C' before 'A':
        L.remove(x)  # delete that element.
print_list(L)  # Print list.
write_list_to_file(L) # Wite list to file

# ------------------------------------------------------------------------------
