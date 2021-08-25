import os
import requests
import sys
import time
import json
#import curses
import spotipy
import spotipy.util as util
import webbrowser
import argparse
import urllib.request
from json.decoder import JSONDecodeError
import PIL.Image
import climage
from pyfiglet import Figlet
from dotenv import load_dotenv

load_dotenv()
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
REDIRECT_URI = os.getenv('REDIRECT_URI')


#define token
token = ""

#ascii characters
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

#resize image
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return (resized_image)
    
#grayscale image
def grayify(image):
    grayscale_image = image.convert("L")
    return (grayscale_image)
    
#convert pixels to ascii
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return(characters)

#image converter
def convertImage(url, new_width=100):
    urllib.request.urlretrieve(url, "img.png")
    img = PIL.Image.open("img.png")

    new_image_data = pixels_to_ascii(grayify(resize_image(img)))

    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    return(ascii_image)

#color display image
def displayImage(url):
    urllib.request.urlretrieve(url, "img.png")
    img = PIL.Image.open("img.png")
    output = climage.convert("img.png")
    return output


#login function
def login(username):
    #permissions spotipy will ask for
    scope = 'user-read-private user-read-playback-state user-modify-playback-state'
    try:
        #tries to login
        token = util.prompt_for_user_token(username, scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)
        return token
        print("got token")
    except (AttributeError, JSONDecodeError):
        #if theres an error remove the cache and try again
        os.remove(f".cache-{username}")
        token = util.prompt_for_user_token(username, scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)
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

#try except loop
def do_action(actionToDo):
    try:
        return actionToDo
    except:
        login(username)
        token=login(username)
        spotifyObject=spotipy.Spotify(auth=token)


while True:
    current = do_action(spotifyObject.current_user_playing_track())
    if current == None:
        os.system("clear")
        print("nothing is playing")
        while current == None:
            current = do_action(spotifyObject.current_user_playing_track())
            time.sleep(5)
    else:
        #print(json.dumps(current, sort_keys=True, indent=4))
        track = current['item']['name']
        artist = current['item']['artists'][0]['name']
        imageURL = current['item']['album']['images'][0]['url']


        os.system("clear")
        print(track + " - " + artist)
        #print(convertImage(imageURL))
        print(displayImage(imageURL))

        newTrack = current['item']['name']

        while newTrack == track:
            newTrack = do_action(spotifyObject.current_user_playing_track())
            if newTrack == None:
                break
            newTrack = newTrack['item']['name']
            time.sleep(5)



