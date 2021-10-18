from setuptools import setup, Command

start_command = 'playlist-converter'

setup(
    name='playlist-converter',
    version='0.0.1',
    packages=['playlist_converter'],
    install_requires=[
        'importlib; python_version == "3.9"',
    ],
    entry_points={
        "console_scripts": [
            start_command + " = playlist_converter:main",
        ]
    },
)
