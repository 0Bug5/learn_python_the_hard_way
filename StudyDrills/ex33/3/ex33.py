# Study Drills

# QUESTION:

    # 3. Add another variable to the function arguments that you can pass in that lets you change the +1 on line 8 so you can change how much it increments by

# ANSWER:


def drills(loopNum, increment):
    i = 0
    numbers = []

    while i < loopNum:
        print(f'\nAt the top i is {i}\n')
        numbers.append(i)

        i = i + increment
        print('Numbers is now: ', numbers, '\n')
        print(f'At the bottom i is {i}\n')
        print('===============Next=================')


    print('The Numbers: ')
    for num in numbers:
        print(num)

    return loopNum # wnn zai koma zuwa loopNum variable dake wajen fnx.

loopNum = int(input('\nEnter a Number to loop: '))
increment = int(input('\nEnter a Number to increment By: '))

drills(loopNum, increment)