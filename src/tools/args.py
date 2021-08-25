import argparse


def parse_args():
    """
    Adds support for command-line arguments.
    -f and -u require a paramter after (to indicate the filename or url desired),
    -a and -g will store True when provided, so no need for parameters.

    :return: dict
    """
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", required=False, help="Spreadsheet File Path")
    ap.add_argument("-u", "--url", required=False, help="Single File URL")
    ap.add_argument("-a", "--audio", required=False, action="store_true", help="Download Audio Only")
    ap.add_argument("-c", "--cl", required=False, action="store_true", help="Run Fetcher without GUI (faster performance)")

    args = vars(ap.parse_args())

    return args
