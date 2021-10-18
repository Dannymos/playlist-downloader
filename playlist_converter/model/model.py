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
        number_of_loops = 0
        names = ''

        for artist in self.artists:
            if number_of_artists_for_track == 1:
                names = artist.name
            elif number_of_artists_for_track > 1:
                if number_of_loops == 0:
                    names = artist.name
                elif number_of_loops > 0 & number_of_loops <= number_of_artists_for_track:
                    names += ' & ' + artist.name
            number_of_loops += 1

        return names


class Playlist:

    def __init__(self, name: str, description: str, tracks: List[Track]):
        self.name = name
        self.description = description
        self.tracks = tracks
