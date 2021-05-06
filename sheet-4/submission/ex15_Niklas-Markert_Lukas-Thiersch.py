# ------------------------------------------------------------------------------

# Sheet 4 Exercise 15

# Niklas Markert - 1611460 / bt70985
# Lukas Thiersch - 1607110 / bt708626

# ------------------------------------------------------------------------------

import random
import logging

# a) ---------------
# What assert does is, it gets a bool-expression and evaluates this. If the expression got evaluated true the code
# continues like normal, but if it evaluates false it raises an AssertionError with a given message.
#
# assert is very useful in two situations:
#   - If you want to debug your code, you can use assert to say: "If there got no exception raise, the asserted
#     statement must be true, from that point on". That helps you to exclude some possible error sources.
#   - If for example your written function is also used by others, who don't know the code, you can use assert at the
#     beginning of the function to secure that only correct values got entered, so your function works right
#
# For example: You have a function foo that should take two integers and calculates their sum times two. Because the
#   used operands can correctly be used on other types, it wouldn't throw an error by itself when you input two strings
#   there.
#   Now imagine the situation, that someone uses this function and doesn't know exactly what this does, but knows he
#   need the solution for his next step. When he now enters, maybe by mistake, his two ints as strings, the function
#   by itself would throw no exception, so he thinks it all went right and casts the string output to int because he
#   needed an int. But now he got a wrong int value, because the operands are different on ints and strings.
#   So with the assert, he gets an error as soon as he input string values to foo, so the user notice that, maybe after
#   reading the values from a file, he has to cast them to int first, in order to use the function right.
# ------------------


def foo(x, y):
    assert type(x) == int, 'First argument is not of required type int'
    assert type(y) == int, 'Second argument is not of required type int'
    return (x+y)*2


try:
    print(foo(2, 3))
    print(foo('2', '3'))
except AssertionError as e:
    print(e)


# b) ---------------
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


def main():
    guess = ''
    while guess not in ('right', 'left'):  # Loop for the first guess
        print('Guess in which hand is a present! Enter right or left:')
        guess = input()
        logging.debug('User guessed: ' + guess)

    hand = random.randint(0, 1)  # 0 is left, 1 is right
    hand = 'left' if hand == 0 else 'right'  # Convert the int value (0, 1) to the corresponding string value
    logging.debug('The correct guess would be: ' + hand)

    if hand == guess:  # See if the first guess is correct
        print('You got it, here is the present!')
    else:
        print('Wrong! Guess again!')
        guess = ''
        while guess not in ('right', 'left'):  # Loop for the second guess
            print('Guess in which hand is a present! Enter right or left:')
            guess = input()
            logging.debug('User guessed: ' + guess)

        if hand == guess:  # See if the second guess is correct
            print('You got it, here is the present!')
        else:
            print('Nope! You do not seem to be very good at this game.')


logging.debug('Start of program')
if __name__ == '__main__':
    main()
    logging.debug('End of program')