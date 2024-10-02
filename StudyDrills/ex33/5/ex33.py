# QUESTION:
     # 5. Write it to use for-loops and range. Do you need the incrementor in the middle anymore? What happens if you do not get rid of it?

# ANSWER:

style = '=' * 40
numbers = []

for i in range(0, 6):
    print(style)
    print('At the top i is ', i)
    numbers.append(i)

    # IDAN BA KAYI COMMENTING WANN BA TO ZAI INCREMENTING! RESULT DIN ZAI KASANCE KAMAR HAKA.

    # At the top i is  0
    # Number is Now:  [0]
    # At the bottom i is 1 

    i = i + 1

    print('Number is Now: ', numbers)
    print('At the bottom i is', i, '\n')

print('Number Are: ')
for i in numbers:
    print('\t[+] ', i, ' [+]')

print('\n###################### AFTER THE COMMENT ########################\n')

style = '=' * 40
numbers = []

for i in range(0, 6):
    print(style)
    print('At the top i is ', i)
    numbers.append(i)

    # IDAN KAYI COMMENTING WANN TO BA ZAI INCREMENTING BA! RESULT DIN ZAI KASANCE KAMAR HAKA.

    # At the top i is  0
    # Number is Now:  [0]
    # At the bottom i is 0

    # i = i + 1 

    print('Number is Now: ', numbers)
    print('At the bottom i is', i, '\n')

print('Number Are: ')
for i in numbers:
    print('\t[+] ', i, ' [+]')