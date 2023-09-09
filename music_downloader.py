# import json

import spotipy
from pytube import *
from spotipy.oauth2 import SpotifyClientCredentials

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

playlist_id = '4AiQqiBwWiBBk0PWKIj1Qh' #ADD YOUR PLAYLIST ID

download_path = "../Music"  

playlist_items = spotify.playlist_items(playlist_id)
song_name = playlist_items


def get_artists_names():
  artists_names = []
  for item in song_name['items']:
      for innerItem in item['track']['artists'][-1:]: #only one artist per song (main one)
        artists_names.append(innerItem['name'])
  return artists_names

def get_songs_names():
  songs_names = []
  for item in song_name['items']:
    songs_names.append(item['track']['name'])
  return songs_names


list1 = get_artists_names()
list2 = get_songs_names()
songs_dict = dict(zip(list1, list2))
   

def download_yt(dict):
  for k,v in dict.items():
    song = Search(f'{k} {v}')
    for result in song.results:
      print(result.title)
      yt = YouTube(f'http://youtube.com/watch?v={result.video_id}')
      stream_info = yt.streams.filter(only_audio=True)
      stream = yt.streams.get_by_itag(stream_info[0].itag)
      stream.download(download_path)
      break


download_yt(songs_dict)



# Just to check json in nice formatted way
# file = open('records.txt', 'w')
# json.dump(song_name, file)