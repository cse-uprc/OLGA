from sys import path
from pyowm import OWM
import json
import os

try:
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    print (str(__location__))

    with open(os.path.join(__location__, 'keys_weather.json')) as json_file:
        data=json.load(json_file)
        TOKEN=data['token']

    # owm = OWM(TOKEN)
    # observation = owm.weather_at_place('Kent,US')
    # w = observation.get_weather()
except:
    print ("There was an error installing. Probably related to the internet connection.")

def install():
    # Adds the extensions commands to the command file
    import consts
    print("Installing WeatherEXT")
    print(consts.COMMANDS_FILE)
    commandsFile = open(consts.COMMANDS_FILE, "a") # w+?
    commandsFile.write("temperature,WeatherEXT\n")
    commandsFile.write("clouds,WeatherEXT\n")
    commandsFile.write("pressure,WeatherEXT\n")
    commandsFile.write("humidity,WeatherEXT\n")
    commandsFile.write("summary,WeatherEXT\n")
    commandsFile.write("detailed_summary,WeatherEXT\n")
    commandsFile.close()
    print("Install Complete!")
    return 

def init():
    # A very useful function that does a lot of things!
    return

def listen(command):
    try:
        # Takes and processes command from OLGA
        
        # Adds olga's directory to be accessible
        import os
        olgaDir = os.getcwd().replace("Extensions"+os.sep, "")
        path.append(olgaDir)
        from olga import makeOOO

        # Need to get the most current weather.
        owm = OWM(TOKEN)
        observation = owm.weather_at_place('Kent,US')
        w = observation.get_weather()
        
        # Package output into an Olga Output Object
        output = None
        if(command=="temperature"):
            output = makeOOO(text=str(w.get_temperature('fahrenheit')['temp']) +' F Date/Time:'+ str(w.get_reference_time(timeformat='iso')))
        elif(command=="clouds"):
            output = makeOOO(text= str(w.get_clouds())+"% Cloud Cover. Date/Time:" + str(w.get_reference_time(timeformat='iso')))
        elif(command=="pressure"):
            output = makeOOO(text=str(w.get_pressure())+" Date/Time:" + str(w.get_reference_time(timeformat='iso')))
        elif(command=="humidity"):
            output = makeOOO(text=str(w.get_humidity())+"% Humidity. Date/Time:" + str(w.get_reference_time(timeformat='iso')))
        elif(command=="summary"):
            output = makeOOO(text=str(w.get_status()))
        elif(command=="detailed_summary"):
            output = makeOOO(text=w.get_detailed_status())
        return output
    except:
        output = makeOOO(error="Internet is required sweetheart...")
    return output
