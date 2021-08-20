# spotify-terminal-now-playing

a now playing view for terminal

# instructions

go to spotify dev portal
make new app
set callback uri to https://www.google.com
now we have to set the client id, client secret, and redirect uri as environment variables
if on mac/linux use export (make sure to keep the quotation marks)
export SPOTIPY_CLIENT_ID="Enter your client ID here"
export SPOTIPY_CLIENT_SECRET="Enter your client secret here"
export SPOTIPY_REDIRECT_URI="Enter your redirect URL here"
if on windows use set (make sure there are no quotation marks)
set SPOTIPY_CLIENT_ID=Enter your client ID here
set SPOTIPY_CLIENT_SECRET=Enter your client secret here
set SPOTIPY_REDIRECT_URI=Enter your redirect URL here

then you can run the script

python main.py "spotify-username"

to get you username go to your account page, its not the pretty name, mine is a string of random characters

then accept the permissions and copy the url you get redirected to, paste that in the terminal and hit enter
