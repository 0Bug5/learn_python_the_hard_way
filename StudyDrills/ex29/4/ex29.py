print('''
Question:

4. Can you put other boolean expressions from Exercise 27 in the if-statement? Try it.

Answer:

[+] Yep.
''')

print("#" * 30, "\n")

people = 1 ==  1 and not(True or False)
cats = False
dogs = not(True and False)


if people != cats:
    print("Too many cats! The world is doomed!")

if people < cats:
    print("Not many cats! The world is saved!")

if people or dogs:
    print("The world is drooled on!")

if people and dogs:
    print("The world is dry!")


dogs += 5

if people or not(dogs):
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people and not(False or dogs):
    print("People are dogs.")

print("#" * 30, "\n")