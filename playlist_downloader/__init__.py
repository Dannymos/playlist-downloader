import getopt, sys
import logging
import sys
import traceback
from pprint import pprint

from .utils import PlaylistDownloaderException, MissingEnvironmentVariableException, ProgressBarHandler
from .playlistdownloader import PlaylistDownloader
from .config import configuration

__all__ = ['utils',
           'model',
           'PlaylistDownloader',
           'PlaylistDownloaderException',
           'MissingEnvironmentVariableException',
           'ProgressBarHandler']


def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(levelname)s]: %(message)s')

    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


def parse_arguments():
    opts, args = getopt.getopt(sys.argv[1:], "p:", ["playlist-id="])
    for o, a in opts:
        if o == 'p' or o == '--playlist-id':
            configuration.spotify.playlist_id = a




def main() -> None:
    try:
        setup_logger()
        parse_arguments()
        _real_main()
    except KeyError:
        sys.exit('Please set the all the required environment variables, and rerun the program')
    except getopt.GetoptError as err:
        sys.exit('No valid playlist id provided, please provide a valid playlist as an argument ( -p or '
                 '--playlist-id)')
    except KeyboardInterrupt:
        sys.exit('\nERROR: Interrupted by user')
    except Exception:
        pprint(traceback.format_exc())


def _real_main() -> None:
    playlist_converter = PlaylistDownloader(configuration)
    playlist_converter.convert_spotify_playlist()
