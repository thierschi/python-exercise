# ------------------------------------------------------------------------------

# Sheet 4 Exercise 14 - Resubmission

# Niklas Markert - 1611460 / bt70985

# ------------------------------------------------------------------------------

import turtle
import logging

logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')


def fct(length, counter):           # function fct is defined with parameters
                                    # lenght and counter

    logging.debug("Function fct(length, counter) called with length = "
                  + str(length) + " and counter = " + str(counter) + ".")

    if length > 5:                  # check if length is greater 5
                                    # if true the following code is
                                    # run
                                    # --> turtle stops drawing if a branch
                                    # would be shorter than 5

        turtle.forward(length)      # the turtle moves the distanced saved in
                                    # length forward

        turtle.right(20)            # the turtle turns right 20 degrees

        fct(length-20, counter+1)   # recursive call to fct with lenght-20
                                    # and incremented counter

                                    # --> Until this point the turtle draws
                                    # "the right branch(es)" recursively
                                    # after this point the left branches
                                    # get drawn

        turtle.left(40)             # the turtle turns 40 degrees left

        fct(length-20, counter+1)   # recursive call of fct with lenght-20
                                    # and incremented counter

        turtle.right(20)            # the turtle turns right 20 degrees

        turtle.backward(length)     # the turtle goes backwards length distance
                                    # --> it is now at the point, where
                                    # it was before the call to fct

    logging.debug("Function fct(length, counter) is finished with length = " + str(length) + " and counter = "
                  + str(counter) + ".")


def main():
    logging.debug("Function main() called. No args.")
    counter, length = 0, 85         # set counter to 0 and length to 85
    turtle.left(90)                 # this is the first call to the turtle,
                                    # the following things happen:
                                    # - The turtle window is opened
                                    # - The turtle is turned left 90 degrees
                                    # (the starting point of the turtle is
                                    # 0 degrees -> facing east)

    turtle.color("green")           # the turtle's drawing color is set to green
    fct(length, counter)            # function fct is called with params
                                    # length and counter

    turtle.done()                   # prevents the window from closing once
                                    # drawing is finished.

    logging.debug("Function main() is finished. No args.")

logging.debug('Start of program')	# debug message for the start of the program
# see https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    main()							# call function main()
logging.debug('End of program')		# debug message for the end of the program

# ------------------------------------------------------------------------------

# a) Find out what each code line does by experimenting with the code.
# Then comment every uncommented line of code.

# For the answer: See code above.

# ------------------------------------------------------------------------------

# b) Log each function call of fct and main including the arguments. For example,
# each time a function fun(x) is called, a debug message similar to “Function
# fun(x) called with x = ...” should appear using the logging.debug() function.
# Do not use the print() function.

# For the answer: See code above.

# ------------------------------------------------------------------------------

# c) In a similar way, at the end of each function, output a debug message
# stating that the function is finished (with parameters included). Run the
# code with these debug messages and briefly comment on what you observe
# regarding the function calls.

# Observation:
# We can essentially see the call stack of this program with all it's
# recursive calls. It is growing until a branch would be shorter than
# 5 and then we see one or more "endings" where the turtle than returns.

# ------------------------------------------------------------------------------

# d) What data types and what sign should the arguments length and counter have?
# What do you get as a result and how does the program produce it? Justify your
# answer by explaining (the structure of) the program.

# Counter: The value and sign of counter is not relevant,because - besides
# passing the value of counter along - it's value gets never used. The
# type however is somewhat important, because we increment it by one when
# passing it to the recursive call and this would throw an error if it was
# not a number or float. The only thing that is changing with a different
# value for counter is our debug output.

# Length: The length's type must be a number as moving the turtle forward
# by a string or boolean value would not make sense and ultimately
# result in errors. The length's value and sign however are somewhat
# important: If the length is < 5 or negative the turtle won't draw anything
# because of the check in fct that checks if length is smaller 5. Although
# if you want the turtle to do nothing you can pass small / negative values.

# ------------------------------------------------------------------------------
