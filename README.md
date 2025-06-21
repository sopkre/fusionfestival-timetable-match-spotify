# fusionfestival-timetable-match-spotify
Snippet to compare artists from fusion festival timetable with artists from ones spotify liked songs.

## Usage 

```
get_spotify_matches.py -i <spotify-clientinfo-yaml>
```

The spotify client info, i.e. the spotify client id and secret, need to be set in an input yaml-file, just follow the syntax in the provided ```example_spotify.yaml```

For infos on how to prepare spotipy, check https://spotipy.readthedocs.io/en/2.25.1/ (esp. the part on SpotifyOAuth)
