# ------------------------------------------------------------------------------

# Sheet 3 Exercise 10

# Lukas Thiersch - 1607110 / bt708626

# ------------------------------------------------------------------------------

# The management of your company has run a lottery. Unfortunately, the
# implementation did not prevent one and the same person from registering
# more than once to increase winning chances, even though the conditions
# of participation prohibit it. You are given a list of all participants:

L = ['Lucas Sankt ', 'Phillipp Klug ', 'Alf Redo ', 'Klaudia Kaiser ',
     'Ute Beich ', 'Vanessa Trommler ', 'Lien Hsia ', 'Alf Redo ',
     'Alf Redo ', 'Ute Beich ']

# Your task is to remove all duplicate entries, so that every name appears
# only once. The end result should be a list.

# ------------------------------------------------------------------------------

# a) Write a Python script that completes the task without using the set
# datatype.


def get_unique_list_entries_without_set(old_list):
    old_list.sort()

    unique_list = []

    last_item = ''
    for current_item in old_list:
        if current_item != last_item:
            last_item = current_item
            unique_list.append(current_item)

    return unique_list

# ------------------------------------------------------------------------------

# b) Write a Python script (in the same file) that completes the task using
# the set datatype.


def get_unique_list_entries_with_set(old_list):
    helper_set = set(())
    for item in old_list:
        helper_set.add(item)

    new_list = list(helper_set)

    # Sorting is not an essential part of this algorithm
    # The purpose is to generate the same output as
    # the algorithm in a)
    new_list.sort()

    return new_list

# ------------------------------------------------------------------------------

# Testing both methods:

print("\nget_unique_list_entries_without_set:")
print(get_unique_list_entries_without_set(L))

print("\nget_unique_list_entries_with_set:")
print(get_unique_list_entries_with_set(L))
