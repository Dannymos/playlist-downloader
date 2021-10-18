import logging
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
from typing import List

from playlist_converter.utils import progress_bar_handler
from playlist_converter.config import SpotifyConfig
from playlist_converter.model import Playlist, Track, Artist

class SpotifyService:

    def __init__(self, config: SpotifyConfig):
        self._logger = logging.getLogger(__name__)
        self._progress_bar_handler = progress_bar_handler
        self._spotify_config = config
        self._spotipy_client = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=self._spotify_config.client_id,
                client_secret=self._spotify_config.client_secret))

    def _get_playlist_tracks_from_spotify(self) -> List[Track]:
        playlist_tracks = self._spotipy_client.playlist_items('spotify:playlist:' + self._spotify_config.playlist_id,
                                                              fields='items.track.name,items.track.artists.name',
                                                              additional_types=['track'])

        if len(playlist_tracks['items']) == 0:
            raise Exception('No tracks found')

        self._progress_bar_handler.update(increment=1)
        return self._map_api_response_to_list_of_tracks(playlist_tracks['items'])

    def get_playlist_from_spotify(self) -> Playlist:
        self._progress_bar_handler.create(total=3,
                                          description='Fetching Spotify playlist [' + self._spotify_config.playlist_id + ']',
                                          unit=' steps')
        playlist = self._spotipy_client.playlist('spotify:playlist:' + self._spotify_config.playlist_id,
                                                 fields='name,description')

        self._progress_bar_handler.update(increment=1)
        tracks = self._get_playlist_tracks_from_spotify()

        self._progress_bar_handler.update(increment=1)
        self._progress_bar_handler.close()
        self._progress_bar_handler.print_message('Playlist found: [' + playlist['name'] + '] with [' + str(len(tracks)) + '] tracks')

        return Playlist(playlist['name'], playlist['description'], tracks)

    def _map_api_response_to_list_of_tracks(self, tracks: List) -> List[Track]:
        tracklist = []
        for track in tracks:
            readable_track = self._map_api_track_to_model(track['track']['name'], track['track']['artists'])
            tracklist.append(readable_track)

        return tracklist

    @staticmethod
    def _map_api_track_to_model(track_name: str, artists: str) -> Track:
        track_name = track_name
        track_artists = []
        for artist in artists:
            track_artists.append(Artist(artist['name']))

        return Track(track_name, track_artists)
