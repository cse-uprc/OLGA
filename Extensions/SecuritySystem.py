from sys import path
import threading
import os

def install():
    import consts
    commandsFile = open(consts.COMMANDS_FILE, "a")
    commandsFile.write("arm,SecuritySystem\n")
    commandsFile.write("disarm,SecuritySystem\n")
    commandsFile.close()
    
    threadData = open("threads.data", "w+")
    threadData.write("watchdog:False")
    threadData.close()
    return 

def init():
    return

def listen(command):
    path.append("../")
    from olga import makeOOO
    output = None
    if(command=="arm"):
        try:
            # arm system
            threadFile = open("threads.data", "r")
            threadData = []
            for line in threadFile.readlines():
                print(line)
                for s in line[:].split(':'):
                    print(s)
                    threadData.append(s)
            
            print(threadData)
            
            if (threadData[1] == "True"):
                output = makeOOO(text=="Watchdog service already running.")
                return output
                
            threadFile.close()
            threadFile = open("threads.data", "w")
            
            watchdogThread = threading.Thread(target = watchdog)
            watchdogThread.daemon = True
            watchdogThread.start()
            
            threadFile.write("watchdog:True")
            threadFile.close()
            
            output = makeOOO(text="System Armed.")
        except Exception as e:
            print(e)
            output = makeOOO(text="You're a failure.")
            pass
    
    elif (command == "disarm"):
        try:
            # disarm system
            threadFile = open("threads.data", "r")
            threadData = []
            for line in threadFile.readlines():
                for s in line[:].split(':'):
                    threadData.append(s)
                    
            if (threadData[1] == "False"):
                output = makeOOO(text="Watchdog service already shutdown.")
                return output
                
            threadFile.close()
                
            threadFile = open("threads.data", "w")
            threadFile.write("watchdog:False")
            threadFile.close()
            os.remove("threads.data")
            output = makeOOO(text="System Disarmed.")
        except Exception as e:
            print(e)
            output = makeOOO(text="You're a failure.")
            
    return output
    
def watchdog():
    cpuinfo = os.uname()
    if (cpuinfo[4] != 'armv71'):
        threadFile = open("threads.data", "w")
        threadFile.write("watchdog:False")
        return None
    
    import RPi.GPIO as GPIO
    import time
    
    GPIO.setmode(GPIO.BOARD)

    # Define our input/output pins here
    inputs = [36]
    outputs = [40]

    # Setup intputs/outputs
    GPIO.setup(inputs, GPIO.IN)
    GPIO.setup(outputs, GPIO.OUT)
    
    while (True):
        threadFile = open("threads.data", "r")
        threadData = []
        for line in threadFile.readlines():
            line.split(",")[1].replace("\n", "")
            for s in line[:-1].split(','):
                threadData.add(s)
                
        if (threadData[1] == "False"):
            threadFile.close()
            break
    
        sensors = GPIO.input(inputs)
        if (sensors == GPIO.HIGH):
            GPIO.output(outputs, GPIO.HIGH)
            time.sleep(1.5)
            GPIO.output(outputs, GPIO.LOW)

    # Cleanup
    GPIO.cleanup()
