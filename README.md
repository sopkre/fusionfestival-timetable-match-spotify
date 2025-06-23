# fusionfestival-timetable-match-spotify
This code snippet compares artists from the Fusion Festival timetable with artists from one's Spotify liked songs or created playlists. 

## Usage 

```
get_spotify_matches.py [-h] -i INFILENAME (--playlists | --likes )
```

The option ```--playlists``` uses the artists in your own created playlists and the option ```--likes``` from your liked songs.

The required INFILENAME needs your spotify client info, i.e. the spotify client id and secret (see below), set in an input yaml-file - just follow the syntax in the provided ```example_spotify.yaml```

For using spotipy here, you need to add an app to the https://developer.spotify.com/dashboard/applications and set the callback URI to ```https://example.com/callback/``` - from this app, you also get the client ID and secret. More info can be found at https://spotipy.readthedocs.io/en/2.25.1/ (esp. at the part about SpotifyOAuth). 
