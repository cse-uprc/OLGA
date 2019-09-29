from sys import path

def install():
    # Adds the extensions commands to the command file
    import consts
    print("Installing ItunesEXT")
    print(consts.COMMANDS_FILE)
    commandsFile = open(consts.COMMANDS_FILE, "a")
    commandsFile.write("itunes,ITunesEXT\n")
    commandsFile.close()
    return 

def init():
    # A very useful function that does a lot of things!
    return

def listen(command):
    # Takes and processes command from OLGA
    
    # Adds olga's directory to be accessible
    import os
    olgaDir = os.getcwd().replace("Extensions"+os.sep, "")
    path.append(olgaDir)
    from olga import makeOOO
    
    # Package output into an Olga Output Object
    output = None
    if(command=="itunes"):
        output = makeOOO(text="Open Itunes")
        import subprocess
        subprocess.Popen('C:\\Program Files\\iTunes\\itunes.exe') # This opens up the calculator
    return output
