import os
import sys
import json
import spotipy
import spotipy.util as util
import webbrowser
from json.decoder import JSONDecodeError

#define token
token = ""

#login function
def login(username):
    #permissions spotipy will ask for
    scope = 'user-read-private user-read-playback-state user-modify-playback-state'
    try:
        #tries to login
        token = util.prompt_for_user_token(username, scope)
        return token
        print("got token")
    except (AttributeError, JSONDecodeError):
        #if theres an error remove the cache and try again
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope)
        return token
    except (spotipy.SpotifyException):
        #if the environment variables arent set, exit
        sys.exit("no environment variables")


#determine if there is a argument
try:
    len(sys.argv[1])
    argument = True
except:
    argument = False

#if there is an argument use that, if else try using username file
if argument == True:
    username=sys.argv[1]
    token = login(username)
    try:
        #wipe existing username
        os.remove("username.txt")
    except:
        print("writing new username file")
    #set cache username to new username
    print(username, file=open('username.txt', 'w'))

else:
    #if there is no argument
    try:
        #try opening username cache file and reading username
        file = open("username.txt", "r")
        username = file.read()
    except:
        #if it doesnt work ask for a username and exit
        print("Please Specify a username as such")
        print("main.py \"username\"")
        sys.exit("No username")
    #if it can find a username try logging in
    token = login(username)







spotifyObject=spotipy.Spotify(auth=token)

print("successfully logged in")


