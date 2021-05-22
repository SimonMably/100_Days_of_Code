import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
SCOPE = os.getenv("SCOPE")
CACHE = os.getenv("CACHE")

# --- Scraping Top 100 Song Titles From User Inputted Date ---------------------
URL = "https://www.billboard.com/charts/hot-100"

date = input("What date would you like to get music from (YYYY-MM-DD): ")

response = requests.get(f"{URL}/{date}")
music_billboard = response.text
soup = BeautifulSoup(music_billboard, "html.parser")

song_titles = soup.find_all(name="span", class_="chart-element__information__song")

song_names = [song.getText() for song in song_titles]
print(song_names)

# --- Spotify OAuthentication --------------------------------------------------
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=SCOPE,
        show_dialog=True,
        cache_path=CACHE
    )
)

user_id = sp.current_user()["id"]

# --- Search Spotify for Scraped Song Titles -----------------------------------

song_uris = []
date_list = date.split("-")

for song in song_names:
    track_id = sp.search(q=f"track:{song} year:{date_list[0]}", type="track")
    print(track_id)
    try:
        uri = track_id["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# --- Create Playlist and Add Searched Songs --------------------------

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100",
                                   public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)




