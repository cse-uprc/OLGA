import spotipy
import json
import os
import os.path
import sys
import spotipy.util as util
from json.decoder import JSONDecodeError
import pickle

def install():
    # Adds the extensions commands to the command file
    import consts
    print("Installing Spotify")
    print(consts.COMMANDS_FILE)
    commandsFile = open(consts.COMMANDS_FILE, "a")
    commandsFile.write("play,spotify\n")
    commandsFile.close()
    return 

def init():
    # Log in?
    return

def listen(command):
    scope = 'user-read-private user-read-playback-state user-modify-playback-state'
    username = "lonemaurader"
    track = command.replace("play ","")

    import os
    # Check if there is a spotify token file
    if (os.path.exists(f".pickle--{username}")):
        spotify = pickle.load(open( f".pickle--{username}", "rb" ))
    else:
        token = util.prompt_for_user_token(username, scope, client_id="", client_secret="", redirect_uri="https://localhost/")
        # Generate request (before API)
        spotify = spotipy.Spotify(auth=token)
        pickle.dump(spotify, open( f".pickle--{username}", "wb" ) ) # thats hot :fire:

    # Get the response (after API)
    # Look through devices
    devices = spotify.devices()
    print(json.dumps(devices, sort_keys=True, indent=4))
    deviceId = devices['devices'][0]['id']

    # Play/edit/change music
    tids = [] 
    results =spotify.search(q=track, limit=1, type='track') 
    for i, t in enumerate(results['tracks']['items']):
        tids.append(t['uri'])
    spotify.start_playback(deviceId, None, tids, None)

    # Adds olga's directory to be accessible
    import os
    olgaDir = os.getcwd().replace("Extensions"+os.sep, "")
    sys.path.append(olgaDir)
    from olga import makeOOO
    
    # Package output into an Olga Output Object
    output = makeOOO(text="Success")

    return output
