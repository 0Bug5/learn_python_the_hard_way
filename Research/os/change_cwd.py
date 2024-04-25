##########################################################################################
#       WANNAN WANI PROGRAME NE DA ZAI CHANZA MA  CWD(current working dir) ZUWA WANI DIR #
##########################################################################################

import os
def current_dir(tense):
    print(f'Current working dir {tense}')
    print(os.getcwd())
    print()

current_dir('BEFORE: ')
os.chdir('../')
current_dir('AFTER: ')