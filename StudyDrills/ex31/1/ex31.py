print("#" * 60)
print("WELCOME TO THE ADVANTURE GAME V1.0\n")
print('''You enter a dark room with four doors.
Do you go through door #1, door #2, door #3 or door #4?''')
print("#" * 60)

door = input("> ")

if door == "1":
    print("There's a giant beer here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Goood job!")
    elif bear == "2":
        print("The bear eats your face off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yello jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a full of muck.")
        print("Good job!")

# I inject these code!
elif door == "3":
    print("#" * 50)
    print("WELCOME TO THE SCARY ROOM!")
    print("You see a black python snake staring at you.")
    print("what do you do?")
    print("1. Fight the snake.")
    print("2. Run away from the snake")
    print("#" * 50)

    dsecision = input("> ")

    if dsecision == "1":
        print("The snake bite you and die. Good job!")
    elif dsecision == "2":
        print("The door is closed and you can't escape.")
        print("Good job!")
    else:
        print(f"{dsecision} isn't an option. The snake swallow you.")
        print("Game over!")

elif door == "4":
    print("@" * 30)
    print("oops! YOU ENTER A FIGHTING ROOM")
    print("Two knight guard with weapons are standing infront of you.")
    print("What would you do?")
    print("1. Fight them.\n2. Staring at them.")
    print("@" * 30)

    choise = input("> ")
    
    if choise == "1" or choise == "2":
        print("These people are too powerfull and You can't fight them.")
        print("Good job!")
    else:
        print(f"{choise} can't help you. No way to escape!")
        print("Game Over ):")
else:
    print("You stumble around and fall on a knife and die. Good job!")