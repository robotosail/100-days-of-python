#-------------Spotify playlist creator-----------#
from posixpath import split
from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# scrapping the songs
date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select(selector="li h3", class_="c-title")
# list comprehension to get the names of the songs from the html
song_names = [song.getText() for song in song_names_spans]
# getting the key and id from the environment variables
scope = "playlist-modify-private"
redirect_url = "https://example.com/"
SECRET = os.getenv("KEY")
ID = os.getenv("ID")
# authenticating ourselves
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=ID, client_secret=SECRET, scope=scope, redirect_uri=redirect_url))
# tecca_uri = 'spotify:artist:4Ga1P7PMIsmqEZqhYZQgDo'
# results = sp.artist_albums(tecca_uri, album_type='album')
# albums = results['items']
# print(albums)
user_id = sp.current_user()["id"]
song_uris = []

# adding the name of each song to the list
song_names = [name for name in song_names]
# print(song_names)

# splitting the dates from the "-"
year = date.split("-")[0]
if len(song_names) > 101:
    song_names = song_names[1:]

# looping through the songs
for song in song_names:
    # removing the whitespaces from the songs and searching through the database for the songs based on the year.
    result = sp.search(q=f"track:{song.strip()} year:{year}", type="track")
    # print(result)
    # testing if the code will work
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# # print(playlist)

# creating a playlist
playlist = sp.user_playlist_create(
    user=user_id, name=f"{date} Billboard 100", public=False)

# adding the songs to the play list
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
