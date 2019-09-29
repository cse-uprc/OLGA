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
            
            if (threadData[1] == "True"):
                output = makeOOO(text="Watchdog service already running.")
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
            
            output = makeOOO(text="System Disarmed.")
        except Exception as e:
            print(e)
            output = makeOOO(text="You're a failure.")
            
    return output
    
def watchdog():
    try:
        import RPi.GPIO as GPIO
        import threading
        import time
        
        GPIO.setmode(GPIO.BOARD)

        # Define our input/output pins here
        inputs = [36]
        outputs = [38]

        # Setup intputs/outputs
        GPIO.setup(inputs, GPIO.IN)
        GPIO.setup(outputs, GPIO.OUT)
        
        GPIO.add_event_detect(inputs[0], GPIO.RISING)
        
        while (True):
            threadFile = open("threads.data", "r")
            threadData = []
            for line in threadFile.readlines():
                for s in line[:].split(':'):
                    threadData.append(s)
            threadFile.close()
            
            if (len(threadData) < 2 or threadData[1] == "False"):
                print("Okay, so end?")
                break
            
            if (GPIO.event_detected(inputs[0])):
                print("EVENT")
                GPIO.output(outputs, GPIO.HIGH)
                time.sleep(1.5)
                GPIO.output(outputs, GPIO.LOW)
        
        print("Shutting Down Service")
        GPIO.remove_event_detect(inputs[0])
        GPIO.cleanup()
        
        threadFile = open("threads.data", "w")
        threadFile.write("watchdog:False")
        
    except Exception as e:
        print(e)
