from sys import path

def install():
    # Adds the extensions commands to the command file
    import consts
    print("Installing ExcelEXT")
    print(consts.COMMANDS_FILE)
    commandsFile = open(consts.COMMANDS_FILE, "a")
    commandsFile.write("excel,ExcelEXT\n")
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
    if(command=="excel"):
        output = makeOOO(text="Open Microsoft Excel")
        import subprocess
        subprocess.Popen('C:\\Program Files (x86)\\\Microsoft Office\\root\\Office16\\EXCEL') # This opens up the calculator
    return output
