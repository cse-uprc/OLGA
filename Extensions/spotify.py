import spotipy
import json
import os
import sys
import spotipy.util as util
from json.decoder import JSONDecodeError

scope = 'user-read-private user-read-playback-state user-modify-playback-state'
username = sys.argv[1]
track = ' '.join(sys.argv[2:])

try:
    token = util.prompt_for_user_token(username, scope)

except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token(username, scope)

spotify = spotipy.Spotify(auth=token)

devices = spotify.devices()
print(json.dumps(devices, sort_keys=True, indent=4))
deviceId = devices['devices'][0]['id']

user = spotify.current_user()
displayName = user['display_name']

tids = [] 
results =spotify.search(q=track, limit=1, type='track') 
#spotify.artist_albums(dtp_uri, album_type='album')
for i, t in enumerate(results['tracks']['items']):
    tids.append(t['uri'])
spotify.start_playback(deviceId, None, tids, None)
