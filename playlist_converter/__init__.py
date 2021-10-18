import logging
import sys
import traceback
from pprint import pprint

from .utils import PlaylistConverterException, MissingEnvironmentVariableException, ProgressBarHandler
from .playlistconverter import PlaylistConverter
from .config import configuration

__all__ = ['utils',
           'model',
           'PlaylistConverter',
           'PlaylistConverterException',
           'MissingEnvironmentVariableException',
           'ProgressBarHandler']


def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')

    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)


def main() -> None:
    try:
        setup_logger()
        _real_main()
    except KeyError:
        sys.exit('Please set the all the required environment variables, and rerun the program')
    except PlaylistConverterException as exception:
        pprint(exception.message)
        sys.exit(exception.traceback)
    except KeyboardInterrupt:
        sys.exit('\nERROR: Interrupted by user')
    except Exception:
        pprint(traceback.format_exc())


def _real_main() -> None:
    playlist_converter = PlaylistConverter(configuration)
    playlist_converter.convert_spotify_playlist()
