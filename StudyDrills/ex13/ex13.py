
# 1. Try giving fewer than three arguments to your script. See that error you get? See if you can explain it.

# 2. Write a script that has fewer arguments and one that has more. Make sure you give the unpacked variables good names.

#script with fewer arguments.
from sys import argv
# script, os, version = argv

# print('Target OS:', os)
# print('Target OS version:', version)

target_machine = input('Enter Target Machine Name: ')
#script with more arguments.
script, osName, osVersion, osManufacturer, osConfiguration, productId = argv

print('##################TARGET MACHINE INFORMATION################')
# print('OS Name:', osName)
# print('OS Version:', osVersion)
# print('OS Manufacturer:', osManufacturer)
# print('OS Configuration:', osConfiguration)
# print('Product ID:', productId)

# 3. Combine input with argv to make a script that gets more input from a user. Don’t overthink it. Just use argv to get something, and input to get something else from the user.


print(f'OS Name: {osName}')
print(f'OS Version: {osVersion}')
print(f'OS Manufacturer: {osManufacturer}')
print(f'OS Configuration: {osConfiguration}')
print(f'Product ID: {productId}')


print(f'{target_machine} Found!')