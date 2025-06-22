# fusionfestival-timetable-match-spotify
This code snippet compares artists from the Fusion Festival timetable with artists from one's Spotify liked songs.

## Usage 

```
get_spotify_matches.py -i <spotify-clientinfo-yaml>
```

The spotify client info, i.e. the spotify client id and secret, need to be set in an input yaml-file, just follow the syntax in the provided ```example_spotify.yaml```

For infos on how to prepare spotipy, check https://spotipy.readthedocs.io/en/2.25.1/ (esp. the part on SpotifyOAuth). As redirect URI, use ```https://example.com/callback/```. 
