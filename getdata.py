# https://sotiriskakanos.com/2017/08/05/using-spotifys-web-api-with-python/
# thanks to this post for help with client credentials flow !!
import os
import csv
import pandas as pd
from datetime import datetime, timedelta
from dateutil.parser import parse
import pprint
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='9136122514e44a0e986b3ede133f8e63',client_secret='ab32dd62d54540168f81fc737487c1a0')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

with open('trackdata.csv', 'a') as f:
    f.write('\n')

with open('alltracks.csv',newline='',encoding="iso-8859-1") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        pprint.pprint(row)
        art = row['artist']
        tra = row['song']
        date = row['date']

        query = 'artist:{} track:{}'.format(art,tra)
        result = sp.search(q=query, type='track', limit='1')
        track_id = result['tracks']['items'][0]['id']

        features = sp.audio_features(track_id)[0]
        track_info = sp.track(track_id)
        
        album_date = track_info['album']['release_date']

        artist_id = track_info['artists'][0]['id']
        artist_info = sp.artist(artist_id)

        f = open('trackdata.csv','a')
        labels = ['id','song','artist','album','date','danceability','energy','key','loudness','mode','speechiness','acousticness','instrumentalness','liveness','valence','tempo','time signature','genres','release date','artist popularity','track popularity']
        with f:
            writer = csv.DictWriter(f, fieldnames=labels)
            writer.writerow({
                "id": track_id,
                "song": track_info['name'], 
                "artist": artist_info['name'],
                "album": track_info['album']['name'],
                "date": date,
                'danceability': features['danceability'],
                'energy': features['energy'],
                'key': features['key'],
                'loudness': features['loudness'],
                'mode': features['mode'],
                'speechiness': features['speechiness'],
                'acousticness': features['acousticness'],
                'instrumentalness': features['instrumentalness'],
                'liveness': features['liveness'],
                'valence': features['valence'],
                'tempo': features['tempo'],
                'time signature': features['time_signature'],
                'genres': artist_info['genres'],
                'release date': album_date,
                'artist popularity': artist_info['popularity'],
                'track popularity': track_info['popularity'] 
            })