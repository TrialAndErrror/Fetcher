import os
import logging

YT_PREFIX = 'https://www.youtube.com/watch'


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
        files_list = [file for file in home_dir if file.endswith('.csv')]
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
        logging.warning(f'Could not read file; Error: {e}')
    else:
        log_empty_video_list(current_video_files)
        return current_video_files


def find_youtube_links(path):
    """
    Matches youtube prefix to return a list of video links.

    :param path: str
    :return: current_video_files: list
    """
    try:
        with open(path) as file:
            current_video_files = get_video_links_from_sheet(file, YT_PREFIX)
    except Exception as e:
        logging.warning(f'Error opening {path} as file; error {e}')
    else:
        return current_video_files


def log_empty_video_list(current_video_files):
    """
    Check to see if video list if empty. If so, log it.

    :param current_video_files: list
    :return: None
    """
    is_files_found = bool(len(current_video_files) > 0)
    if not is_files_found:
        logging.warning('No video links found')


def get_video_links_from_sheet(file, youtube_prefix):
    """
    Get list of entries to check against youtube_prefix parameter.

    :param file: file
    :param youtube_prefix: str
    :return: current_video_files: list
    """
    entry_list = get_link_entry_list(file)
    current_video_files = [item for item in entry_list if item.startswith(youtube_prefix)]
    return current_video_files


def get_link_entry_list(file):
    """
    Reformat items in entry list and remove newline characters.
    :param file: file
    :return: entry_list: list
    """
    try:
        item_list = file.read().replace('\n', ',').split(',')
        item_list = [item.strip(' " " ') for item in item_list]
    except Exception as e:
        logging.warning(f'Error reading file; error {e}')
    else:
        entry_list = [entry for entry in item_list if len(entry) > len(YT_PREFIX)]
        return entry_list


def read_spreadsheet(file):
    """
    Returns output directory and list of video files from the spreadsheet.

    :param file:
    :return: str, list
    """
    output_dir_name = file[:-4]
    all_cells = read_list_path(file)
    current_video_files = [item for item in all_cells if item.startswith('https://www.youtube.com/watch')]
    return output_dir_name, current_video_files