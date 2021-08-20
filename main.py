import os
import sys
import json
import spotipy
import spotipy.util as util
from json.decoder import JSONDecodeError

def login(username):
    #permissions spotipy will ask for
    scope = 'user-read-private user-read-playback-state user-modify-playback-state'
    try:
        token = util.prompt_for_user_token(username, scope)
    except (AttributeError, JSONDecodeError):
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope)
    except (spotipy.SpotifyException):
        sys.exit("no environment variables")


try:
    len(sys.argv[1])
    username=sys.argv[1]
    login(username)
    try:
        os.remove("username.txt")
    except:
        print(username, file=open('username.txt', 'w'))
except:
    try:
        file = open("username.txt", "r")
        username = file.read()
    except:
        print("Please Specify a username as such")
        print("main.py \"username\"")
        sys.exit("No username")
    login(username)
        

print ("successfully logged in")







