from .config import Config, SpotifyConfig, YouTubeConfig

__all__ = ['configuration', 'Config', 'SpotifyConfig', 'YouTubeConfig']

global configuration

configuration = Config()
