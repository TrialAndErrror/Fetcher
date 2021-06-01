import sys

from src.fetch import fetch, download_single_video, download_all_videos
from src.args import parse_args
from src.debug_tools import timer, report_success_or_failure


@timer
def fetch_with_timer():
    """
    Start logging and fetch. Wrapper is timer from src.fetcher.debug_tools

    :return: None
    """
    args = parse_args()
    if args.get("url", False):
        download_single_video(args["url"])
    else:
        if args.get("file", False):
            download_all_videos([args["file"]])
        else:
            num_sheets, num_videos = fetch()
            report_success_or_failure(num_sheets, num_videos)


if __name__ == '__main__':
    """
    This is the main entry point of Fetcher.
    
    Use 'python3 main.py' to run Fetcher from the command line.
    
    If you want to import Fetcher into your project,
    you can import src.fetcher.fetch.fetch directly to get the main
    functionality. Other modules can be imported as necessary.
    """
    fetch_with_timer()
