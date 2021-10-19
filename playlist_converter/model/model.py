import re
from typing import List


class Artist:

    def __init__(self, name: str):
        self.name = name


class YouTubeVideo:

    def __init__(self, title: str, video_id: str, video_link: str):
        self.title = title
        self.video_id = video_id
        self.url = video_link


class Track:

    def __init__(self, name: str, artists: List[Artist], youtube_video: YouTubeVideo = None):
        self.name = name
        self.artists = artists
        self.youtube_video = youtube_video

    def get_name_and_artists_as_string(self) -> str:
        return self.get_all_artist_names_as_string() + ' - ' + self.name

    def get_all_artist_names_as_string(self) -> str:
        number_of_artists_for_track = len(self.artists)
        names = ''

        for index, artist in enumerate(self.artists):
            if number_of_artists_for_track == 1:
                names = artist.name
            elif number_of_artists_for_track > 1:
                if index == 0:
                    names = artist.name
                elif index > 0 & index <= number_of_artists_for_track:
                    names += ' & ' + artist.name

        return names


class Playlist:

    def __init__(self, name: str, description: str, tracks: List[Track]):
        self.name = name
        self.description = description
        self.tracks = tracks

    def get_all_track_urls(self) -> List[str]:
        urls = []
        for track in self.tracks:
            urls.append(track.youtube_video.url)

        return urls
