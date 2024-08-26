print(''' 
Study Drills
      
Question:

2. Change the numbers of cars, people, and trucks, and then trace through each if-statement
to see what will be printed.

Answer:

[+] Yep.
''')

print('#'*50)

people = 3
cars = -1
trucks = 101

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("W can\'t decide.")


if trucks > cars:
    print("That\' too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can\'t decide.")

if people > trucks:
    print("Alright, let\'s just take the trucks.")
else:
    print("Fine, let\'s stay home then.")
    
print('#'*50)