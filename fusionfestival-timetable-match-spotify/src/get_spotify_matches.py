#!/usr/bin/env python3.13

"""
Code to compare artists from liked spotify songs with artists from fusion festival timetable. 

For infos on how to prepare spotipy, check https://spotipy.readthedocs.io/en/2.25.1/ (esp. at SpotifyOAuth)

Usage: get_spotify_mathces.py -i spotify_clientinfo.yaml
"""

import json 
import spotipy
import yaml
import argparse

import urllib.request
from spotipy.oauth2 import SpotifyOAuth
import numpy as np

def get_fusion_timetable_json(url):
    """Reads timetable json from fusion festival website.
    Parameters
    ---------
        url : str 
            url of file
    """
    body = urllib.request.urlopen(url).read()
    decoded_body = body.decode('unicode_escape')

    # remove js code before actual json data
    code_before_json = "JSON.parse(\'"
    jsonstart_index = decoded_body.find(code_before_json)
    json_data = decoded_body[jsonstart_index+len(code_before_json): ]

    # remove js code after actual json data
    json_data = json_data.replace("\')}}]);", "")

    return json.loads(json_data)

def get_spotify_likedsong_artists(client_id, client_secret):

    """Reads timetable json from fusion festival website.
    Parameters
    ---------
        client_id : str 
            client_id from spotify for authentication
        client_secret : str
            client_secret from spotify for authentication
    """

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                client_secret=client_secret,
                                                redirect_uri="http://example.com/callback/",
                                                scope="user-library-read"))
    liked_artists = []

    max_number = 10000
    print("[INFO] Start getting liked song info from Spotify...")
    for offset in np.arange(0, max_number, 50): 
        results = sp.current_user_saved_tracks(limit=50, offset=offset) # can only request max. 50 at once
        if len(results['items']) > 0:
            for idx, item in enumerate(results['items']):
                track = item['track']
                liked_artists += [track['artists'][0]['name']]
        else:
            print(f"[INFO] Done! Got {len(liked_artists)} liked songs. \n" )
            break
    
    return liked_artists

def main(url, spotify_client_id, spotify_client_secret):
    """Compares artists in fusion fesitval timetable with artists from spotify liked songs.
    Parameters
    ---------
        url : str
            url of fusion festival timetable data
        client_id : str 
            client_id for spotify authentication
        client_secret : str
            client_secret for spotify authentication
    """
    ## Get fusion artists
    data = get_fusion_timetable_json(url)

    fusion_artists = []
    for d in data: 
        fusion_artists += [d['artist']]
    fusion_artists = [f.lower() for f in fusion_artists]
    
    ## Get liked artists
    liked_artists = get_spotify_likedsong_artists(client_id=spotify_client_id, client_secret=spotify_client_secret)
    liked_artists = [f.lower() for f in liked_artists]

    ## overlap
    overlap = set(fusion_artists) & set(liked_artists)
    
    print(f"Artists at Fusion Festival and in Spotify liked songs: \n {overlap}")


if __name__ == "__main__":

    FUSION_FESTIVAL_URL = "https://timetable.fusion-festival.de/static/js/346.003d780e.chunk.js"

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infilename", help="yaml file with spotify client id and secret", required=True)
    args = parser.parse_args()

    with open(args.infilename, 'r') as file:
        spotify_params = yaml.safe_load(file)

    client_id = spotify_params['CLIENT_ID']
    client_secret = spotify_params['CLIENT_SECRET']

    main(FUSION_FESTIVAL_URL, client_id, client_secret)