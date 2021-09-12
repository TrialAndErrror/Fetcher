from src.commands import run_single_sheet, run_single_url, run_fetch
from src.tools.args import parse_args
from src.tools.debug_tools import timer, report_success_or_failure


@timer
def fetch_with_timer():
    """
    Start logging and fetch. This is the main function that runs Fetcher.

    :return: None
    """
    args = parse_args()
    """
    Fetcher operates in three different ways. You can select a mode by including the flags and required parameters.
    
    Option 1: Download Single URL
    Option 2: Download Single Spreadsheet
    Option 3: Fetch (Download All Spreadsheets in Root Directory)

    """

    if args.get("cl", False):
        """
        Option 1: Command Line Fetch (Download All Spreadsheets in Root Directory)
        """
        num_videos = run_fetch(args)
        report_success_or_failure(num_videos)

        """
        note: "audio" parameter indicates to only download audio.
        On command line, this is accessible from -a or --audio
        """

    elif args.get("url", False):
        """
        Option 2: Download Single URL
        Flags: -u, --url
        Example: python fetch.py -u 'https://www.youtube.com/watch?v=6W7HDm9Ja2Q'
        """
        run_single_url(args.get('url'), args.get('audio', False))
        print(f'\nSuccess! Downloaded {args["url"]}.')

    elif args.get("file", False):
        """
        Option 3: Download Single Spreadsheet
        Flags: -f, --file
        Example: python fetch.py -f 'videos.csv'
        """
        num_videos = run_single_sheet(args.get('file'), args.get('audio'))
        report_success_or_failure(num_videos)


if __name__ == '__main__':
    """
    This is the main entry point of Fetcher.
    
    Use 'python3 main.py' to run Fetcher from the command line.
    
    If you want to import Fetcher into your project,
    you can import the individual functions from src.commands.py
    """
    fetch_with_timer()
