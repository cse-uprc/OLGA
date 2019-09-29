from sys import path

def install():
    # Adds the extensions commands to the command file
    import consts
    print("Installing AdobeEXT")
    print(consts.COMMANDS_FILE)
    commandsFile = open(consts.COMMANDS_FILE, "a")
    commandsFile.write("adobe,AdobeEXT\n")
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
    if(command=="adobe"):
        output = makeOOO(text="Open Adobe Acrobat Reader")
        import subprocess
        subprocess.Popen('C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe') # This opens up the calculator
    return output
