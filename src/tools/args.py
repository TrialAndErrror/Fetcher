import argparse


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", required=False, help="Spreadsheet File Path")
    ap.add_argument("-u", "--url", required=False, help="Single File URL")
    ap.add_argument("-a", "--audio", required=False, action="store_true", help="Download Audio Only")
    ap.add_argument("-g", "--gui", required=False, action="store_true", help="Run GUI for downloading files")

    args = vars(ap.parse_args())

    return args
