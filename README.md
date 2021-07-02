# Fetcher
Fetcher helps you to watch YouTube videos in your native video player on your computer.

Fetcher is built upon the Pafy framework to interact with YouTube videos.

Fetching video urls based on a list of video urls in .csv files. 
Fetcher looks for any valid YouTube urls and ignores any other text, so feel free to organize your CSV list with plaintext headings.

Fetcher uses multithreading with a default maximum workers of 5, but that can be changed within fetch.py. 


## Setup
* Create a virtual environment and install the requirements.
    * python -m venv venv
    * pip install -r requirements.txt


## Usage:
#### Spreadsheet (Default Setting):
* Place a CSV file in the root directory of the project (where main.py is located).

* Run main.py.

* Fetcher will create a directory for each CSV file in the root directory.

* Run your native video player to access the video files in each directory.

#### GUI (In Development)
* run fetch.py from the command line.
* Note: GUI still under development and does not show progress. For monitoring purposes, watch the console to make sure 
everything is going well.

#### Fetch All Files
* run fetch.py from the command line with the -c or --cl flag to run Fetcher from the command line.
* Note: If you're running into issues with the GUI, or want faster performance, the command line mode may help.

#### Single File (from command line)
* run main.py from the command line with the -u or --url flag to specify a URL.
    * ex: python main.py -u https://www.youtube.com/watch?v=xQJ-3PbJoYY

#### Spreadsheet (from command line)
* run main.py from the command line with the -f or --file flag to specify a spreadsheet file.
    * ex: python main.py -f video_list.csv


## Technical Tips:
The url detection is handled in fetcher.fetch.read_spreadsheet(). It matches based on string.startswith(),
so if you run into errors with Fetcher detecting headings as urls, check that piece out.

fetch.py is the main module, which accesses file_actions to handle the spreadsheet and video_actions to interact with the video object.


