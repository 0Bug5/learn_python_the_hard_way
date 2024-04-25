#This one is like your script with argv
# wnn layin dai dai yake da 'from sys import argv'
def print_two(*args):
	# wnn layin dai dai yake da unpacks variables dina
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")
	
#Ok, that *args is actually pointless, we can just do this.
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")
	
#This just take one argument
def print_one(arg1):
	print(f"arg1: {arg1}")
	
#This one takes no argument
def print_none():
	print("I got nothin'. ")

print_two("Mus'ab", "Ibn Umair")
print_two_again("Zacks", "Mus'ab")
print_one('First')
print_none()