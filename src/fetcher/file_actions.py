import os
import logging


def find_files():
    """
    Generates list of CSV files in current working directory.

    :return: (files_found: bool; files_list: list)
    """

    try:
        home_dir = os.listdir()
    except Exception as e:
        logging.warning('Error reading files in home directory')
        logging.warning(f'Error was {e}')
    else:
        files_list = [file for file in home_dir if file[-4:] == '.csv']
        files_found = bool(len(files_list) > 0)
        return files_found, files_list


def read_list_path(path):
    """
    Reads CSV file located at path param and returns all video files contained within

    :param path: str
    :return: current_video_files: list[str]
    """

    try:
        current_video_files = find_youtube_links(path)
    except Exception as e:
        logging.warning('Could not read file')
        logging.warning(f'Error: {e}')
    else:
        log_empty_video_list(current_video_files)
        return current_video_files


def find_youtube_links(path):
    youtube_prefix = 'https://www.youtube.com/watch'
    with open(path) as file:
        current_video_files = get_video_links_from_sheet(file, youtube_prefix)
    return current_video_files


def log_empty_video_list(current_video_files):
    is_files_found = bool(len(current_video_files) > 0)
    if not is_files_found:
        logging.warning('No video links found')


def get_video_links_from_sheet(file, youtube_prefix):
    item_list = file.read().split(',')
    entry_list = [item.replace('\n', '') for item in item_list]
    current_video_files = [item for item in entry_list if item.startswith(youtube_prefix)]
    return current_video_files
