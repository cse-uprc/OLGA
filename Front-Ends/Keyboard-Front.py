from sys import path
import os
olgaDir = os.getcwd().replace("Front-End"+os.sep, "")
path.append(olgaDir)
from olga import OLGA, OutputObject
from pynput.keyboard import Key, KeyCode, Listener

olgaInstance = None # Declare global instance

# The currently active modifiers
current_keys = set()

# Keyboard shortcut processing
def callAdobe():
    global olgaInstance
    output = olgaInstance.run("adobe")
    processOutput(output)

def callCalc():
    global olgaInstance
    output = olgaInstance.run("calculator")
    processOutput(output)

def callExcel():
    global olgaInstance
    output = olgaInstance.run("excel")
    processOutput(output)

def callOutlook():
    global olgaInstance
    output = olgaInstance.run("outlook")
    processOutput(output)

def callPower():
    global olgaInstance
    output = olgaInstance.run("powerpoint")
    processOutput(output)

def callWord():
    global olgaInstance
    output = olgaInstance.run("word")
    processOutput(output)

# The key combination to check
combination_to_function = {
    frozenset([Key.shift, KeyCode(char='a')]): callAdobe,
    frozenset([Key.shift, KeyCode(char='A')]): callAdobe,
    frozenset([Key.shift, KeyCode(char='c')]): callCalc,
    frozenset([Key.shift, KeyCode(char='C')]): callCalc,
    frozenset([Key.shift, KeyCode(char='e')]): callExcel,
    frozenset([Key.shift, KeyCode(char='E')]): callExcel,
    frozenset([Key.shift, KeyCode(char='o')]): callOutlook,
    frozenset([Key.shift, KeyCode(char='O')]): callOutlook,
    frozenset([Key.shift, KeyCode(char='p')]): callPower,
    frozenset([Key.shift, KeyCode(char='P')]): callPower,
    frozenset([Key.shift, KeyCode(char='w')]): callWord,
    frozenset([Key.shift, KeyCode(char='W')]): callWord
}

def on_press(key):
    # When a key is pressed, add it to the set we are keeping track of and check if this set is in the dictionary
    current_keys.add(key)
    if frozenset(current_keys) in combination_to_function:
        # If the current set of keys are in the mapping, execute the function
        combination_to_function[frozenset(current_keys)]()

def on_release(key):
    # When a key is released, remove it from the set of keys we are keeping track of
    current_keys.remove(key)

# OLGA Front-end methods
def processOutput(output):
    # only the error and text properties are checked in the console front-end
    if(output.error!=None):
        print(output.error) # if an error exists display
    else:
        print(output.text)  # otherwise the text property is displayed

def run(olgaInstance):
    print("WELCOME TO OLGA")
    print("Good Luck ;)")
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    
def init():
    # Create an instance of OLGA and start the front-end
    global olgaInstance
    olgaInstance = OLGA()
    run(olgaInstance)

if __name__ == "__main__":
    init()