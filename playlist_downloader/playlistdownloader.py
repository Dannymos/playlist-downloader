import logging
from typing import List

from playlist_downloader.utils import progress_bar_handler
from playlist_downloader.spotify import SpotifyService
from playlist_downloader.youtube import YouTubeService
from playlist_downloader.config import Config
from playlist_downloader.model import Track


class PlaylistDownloader:
    def __init__(self, configuration: Config):
        self._logger = logging.getLogger(__name__)
        self._spotify_service = SpotifyService(configuration.spotify)
        self._youtube_service = YouTubeService(configuration.youtube)
        self._progress_bar_handler = progress_bar_handler

    def convert_spotify_playlist(self) -> None:
        playlist = self._spotify_service.get_playlist_from_spotify()
        self._logger.info(
            'Playlist found: [' + playlist.name + '] with [' + str(len(playlist.tracks)) + '] tracks')
        tracks_with_video = self._get_youtube_video_for_tracks_in_playlist(playlist.tracks)
        playlist.tracks = tracks_with_video
        self._download_youtube_video_for_tracks_in_playlist(playlist.tracks)
        self._logger.info('Done, exiting...')

    def _get_youtube_video_for_tracks_in_playlist(self, tracklist: List[Track]) -> List[Track]:
        self._progress_bar_handler.create(
            total=len(tracklist),
            description='Fetching YouTube URLs []',
            unit=' tracks')
        for track in tracklist:
            result = self._youtube_service.find_youtube_video(
                search_query=track.get_name_and_artists_as_string())

            if result is not None:
                track.youtube_video = result
            else:
                self._progress_bar_handler.print_message(
                    'Could not find video for [' + track.get_name_and_artists_as_string() + ']')

            self._progress_bar_handler.update(
                increment=1,
                description='Fetching YouTube URLs [' + track.name)

        self._progress_bar_handler.close()
        self._logger.info('Done fetching YouTube urls!')

        return tracklist

    def _download_youtube_video_for_tracks_in_playlist(self, tracks: List[Track]):
        self._progress_bar_handler.create(
            total=len(tracks),
            description='Downloading YouTube videos [',
            unit=' tracks')

        for track in tracks:
            self._youtube_service.download_youtube_video_for_track(track)
            self._progress_bar_handler.update(
                increment=1,
                description='Downloading YouTube videos [' + track.name)

        self._progress_bar_handler.close()
        self._logger.info('Done downloading YouTube videos!')
