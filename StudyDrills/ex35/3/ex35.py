from sys import exit

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

    # Farko mun sanya matsawar bear tazama false.
    bear_move = False

    while True:
        choice = input('> ')

        if choice == 'honey':
            dead('The bear looks at you then slap your face off.')

        # Wann layin na nufin idan player ya shigar da 'taunt bear' sann kuma variable 'bear_move == False' yanxu ya zama True(Ma'ana bear ya matsa.) to zai mana printing din abun da ke qasan fnx dn.
        elif choice == 'taunt bear' and not bear_move:
            print('The bear has move from the door.')
            print('You can go through it now.')
            # 'bearmove = True' Hakan na nufin yanxu bear na ya masta.
            bear_move = True
        
        # An bani damar shigar da wani choice dn. layin of code dn na cewa idan player ya shigar da 'taunt bear' sann kuma variable dina na saman nan ya zama true('bear_move == True', ma'ana bear na ya matsa daga inda yake). NB: ba variable dina na wajan loop dina ba. tohm yayi printing dead() fnx.
        elif choice == 'taunt bear' and bear_move:
            dead('The bear gets pissed off and chews your leg off')

        # Idan kuma na shigar da 'open door' bayan bear na ya matsa daga inda yake(bear_move == True). sae ya kira wani fnx mai suna gold_room().
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
        start()
    elif 'head' in choice:
        dead('Well that was tasty!')
    else:
        cthulhu_room()


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