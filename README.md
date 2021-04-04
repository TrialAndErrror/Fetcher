# Fetcher
Fetcher helps you to watch YouTube videos in your native video player on your computer.

Fetcher is built upon the PyTube framework to interact with YouTube videos.

Fetching video urls based on a list of video urls in .csv files. 
Fetcher looks for any valid YouTube urls and ignores any other text, so feel free to organize your CSV list with plaintext headings.

Fetcher uses multithreading with a default maximum workers of 5, but that can be changed within fetch.py. 

## Usage:
Place a CSV file in the root directory of the project (where main.py is located).

Run main.py.

Fetcher will create a directory for each CSV file in the root directory.

Run your native video player to access the video files in each directory.

## Audio Files:
If you wish to capture audio only, add the prefix [AUDIO] to the filename of your CSV file; Fetcher will recognize this
tag and only download the audio from the URLs. Currently it still downloads them as mp4 files, but with no video, thus
reducing the file size.

## Technical Tips:
The url detection is handled in fetcher.fetch.read_spreadsheet(). It matches based on string.startswith(),
so if you run into errors with Fetcher detecting headings as urls, check that piece out.

fetch.py is the main module, which accesses file_actions to handle the spreadsheet and video_actions to interact with the video object.


