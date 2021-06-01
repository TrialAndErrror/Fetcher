from src.fetch import fetch, run_single_sheet, run_single_file
from src.args import parse_args
from src.debug_tools import timer, report_success_or_failure
from src.gui_src import run_gui


@timer
def fetch_with_timer():
    """
    Start logging and fetch. Wrapper is timer from src.fetcher.debug_tools

    :return: None
    """

    args = parse_args()
    print(args)

    if args.get("gui", False):
        run_gui()

    elif args.get("url", False):
        run_single_file(args)
        print(f'\nSuccess! Downloaded {args["url"]}.')
    else:
        if args.get("file", False):
            num_sheets, num_videos = run_single_sheet(args)
        else:
            num_sheets, num_videos = fetch(audio=args.get("audio", False))
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
