# Fetcher
Fetcher helps you to watch YouTube videos in your native video player on your computer.

Fetcher is built upon the Pafy framework to interact with YouTube videos, with some Playlist handling
done by the PyTube library.

Fetching video urls based on a list of video urls in .csv files. 
Fetcher looks for any valid YouTube urls and ignores any other text, so feel free to organize your CSV
list with plaintext headings.

Fetcher uses multithreading with a default maximum workers of 5.

## Setup:
* Create a virtual environment and install the requirements.
    * python -m venv venv
    * pip install -r requirements.txt


## Usage:
#### Spreadsheet (Default Setting):
* Place a CSV file in the root directory of the project (where fetch.py is located).

* Run fetch.py.

* Fetcher will create a directory for each CSV file in the root directory.

* Run your native video player to access the video files in each directory.


#### GUI (In Development)
* run main.py from the command line with the -g or --gui flag to show the GUI and manually enter data.
    * ex: python main.py -g
* Note: GUI still under development. If your files are downloading slowly, try cancelling the download and restart the process.



#### Fetch All Files
* run fetch.py from the command line with the -c or --cl flag to run Fetcher from the command line.
* Note: If you're running into issues with the GUI, or want faster performance, the command line mode may help.

#### Single File (from command line)
* run main.py from the command line with the -u or --url flag to specify a URL.
    * ex: python main.py -u https://www.youtube.com/watch?v=xQJ-3PbJoYY

#### Spreadsheet (from command line)
* run main.py from the command line with the -f or --file flag to specify a spreadsheet file.
    * ex: python main.py -f video_list.csv

#### Audio Only (from command line)
* run main.py from the command line with the -a or --audio flag to indicate that you only want audio.
    * ex: python main.py -u https://www.youtube.com/watch?v=xQJ-3PbJoYY -a 
    * ex: python main.py -f video_list.csv --audio

## Technical Tips:
The url detection is handled in src.file_actions.find_youtube_links(). It matches based on string.startswith(),
so if you run into errors with Fetcher detecting headings as urls, make sure that your YouTube links start with
the same string that is indicated in the YT_PREFIX global variable in src.file_actions



