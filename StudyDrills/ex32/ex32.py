# QUESTIONS:

# 2. Could you have avoided that for-loop entirely on line 22 and just assigned range(0,6) directly to elements?

# ANSWER:
    # i solve it based on my understanding.

the_count = [1, 2, 3, 4,]
fruits = ['apples', 'orange', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through list
for number in the_count:
    # print(f"This count {number}")
    pass

# same as above
for fruit in fruits:
    # print(f"A fruit of type: {fruit}")
    pass

# also we can go through mixed lists too
for i in change:
    # print(f"I got {i}")
    pass

# we can also buld lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 40): # i changed it to 40 instead of 6.
    print(f"Adding {elements} to the list.") # i solve it based on my understanding
    # append is a function that list understand
    elements.append(i)

# now we can print them out too
for i in elements:
    pass
    # print(f"Elements was {i}")