from src.fetch import fetch
from src.commands import run_single_sheet, run_single_url
from src.tools.args import parse_args
from src.tools.debug_tools import timer, report_success_or_failure
from src.gui.gui_tools import run_gui


@timer
def fetch_with_timer():
    """
    Start logging and fetch. This function is the heart of the commmand-line prompt.
    Wrapper is timer from src.tools.debug_tools

    :return: None
    """

    args = parse_args()
    print(args)

    if args.get("gui", False):
        """
        -g, -gui flag:
        Run graphical interface.
        """
        run_gui()

    elif args.get("url", False):
        """
        -u, -url flag:
        Download single url.
        """
        run_single_url(args)
        print(f'\nSuccess! Downloaded {args["url"]}.')
    else:
        if args.get("file", False):
            """
            -f, --file flag:
            Download single sheet of urls.
            """
            num_sheets, num_videos = run_single_sheet(args)
        else:
            """
            No flags:
            Download all sheets found in root directory.
            """
            num_sheets, num_videos = fetch(audio=args.get("audio", False))
            """
            note: "audio" parameter indicates to only donwload audio.
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
