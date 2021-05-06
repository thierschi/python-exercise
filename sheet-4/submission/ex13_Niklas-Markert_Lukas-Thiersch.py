# ------------------------------------------------------------------------------

# Sheet 4 Exercise 13

# Niklas Markert - 1611460 / bt70985
# Lukas Thiersch - 1607110 / bt708626

# ------------------------------------------------------------------------------

import traceback

# a)
try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError:
    print('[Error] No such file')
    f = open('errors.txt', 'w')
    f.write(traceback.format_exc())
    f.close()


# b)
try:
    x = float(input('Enter a number:'))
    y = float(input('Enter a number:'))
    print(y, '/', x, '=', y/x)
except ValueError:
    print('[Error] Given input can\'t be converted to float')
except ZeroDivisionError:
    print('[Error] Division with zero is not allowed')


# c)
def sum_pair(L):
    sum_pair_list = []
    try:
        for i in range(len(L)):
            try:
                sum_pair_list.append(L[i]+L[i+1])
            except TypeError:
                print('[Error] Operand + is not supported for ' + str(type(L[i])) + ' and ' + str(type(L[i+1])))
            except IndexError:
                print('[Error] Addressed index is out of bounds')

    except TypeError:
        print('[Error] Object ' + str(L) + ' with type ' + str(type(L)) + ' has no len()')

    print('Pairwise sum:', sum_pair_list)


sum_pair([10, 5, 76, 12, 3, 9])
sum_pair([10, 5, '7', 12, 3, 9])
sum_pair(7.9)