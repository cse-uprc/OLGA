import consts
commands = {}   # list of commands and respective extensions
extensions = [] # list of extensions

class OutputObject:
    # The Olga Output Object is meant
    #   to be a way to store data from extensions
    def __init__(self):
        self.text = None
        self.error = None

def makeOOO(text=None, error=None):
    OOO = OutputObject()
    OOO.text = text
    OOO.error = error
    return OOO

def init():
    global commands
    global extensions
    # Get commands
    with open(consts.COMMANDS_FILE, "r") as f:
        for line in f:
            commands[line.split(",")[0]] = line.split(",")[1]   # setting command dictionary
            if not line.split(",")[1] in extensions:
                extensions.append(line.split(",")[1])   # list of all extensions
    
    # Get front end
    with open(consts.CONFIG_FILE, "r") as f:
        for line in f:
            if "FRONT-END:" in line:
                frontEnd = line.replace("FRONT-END:", "")
    
    front = __import__("Front-Ends."+frontEnd, globals(), locals(), ["init"])
    front.init()
    

def run(command):
    global commands
    global extensions
    if command in commands.keys():
        extension = __import__(("Extensions."+commands[command]), globals(), locals() ["listen"])
        output = extension.listen(command)
    else:
        output = makeOOO(error="Command Unknwon")
    return output

if __name__ == "__main__":
    init()