import logging
import mutagen
import yt_dlp
from youtubesearchpython import VideosSearch

from playlist_converter.model.model import YouTubeVideo, Track
from playlist_converter.config.config import YoutubeDLConfig


class YouTubeService:
    def __init__(self, config: YoutubeDLConfig):
        self._logger = logging.getLogger(__name__)
        self.youtube_dl_options = config.options

    def find_youtube_video(self, search_query: str, max_results: int = 1) -> YouTubeVideo:
        video_search = VideosSearch(search_query, max_results)
        search_result = video_search.result()['result']
        youtube_video = self._map_search_result_to_model(search_result[0])

        return youtube_video

    def download_youtube_video_for_track(self, track: Track) -> None:
        self.youtube_dl_options['outtmpl'] = '/downloads/' + track.get_name_and_artists_as_string() + '.%(ext)s'
        try:
            with yt_dlp.YoutubeDL(self.youtube_dl_options) as ydl:
                ydl.download([track.youtube_video.url])
                self._write_metatags_to_file(track)
        except Exception:
            pass

    @staticmethod
    def _map_search_result_to_model(video_search_result: dict):
        return YouTubeVideo(
            title=video_search_result['title'],
            video_id=video_search_result['id'],
            video_link=video_search_result['link'])

    def _write_metatags_to_file(self, track: Track):
        mutafile = mutagen.File(
           './downloads/' + track.get_name_and_artists_as_string() + '.m4a',
            easy=True)
        mutafile['title'] = track.name
        mutafile['artist'] = track.get_all_artist_names_as_string()
        mutafile.save()
