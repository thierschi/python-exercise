# ------------------------------------------------------------------------------

# Sheet 2 Exercise 8

# Niklas Markert - 1611460 / bt70985
# Lukas Thiersch - 1607110 / bt708626

# ------------------------------------------------------------------------------
running = True
while running:
    # 1)
    while True:
        z = int(input('Enter an int value between 1 and 100: '))
        if z < 1 or z > 100:
            print('Your entered value isn\'t between 1 and 100!')
        else:
            break
    z *= 9

    # 2)
    x = 0
    for i in str(z):
        x += int(i)

    # 3)
    if x % 2 == 0:
        x = x / 2

    # 4)
    x = x * x
    x += 14
    x = x / 5

    print(x)

    running = input('Do you want to do this again? (y/n) ') == 'y'
