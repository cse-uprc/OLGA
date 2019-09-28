from sys import path
import os
olgaDir = os.getcwd().replace("Front-End"+os.sep, "")
path.append(olgaDir)
from olga import OLGA, OutputObject

def processOutput(output):
    # only the error and text properties are checked in the console front-end
    if(output.error!=None):
        print(output.error) # if an error exists display
    else:
        print(output.text)  # otherwise the text property is displayed

def run(olgaInstance):
    print("WELCOME TO OLGA")
    print("Good Luck ;)")
    while True:
        print("Input Command")
        command = input()
        if(command=="exit"):
            break
        output = olgaInstance.run(command)
        processOutput(output)

def init():
    # Create an instance of OLGA and start the front-end
    olgaInstance = OLGA()
    run(olgaInstance)

if __name__ == "__main__":
    init()

