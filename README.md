# Playlist downloader
This script allows you to download spotify playlists by searching YouTube for video's matching the tracks in the playlist, and downloading them.

####Setup

Create a .env file and add the following variables as per the example.env:

```
SPOTIFY_CLIENT_ID=YOURSPOTIFYAPICLIENTID
SPOTIFY_CLIENT_SECRET=YOURSPOTIFYAPICLIENTSECRET
```

Install the required dependencies by executing the following command in the application root directory:

``pip install -r requirements.txt``

Run setup.py to register the starting command:

``python setup.py install``

####Running the application

To run the application execute the following command:

``py -m playlist_downloader --playlist-id YOURPLAYLISTID``

Or

``py -m playlist_downloader -p YOURPLAYLISTID``
