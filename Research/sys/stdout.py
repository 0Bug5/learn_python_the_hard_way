###################################################################################################
#PYTHON PROGRAM DAZAI MAKA CALCULATING TOTAL ARGUMENTS DA KA SHIGAR TA HANYAR AMFANI DA sys module#
####################################################################################################

import sys
n = len(sys.argv)
#wann layin yana mana printing total arguments din mu neh da muka shigar.
print('Total arguments passed:', n)
#wann layin yana mana printing sunan file din mu ne.
print('\nName of the Python script:', sys.argv[0])
#wann layin yana hada mana duka arguments din mu neh wuri daya.
print("\nArgument passed:", end=' ')
#wannan layin yana mana printing din duka arguments din mu da muka shigar.
for i in range(1, n):
    print(sys.argv[i], end=' ')
#wannan layin yana mana calculating din total arguments din mu ne.
sum = 0
for i in range(1, n):
    sum += int(sys.argv[i])
print("\n\nResult: ", sum)