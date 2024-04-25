from sys import argv
import time

# If the file exists it return True, else false😁
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
#Answer by Zack's: By using cat command. e.g cat ex17 > ex18.txt
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

		# This is what i'm talking about⬇
print(f"Does the output file exist? {exists(to_file)}")
print(f"Ready, hit RETURN to continue, CTR-C to abort.")
input('$ ')

out_file = open(to_file, 'w')
out_file.write(indata)

print('Copying 0%...')
time.sleep(2)
print('Copying 15%')
time.sleep(2)
print('Copying 85%')
time.sleep(2)
print('Copying 100%')
time.sleep(2)

print('Alright, all done.')

#Python file method close() closes the opened file. 
#A closed file cannot be read or written any more.
out_file.close()
in_file.close()