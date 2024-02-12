# MusicalTimeMachine to make a Spotify playlist

import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "d59ebf1c2c694etc"  # get your own
CLIENT_SECRET = "4538f23fa8cetc"  # get your own
SPOTIPY_REDIRECT_URI = "http://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=SPOTIPY_REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="etc",
    )
)
user_id = sp.current_user()["id"]

year = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}")
contents = response.text

soup = BeautifulSoup(contents, 'html.parser')
artists = soup.select('li ul li h3')
songs = soup.select('li ul li span.a-no-trucate')  # they have a typo in their site currently

artists_list = [artist.get_text().strip() for artist in artists]
songs_list = [song.get_text().strip() for song in songs]

list_of_top100 = [f"{x} - {y}" for x, y in zip(artists_list, songs_list)]

print(list_of_top100)
