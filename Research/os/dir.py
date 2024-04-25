##########################################################################################
 #               WANNAN WANI PROGRAME NE DA ZAI MA CREATING FOLDERS GUDA BIYU            #
##########################################################################################

import os
#sunan folder da zanyi creating.
directory = 'New_dir'
#location din folder(inda zaka ajiye ta kenan).
parent_dir = 'C:/Users/acer/3D Objects/Pentest/lpthw/Research/os'
#wannan layin yana hada mana folders din guda biyu a wuri daya. parent_dir din mu da kuma directory.
path = os.path.join(parent_dir, directory)

#wann layin zai mana creating na folder din mu.
os.mkdir(path)
#ma'anar '% s' shine zai kira mana sunan folder din mu da muka yi creating ya sa mana shi a cikin string din mu.
print('Directory \'% s\' Created!' % directory)
directory = 'new_dir'
parent_dir = 'C:/Users/acer/3D Object/Pentest/lpthw/Research/os'
mode = 0o666
path = os.path.join(parent_dir, directory)
os.mkdir(path, mode)
print('Directory \' % s\' Created!' % directory)