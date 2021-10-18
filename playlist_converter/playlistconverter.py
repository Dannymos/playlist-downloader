import logging

from playlist_converter.utils import progress_bar_handler
from playlist_converter.spotify import SpotifyService
from playlist_converter.youtube import YouTubeService
from playlist_converter.config import Config


class PlaylistConverter:
    def __init__(self, configuration: Config):
        self._logger = logging.getLogger(__name__)
        self._spotify_service = SpotifyService(configuration.spotify)
        self._youtube_service = YouTubeService(configuration.youtube)
        self._progress_bar_handler = progress_bar_handler

    def convert_spotify_playlist(self) -> None:
        spotify_playlist = self._spotify_service.get_playlist_from_spotify()

        self._progress_bar_handler.create(
            total=len(spotify_playlist.tracks),
            description='Fetching YouTube URLs []',
            unit=' tracks')
        for index, track in enumerate(spotify_playlist.tracks, start=0):
            result = self._youtube_service.search_youtube(
                search_query=track.get_name_and_artists_as_string())

            if result is not None:
                track.youtube_video = result
            else:
                self._progress_bar_handler.print_message('Could not find video for [' + track.get_name_and_artists_as_string() + ']')
            self._progress_bar_handler.update(
                increment=1,
                description='Fetching YouTube URLs [' + track.name)
        self._progress_bar_handler.close()
