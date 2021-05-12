# ------------------------------------------------------------------------------

# Sheet 5 Exercise 18

# Niklas Markert - 1611460 / bt70985
# Lukas Thiersch - 1607110 / bt708626

# ------------------------------------------------------------------------------

# Your friend needs help after having organized a gift list as a dictionary:

gift_dict = {'Playmobil': 'Alf',
             'Slingshot': 'Bart ',
             'Guitar': 'Lisa',
             'Earrings ': 'Nina',
             'Playstation': 'Maya',
             'Books': 'Lisa',
             'TV': 'Alf',
             'Money': 'Alf',
             'Joghurt': 'Nobody'}

# The presents were stored as keys, while the persons were stored as values.

# ------------------------------------------------------------------------------

# a) Why is this not a good idea if each person is to receive exactly one gift?

# This is a bad idea because the logic is the other way around. Normally a
# person can get one gift, but a (type of gift, e.g. money) can be gifted to
# multiple persons (e.g. Alf and Maya could both get Playmobil). With this
# list on the the other hand a gift can be gifted just once (because dict keys
# must be unique) but persons can receive multiple gifts. Hence it would be
# better to use the persons as a key for the dict.

# ------------------------------------------------------------------------------

# Before going shopping, your friend noticed that a person can receive two or
# more gifts this way. However, each person is to receive exactly one gift. At
# the same time, no person should be left empty-handed. Hence, it is important
# to find all persons who are in the dictionary more than once. Use the above
# dictionary to test whether your program works.

# ------------------------------------------------------------------------------

# b) Output all names of those who will receive two or more gifts and output
# the exact number of presents for each of these names.

# and c) In addition, for all persons from b), output a list of all keys (gifts)
# that this person would receive. You may combine this task part with b).

better_dict = {}

for gift, person in gift_dict.items():
    if better_dict.get(person) is None:
        better_dict[person] = [gift]
        continue
    better_dict[person].append(gift)

for person, gifts in better_dict.items():
    if len(gifts) > 1:
        print("Spoiled", person, "gets the following", len(gifts), "gifts:")
        for gift in gifts:
            print("\t-", gift)
        print()

# ------------------------------------------------------------------------------
