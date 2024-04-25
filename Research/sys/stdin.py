###################################################################################################
#PYTHON PROGRAM DAZAI BAKA DAMA KA SHIGAR DA INPUT ARGUMENTS TA HANYAR AMFANI DA sys module
####################################################################################################

import sys
for line in sys.stdin:
    #idan muka danna 'q' zai yi EXIT
    if 'q' == line.rstrip():
        break
    print(f'input: {line}')
print('Exit')