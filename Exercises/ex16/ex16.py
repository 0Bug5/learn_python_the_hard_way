from sys import argv
import time

script , filename = argv

print(f"We are going to erase {filename}.")
print('If you don\'t want that, hit CTR-C (^C).')
print('If you do want that, hit RETRUN.')

input('? ')

print('Opening file...')
target = open(filename, 'w')
time.sleep(2)

print('Truncating the file. goodbye!')
target.truncate()
time.sleep(2)

print(target)
print('Now i\'m going to ask you for the three lines.')

line1 = input('Line1: ')
line2 = input('Line2: ')
line3 = input('Line3: ')

print('I\'m going to write these to the file')

target.write(f"{line1}\n{line2}\n{line3}")

target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print('And finally, we close it.')
target.close()
