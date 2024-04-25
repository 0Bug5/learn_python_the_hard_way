# inserting features from python modules.
from sys import argv

# assigning variables using CMDL.
script, filename = argv

# open file from OS directory.
txt = open(filename)

# printing a plain txt.
print(f"Here's your file {filename}:")
# reading the file with read() fnx	.
#redline yana nufin, yayin printing layi daya kacal(1)
print(txt.readline())

# printing a plain txt.
print('Type the file name again:')
# accepting input from the user.
file_again = input('> ')

# open the file again.
txt_again = open(file_again)
# reading the file with read() fnx.
print(txt_again.close())
