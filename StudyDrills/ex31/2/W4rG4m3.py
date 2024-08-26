import sys
import time
from datetime import datetime

__author__ = "Zacks"

# Question:

# 2. Write a completely new game. Maybe you don’t like this one, so make your own. This is your computer; do what you want

script, ip_address = sys.argv

print('\n' + "@" * 168+ '\n')
print(f'''\t\t\tWELCOME TO Bugs CTF CHANNEL. YOUR IP ADDRESS IS: {ip_address} HAVE FUN WITH MYSQL AND SSH.\n
TASK:
\tYou Are In The CTF G4M3 And There Are Two Remote Machines To Connect To. Which Machine Would You Select?
1. ssh
2. mysql db\n''')
print("@" * 168 + '\n')

try:
    connect_to = input("ctf@root ~$: ")

    # ssh server.
    if connect_to == "1":
        time.sleep(2)
        print(f'''
        Well, You choose number {connect_to} i.e SSH server. Good Luck on your Mission.

        Instructions:

            [+] Connect to this remote machine 127.0.0.1 -p 2020
            [+] username and password: bugs:bugs
            [+] Copy the file called 'passwrd.txt' from the remote machine at home directory to your desktop directory.
            [+] Caution! You are to enter only one command at a time, except for the username and password login.
            [+] Good Luck.\n''')
        
        ssh = input("ctf@root ~$: ")

        def clone_the_file():
            copy_the_pswd_cmd = input("remotemachine@root ~$: ")
            
            if copy_the_pswd_cmd == "scp bugs@127.0.0.1:passwrd.txt ~/Desktop":
                print("Copying the file...")
                time.sleep(1)
                print("Done.")
                print("You Win!\nWell, Good Job! Your Reward is $100 dollers.\n")
            else:
               print(f"Unable to copy the file! '{copy_the_pswd_cmd}' is a Bad command to copy this file!")
               time.sleep(2)
               print("Detected By IDS! Discovering who you are.......")
               time.sleep(3)
               print("We know who you are and where you are!\n")
               time.sleep(2)
               print("@"*35)
               print(f'''\nOS NAME: Microsoft Windows 11 Pro\nWLAN SSID: CONTINENTAL-079\nIP: {ip_address}\n\nLATITUDE: 40*45`19.59"\nLONGTITUDE: 73*58`45.73"\n''')
               print("@"*35 + '\n')
               print("Game Over!!\n")

        def list_dir():
            ls_dir =  input("remotemachine@root ~$: ")

            if ls_dir == "ls":
                print('''remotemachine@root ~$: passwrd.txt''')
                cat_pswd()
                clone_the_file()
            elif ls_dir == "ls -l":
                print(f'''total 1\nremotemachine@root ~$: -r--r--r-- bugs bugs 19663 {datetime.now()} passwrd.txt''')
                cat_pswd()
                clone_the_file()
            elif ls_dir == "ls -la":
                print(f'''total 1\nremotemachine@root ~$: -r--r--r-- bugs bugs 19663 {datetime.now()} .''')
                print(f'''remotemachine@root ~$: -r--r--r-- bugs bugs 19663 {datetime.now()} ..''')
                print(f'''remotemachine@root ~$: -r--r--r-- bugs bugs 19663 {datetime.now()} passwrd.txt''')
                cat_pswd()
                clone_the_file()
            else:
                print(f'''remotemachine@root ~$:\nThe program '{ls_dir}' is currently not installed. You can install it by typing:\nsudo apt-get install {ls_dir}\n-bash: {ls_dir}: command not found''')
                list_dir()

        def hash():
            print("@"*100 + '\n')
            print('''bugs:$y$j9T$F43rnSv/.RSsV8TgeykCB/$yH3X3r/si7B.XG2mUOp/VZNgia5SEdOJzbT8SBWaut.:19891:0:99999:7:::\ndebian-tor:!:19891::::::\nsslh:!:19891::::::\nzacks:$y$j9T$6TIMAzCkBuiyXDXaBtcg2/$6imY2/r03V0HD5txJ6JwLGlTVkk7JbXX2eqBCuh7f31:19934:0:99999:7:::\n''')
            print("@"*100 + '\n')
                
        # cat the password.
        def cat_pswd():
            cat_cmd =  input("remotemachine@root ~$: ")
            if cat_cmd == "cat passwrd.txt":
                # file = open("passwrd.txt", 'r')
                # print(file.read())
                # file.close()
                hash()
            elif cat_cmd == "more passwrd.txt":
                hash()
            elif cat_cmd == "less passwrd.txt":
                hash()
            else:
                print(f'''remotemachine@root ~$:\nThe program '{cat_cmd}' is currently not installed. You can install it by typing:\nsudo apt-get install {cat_cmd}\n-bash: {cat_cmd}: command not found''')
                list_dir()


        def login_to_ssh():
            if ssh == "ssh bugs@127.0.0.1 -p 2020":
                user_name = input("ctf@root ~$: Enter a username: ") 
                password = input("ctf@root ~$: Enter a password: ") 

                if user_name and password == "bugs":
                    print('Connected Successfully!\n')
                    time.sleep(2)
                    print("#" * 100)
                    print('WELCOME TO Bugs CTF REMOTE MACHINE!\n\nTask:\n\tYour Mission Is To Find a Password File Stored Somewhere In This Machine. HAVE FUN!\n\nHelpful Command: ls, ls -l, cat, ls -la\n')
                    
                    print("#" * 100 + '\n')            

                    # ls dir code.
                    list_dir()                    

                else:
                    print(f"ctf@root ~$: Access Denied username {user_name} | password is incorrect and input must be filled!")
                    login_to_ssh()

            else:
                print(f"\nOops! unable to connect to the remote machine. '{ssh}' isn't how to connect to the CTF remote machine!")
                print("Our Host is:127.0.0.1 and Port is:2020. You are SCRIPT KIDDIE!")
                print("Game Over! ):\n")

        login_to_ssh()

    # mysql server code.
    elif connect_to == "2":
        time.sleep(2)
        print(f'''
        WELCOME TO MARIA DB SERVER!, You Select Machine Number {connect_to} i.e Mysql db. Good Luck On Your Mission.

        Instructions:

            [+] Connect to mysql remote database: -u bugs -p 127.0.0.1
            [+] password is: bugs.
            [+] Update the admin table.
            [+] Set the username 'root' and password 'VZNgia5SEdOJzbT8SBWaut.:19891:0:99999:7:::'
            [+] Caution! You are to enter only one command at a time.
            [+] Except for the username and password login.
            [+] Good Luck.\n''')
        
        mysql = input("ctf@root ~$: ")

        def sql_syntax_error():
            print(f'''MariaDB [(none)]> ERROR 152021 OCCURED IN YOUR PROGRAM. You Have Syntax Error In Your Sql Statement.\n''')
            time.sleep(3)
            print("Remember Only one attempt is allowed in this G4ME!\n")
            time.sleep(1)
            print("Game Over!\n")

        def show_db():
            sql_cmd1 =  input("MariaDB [(none)]> ").lower()
            
            if sql_cmd1 == "show databases;".lower():
                print('''
+--------------------+
| Database           |
+--------------------+
| information_schema |
| ctfbank_db         |
+--------------------+
2 rows in set (0.023 sec)\n''')
                use_db()
            else:
                sql_syntax_error()

        def use_db():
            sql_cmd2 =  input("MariaDB [(none)]> ").lower()

            if sql_cmd2 == "use ctfbank_db;":
                print('''Reading table information for completion of table and column names\nYou can turn off this feature to get a quicker startup with -A\n\nDatabase changed\n''')
                show_ctfbank_db()

            else:
                sql_syntax_error()

        def show_ctfbank_db():
            sql_cmd3 =  input("MariaDB [(ctfbank_db)]> ").lower()

            if sql_cmd3 == "show tables;".lower():
                print('''
+-----------------------+
| Tables_in_ctfbank_db  |
+-----------------------+
| ctf_customers         |
| ctf_credit            |
| ctf_deposit           |
| ctf_transfer          |
| ctf_postmeta          |
| ctf_posts             |
| ctf_admin             |
| ctf_term_taxonomy     |
| wp_termmeta           |
| ctf_terms             |
| ctf_usermeta          |
| ctf_users             |
+-----------------------+
12 rows in set (0.001 sec)\n''')
                select_admin()
                
            else:
                sql_syntax_error()

        def select_admin():
            sql_cmd4 = input("MariaDB [(ctfbank_db)]> ").lower()
            
            if sql_cmd4 == "select * from ctf_admin;".lower():
                print('''
+------------+---------------------+---------------------------------------+
| Field      | username            | password                              |
+------------+---------------------+---------------------------------------+
| id         | admin               | $y$j9T$F43rnSv/.RSsV8TgeykCB/$yH3X3ry |
|            |                     |                                       |
+------------+---------------------+------+-----+---------+----------------+''')
                update_admin()
            else:
                sql_syntax_error()
 
        def update_admin():
            sql_cmd5 = input("MariaDB [(ctfbank_db)]> ").lower()

            if sql_cmd5 == "update ctf_admin set username = 'root' and password = 'VZNgia5SEdOJzbT8SBWaut.:19891:0:99999:7:::' where id=1;".lower():
                time.sleep(2)
                print('''Reading table information for completion of table and column names\nYou can turn off this feature to get a quicker startup with -A\n\nctf_admin tables updated successfully.\n\n12 rows in set (0.001 sec)\n''')
                time.sleep(2)
                print("HOORAY! MISSION IS COMPLETED. YOU WIN!\n")
                print("$100 dollers has been transfered to your account. Have Fun!\n")
            else:
                sql_syntax_error()

        def login_to_mysql():
            if mysql == "mysql -u bugs -p 127.0.0.1":
                password = input("Enter a password: ")

                if password == "bugs":
                    time.sleep(1)
                    print('''Welcome to the MariaDB monitor.  Commands end with ; or \g.\nYour MariaDB connection id is 31\nServer version: 10.11.4-MariaDB-1 Debian 12\n\nCopyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.\n\nType 'help;' or '\h' for help. Type '\c' to clear the current input statement.\n\n''')
                    time.sleep(2)           

                    show_db()                    

                else:
                    print(f"ctf@root ~$: Access Denied: password is incorrect | input must be filled!")
                    login_to_mysql()
        
            else:
                print(f"\nOops! Unable To Connect To Mysql Server! '{mysql}' Isn't How To Connect To The CTF Remote Machine.")
                print("Correct Syntax is: '-u bugs -p 127.0.0.1' You are SCRIPT KIDDIE!\n")
                time.sleep(2)
                print("Remember Only one attempt is allowed!\n\nGame Over!\n")

        login_to_mysql()

    # Any choise other than 1 of 2.
    else:
        print(f"\nDon't Be a SCRIPT KIDDIE! '{connect_to}' isn't Exits on this server.\n")
        time.sleep(3)
        print("Connection is Terminated.\n")
        time.sleep(3)
        print("You Are Out Of The Game!\n")

except KeyboardInterrupt:
    print('You Press CTRL-C. Connection Terminated.\n')
