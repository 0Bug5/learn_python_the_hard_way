people = 30
cars = 40
trucks = 15

if cars and trucks > people:
    print("We should take the cars.")
elif cars or not(people or trucks):
    print("We should not take the cars.")
else:
    print("W can\'t decide.")


if trucks > cars :
    print("That\' too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can\'t decide.")

if people and not(trucks or people):
    print("Alright, let\'s just take the trucks.")
else:
    print("Fine, let\'s stay home then.")