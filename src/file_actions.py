import os
import logging
import subprocess
import sys

VID_PREFIX = 'https://www.youtube.com/watch'
SHORT_PREFIX = 'https://youtu.be/'
PL_PREFIX = 'https://www.youtube.com/playlist'


def find_files():
    """
    Generates list of CSV files in current working directory.

    :return: (files_found: bool; files_list: list)
    """

    try:
        home_dir = os.listdir()
    except Exception as e:
        logging.warning(f'Error reading files in home directory\nError was {e}')
    else:
        files_list = [file for file in home_dir if file.endswith('.csv')]
        files_found = bool(len(files_list) > 0)
        return files_found, files_list


def find_youtube_links(path):
    """
    Matches youtube prefix to return a list of video links.

    :param path: str
    :return: current_video_files: list
    """
    try:
        with open(path) as file:
            video_files = get_link_entry_list(file)
    except Exception as e:
        logging.warning(f'Error opening {path} as file; error {e}')
    else:
        if len(video_files) == 0:
            logging.warning('No video links found')
        return video_files


def get_link_entry_list(file):
    """
    Reformat items in entry list and remove newline characters.
    :param file: file
    :return: entry_list: list
    """
    try:
        item_list = file.read().replace('\n', ',').split(',')
    except Exception as e:
        logging.warning(f'Error reading file; error {e}')
        return []
    else:
        item_list = [item.strip(' " " ') for item in item_list]
        entry_list = [entry.split('&list')[0] for entry in item_list if entry.startswith(VID_PREFIX)]
        short_entry_list = [entry for entry in item_list if entry.startswith(SHORT_PREFIX)]
        return entry_list + short_entry_list


def find_links(file):
    full_path = os.path.join(os.getcwd(), file)
    urls = find_youtube_links(full_path)
    output_dir = f'{full_path[:-4]}/'.strip()
    return output_dir, urls


def open_folder(output_dir):
    if sys.platform == 'darwin':
        subprocess.call(["open", output_dir])

    elif sys.platform == 'win32':
        os.startfile(output_dir)
    else:
        subprocess.call(["xdg-open", output_dir])