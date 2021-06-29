from src.commands import run_single_sheet, run_single_url, run_fetch
from src.tools.args import parse_args
from src.tools.debug_tools import timer, report_success_or_failure
from src.gui.gui_tools import run_gui


@timer
def fetch_with_timer():
    """
    Start logging and fetch. This is the main function that runs Fetcher.

    :return: None
    """
    args = parse_args()
    print(args)

    """
    Fetcher operates in four different ways. You can select a mode by including the flags and required parameters.
    
    Option 1: Graphical User Interface mode
    Option 2: Download Single URL
    Option 3: Download Single Spreadsheet
    Option 4: Fetch (Download All Spreadsheets in Root Directory)
    
    Note: Option 1 (GUI) includes radio buttons for selecting options 2-4.
    """

    if args.get("gui", False):
        """
        Option 1: Graphical User Interface mode
        Flags: -g, --gui
        Example: python fetch.py -g
        """
        run_gui()

    elif args.get("url", False):
        """
        Option 2: Download Single URL
        Flags: -u, --url
        Example: python fetch.py -u 'https://www.youtube.com/watch?v=6W7HDm9Ja2Q'
        """
        run_single_url(args)
        print(f'\nSuccess! Downloaded {args["url"]}.')
    else:
        if args.get("file", False):
            """
            Option 3: Download Single Spreadsheet
            Flags: -f, --file
            Example: python fetch.py -f 'videos.csv'
            """
            num_sheets, num_videos = run_single_sheet(args)
        else:
            """
            Option 4: Fetch (Download All Spreadsheets in Root Directory)
            Flags: None
            Example: python fetch.py
            """
            num_sheets, num_videos = run_fetch(audio=args.get("audio", False))
            """
            note: "audio" parameter indicates to only download audio.
            On command line, this is accessible from -a or --audio
            """

        report_success_or_failure(num_sheets, num_videos)


if __name__ == '__main__':
    """
    This is the main entry point of Fetcher.
    
    Use 'python3 main.py' to run Fetcher from the command line.
    
    If you want to import Fetcher into your project,
    you can import src.fetch.fetch directly to get the main
    functionality. Other modules can be imported as necessary.
    """
    fetch_with_timer()
