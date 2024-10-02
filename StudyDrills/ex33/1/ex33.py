# Study Drills

# QUESTION:

    # 1. Convert this while-loop to a function that you can call, and replace 6 in the test (i < 6) with avariable.

# ANSWER:

############################### BEFORE CONVERSION ###############################
# i = 0
# numbers = []

# while i < 6:
#     print(f'\nAt the top i is {i}\n')
#     numbers.append(i)

#     i = i + 1
#     print('Numbers is now: ', numbers, '\n')
#     print(f'At the bottom i is {i}\n')
#     print('===============Next=================')


# print('The Numbers: ')
# for num in numbers:
#     print(num)

############################### AFTER CONVERSION ###############################
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

drills(6)