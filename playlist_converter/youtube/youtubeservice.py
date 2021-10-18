import logging
import time

from youtubesearchpython import VideosSearch

from playlist_converter.model.model import YouTubeVideo


class YouTubeService:
    def __init__(self):
        self._logger = logging.getLogger(__name__)

    def search_youtube(self, search_query: str, max_results: int = 1) -> YouTubeVideo:
        video_search = VideosSearch(search_query, max_results)
        search_result = video_search.result()['result']
        youtube_video = self._map_search_result_to_model(search_result[0])

        return youtube_video

    def _map_search_result_to_model(self, video_search_result: dict):
        return YouTubeVideo(
            title=video_search_result['title'],
            video_id=video_search_result['id'],
            video_link=video_search_result['link'])
