from setuptools import setup, Command

start_command = 'playlist-downloader'

setup(
    name='playlist-downloader',
    version='1.0.1',
    packages=['playlist_downloader'],
    install_requires=[
        'importlib; python_version == "3.9"',
    ],
    entry_points={
        "console_scripts": [
            start_command + " = playlist_downloader:main",
        ]
    },
)
