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
        with open(path) as file:
            current_video_files = file.read().split(',')
    except Exception as e:
        logging.warning('Could not read file')
        logging.warning(f'Error: {e}')
    else:
        return current_video_files
