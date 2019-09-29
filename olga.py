import consts

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

class OLGA:
    # OLGA acts as a mediator between front-end and extensions
    def __init__(self):
        self.commands = {}   # list of commands and respective extensions
        self.extensions = [] # list of extensions

        # Get commands and extensions
        with open(consts.COMMANDS_FILE, "r") as f:
            for line in f:
                # setting command dictionary
                self.commands[line.split(",")[0]] = line.split(",")[1].replace("\n", "")
                if not line.split(",")[1] in self.extensions:
                    # list of all extensions
                    self.extensions.append(line.split(",")[1])
        

    def run(self, command):
        # Take command from user and check for a exact match in the commands dictionary
        if command.split(" ")[0] in self.commands.keys():
            extension = __import__(("Extensions."+self.commands[command.split(" ")[0]]).replace("\n",""),
             globals(), locals(), ["listen"])
            output = extension.listen(command)
        else:
            # There was no matching command in the commands dictionary
            output = makeOOO(error="Command Unknwon")
        return output
