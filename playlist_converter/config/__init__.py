from .config import Config, SpotifyConfig, YoutubeDLConfig

__all__ = ['configuration', 'Config', 'SpotifyConfig', 'YoutubeDLConfig']

global configuration

configuration = Config()
