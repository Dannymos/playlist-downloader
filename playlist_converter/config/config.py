import os

from dotenv import load_dotenv

class Config:

    def __init__(self):
        if not load_dotenv():
            raise Exception('Something went wrong reading the environment variables')

        # Get required Spotify variables
        self.spotify = SpotifyConfig(
            os.environ.get('SPOTIFY_PLAYLIST_ID'),
            os.environ.get('SPOTIFY_CLIENT_ID'),
            os.environ.get('SPOTIFY_CLIENT_SECRET'))

        self.youtube = YoutubeDLConfig({
            'format': 'm4a',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio'
            }],
            'quiet': True,
            'no_warnings': True,
            'no-progress': True,
            'progress': False,
        })


class SpotifyConfig:

    def __init__(self, plid: str, clid: str, clst: str):
        self.playlist_id = plid
        self.client_id = clid
        self.client_secret = clst


class YoutubeDLConfig:

    def __init__(self, options: dict):
        self.options = options
