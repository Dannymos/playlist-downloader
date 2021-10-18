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

        # Get required YouTube variables
        self.youtube = YouTubeConfig(
            os.environ.get('YOUTUBE_DEVELOPER_KEY'),
            os.environ.get('YOUTUBE_API_SERVICE_NAME'),
            os.environ.get('YOUTUBE_API_VERSION'))


class SpotifyConfig:

    def __init__(self, plid: str, clid: str, clst: str):
        self.playlist_id = plid
        self.client_id = clid
        self.client_secret = clst


class YouTubeConfig:

    def __init__(self, dvky: str, api_name: str, api_version):
        self.developer_key = dvky
        self.api_service_name = api_name
        self.api_version = api_version
