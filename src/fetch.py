import logging

from .commands import run_fetch
from .file_actions import find_files


def fetch(audio=False):
    """
    Perform Video Fetch.

    audio is optional param that indicates whether to just download audio.
    :return: None
    """
    files_found, files_list = find_files()
    num_sheets = 0
    num_videos = 0
    if files_found:
        logging.info(f'Files list: {files_list}')
        num_sheets, num_videos = run_fetch(files_list, audio=audio)
    else:
        logging.warning('No files found; please place CSV files in this directory')
    return num_sheets, num_videos