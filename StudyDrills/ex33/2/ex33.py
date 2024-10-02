# Study Drills

# QUESTION:

    # 2. Use this function to rewrite the script to try different numbers.

# ANSWER:


def drills(loopNum):
    i = 0
    numbers = []

    while i < loopNum:
        print(f'\nAt the top i is {i}\n')
        numbers.append(i)

        i = i + 1
        print('Numbers is now: ', numbers, '\n')
        print(f'At the bottom i is {i}\n')
        print('===============Next=================')


    print('The Numbers: ')
    for num in numbers:
        print(num)

    return loopNum # wnn zai koma zuwa loopNum variable dake wajen fnx.

loopNum = int(input('\nEnter a Number to loop: '))

drills(loopNum)