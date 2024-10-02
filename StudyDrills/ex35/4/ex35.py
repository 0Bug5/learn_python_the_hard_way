# QUESTION:
    # 4 Add more to the game. What can you do to both simplify and expand it

# ANSWER:
    
from sys import exit
import time

try:

    def gold_room():
        print('This room is full of gold. How much do you take?')

        choice = input('> ')

        if '0' in choice or '1' in choice:
            how_much = int(choice)
        else:
            dead('Man, learn to type a number.')
            
        if how_much < 50:
            print('Nice, you\'re not greedy, you win!')
            exit(0)
        else:
            dead('You greedy bastard!')    

    def bear_room():
        print('There is a bear here.')
        print('The bear has a bunch of honey.')
        print('The fat bear is in front of another door.')
        print('How are you going to move the bear?')
        bear_move = False

        while True:
            choice = input('> ')

            if choice == 'honey':
                dead('The bear looks at you then slap your face off.')
            elif choice == 'taunt bear' and not bear_move:
                print('The bear has move from the door.')
                print('You can go through it now.')
                bear_move = True
            elif choice == 'taunt bear' and bear_move:
                dead('The bear gets pissed off and chews your leg off')
            elif choice == 'open door' and bear_move:
                gold_room()
            else:
                print('I got no idea what that means.')


    def cthulhu_room():
        print('Here you see the great evil cthulhu.')
        print('Here, it, whatever stares at you and you go insane.')
        print('Do you flee for your life or eat your head?')

        choice = input('> ')

        if 'flee' in choice:
            bugs()
        elif 'head' in choice:
            dead('Well that was tasty!')
        else:
            cthulhu_room()

    def bugs():
        print('You are in a dark room.')
        print('There is a door to the right and left.')
        print('Which one do you take?')

        choice = input('> ')

    def dead(why):
        print(why, 'Good job!')
        exit(0)

    def start():
        print('You are in a dark room.')
        print('There is a door to the right and left.')
        print('Which one do you take?')

        choice = input('> ')

        if choice == 'left':
            bear_room()
        elif choice == 'right':
            cthulhu_room()
        else:
            dead('You stumble around the room until you starve.')


    start()

except KeyboardInterrupt:
    print('\nCTRL-C Pressed!')
    time.sleep(3)
    print('\nGam3 is Exited!\n')