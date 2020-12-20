# Fetcher
Fetcher helps you to watch YouTube videos in your native video player on your computer.

Fetcher is built upon the PyTube framework to interact with YouTube videos.

Fetching video urls based on a list of video urls in .csv files. Fetcher looks for any values longer than 25 characters, so make sure any headings or organization are less than that length.

Fetcher uses multithreading with a default maximum workers of 5, but that can be changed within fetch.py. 

## Usage:
Place a CSV file in the root directory of the project (where main.py is located).

Run main.py.

Fetcher will create a directory for each CSV file in the root directory.

Run your native video player to access the video files in each directory.

