import argparse


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--file", required=False, help="Spreadsheet File Path")
    ap.add_argument("-u", "--url", required=False, help="Single File URL")

    args = vars(ap.parse_args())

    return args