check if username argument is present
if username is present
login(username)
log username to user info file
else
check if user info file exists
if exists
login(username)

while True
Check if Song is playing
if song playing
display "Now Playing"

        get song name
        get artist name
        get album cover
        download album cover
        convert album cover to ascii

        display data

        current song = get song
        new song = get song
        while current song = new song
            new song = get current song
            wait(cooldown time)

    else
        display "No Song Playing"

def login()
use username to get token and attempt to log in
spotipy will automatically use .cache file
if AttributeError or JSONDecodeError
delete .cache file
