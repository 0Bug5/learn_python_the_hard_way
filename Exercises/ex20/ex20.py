from sys import argv

script, input_file = argv

def print_all(f):
	print(f.read())

# amfanin wanan layin shine: zai yi tariya gwargwadon number daka sa.	
def rewind(f):
	f.seek(0)
	
# Readline shine: zai nuna layin farko a script din mu.
def print_a_line(line_count, f):
	print(line_count, f.readline())
	
current_file = open(input_file)

print("First let's print the whole file: \n ")

print_all(current_file)

print("Let's rewind, kind like a tape")

rewind(current_file)

print("Let's print three lines: ")

current_line = 1
print_a_line(current_line, current_file)

#current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

#current_line = current_line + 1
current_line += 1

print_a_line(current_line, current_file)
