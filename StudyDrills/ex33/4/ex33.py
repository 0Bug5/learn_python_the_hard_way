# QUESTION:
    # 4. Rewrite the script again to use this function to see what effect that has.

# ANSWER:

style = '=' * 40

def drill(loopNum, increment):
    i = 0
    numbers = []

    while i < loopNum:
        print(style)
        print('At the top i is', i)
        numbers.append(i)

        i = i + increment
        print('Number is Now: ', numbers)
        print('At the bottom i is', i)

    print(style + '\n')
    print('Numbers Are: \n')
    for i in numbers:
        print('\t==> ', i, ' <==\n')

    return loopNum

loopNum = int(input('\nEnter a Number to Loop: '))
increment = int(input('Enter a Number to Increment By: '))

drill(loopNum, increment)