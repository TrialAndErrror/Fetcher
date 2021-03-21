from src.fetch import fetch
from src.debug_tools import timer, start_logging


@timer
def fetch_with_timer():
    """
    Start logging and fetch. Wrapper is timer from src.fetcher.debug_tools

    :return: None
    """
    start_logging()
    num_sheets, num_videos = fetch()
    print_missing_sheets_or_videos(num_sheets, num_videos)


def print_missing_sheets_or_videos(num_sheets, num_videos):
    if num_sheets > 0 and num_videos > 0:
        print(f'\n\nSuccess! {num_sheets} sheets processed, downloading {num_videos} videos.')
    else:
        print(f'Uh-oh, something went wrong!')
        if num_sheets == 0:
            print('No sheets detected. Make sure you put valid csv files in the root directory.')
            if num_videos > 0:
                print(f'Weird, I still downloaded {num_videos} videos...')
        elif num_videos == 0:
            print('No videos detected. Make sure your csv files have vaild youtube links in them.')
            if num_sheets > 0:
                print(f'I did see {num_sheets} sheets in the directory, but couldn\'t find any video links')


if __name__ == '__main__':
    """
    This is the main entry point of Fetcher.
    
    Use 'python3 main.py' to run Fetcher from the command line.
    
    If you want to import Fetcher into your project,
    you can import src.fetcher.fetch.fetch directly to get the main
    functionality. Other modules can be imported as necessary.
    """
    fetch_with_timer()
