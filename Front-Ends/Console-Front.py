from sys import path

def processOutput(output):
    if(output.error!=None):
        print(output.error)
    print(output.text)

def run():
    path.append("../")
    from OLGA import run
    
    print("WELCOME TO OLGA")
    while True:
        print("Input Command")
        command = input()
        if(command=="exit"):
            break
        output = OLGA.run(command)
        processOutput(output)

def init():
    # For larger front ends there will likely be setup that
    #   should be done before running
    run()