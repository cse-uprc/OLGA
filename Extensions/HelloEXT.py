from sys import path

def install():
    import consts
    print("Installing HelloEXT")
    print(consts.COMMANDS_FILE)
    commandsFile = open(consts.COMMANDS_FILE, "w+")
    commandsFile.write("hello,HelloEXT")
    commandsFile.close()
    return 

def init():
    return

def listen(command):
    path.append("../")
    from OLGA import makeOOO
    output = None
    if(command=="hello"):
        output OLGA.makeOOO(text="Hello World")
    return output
