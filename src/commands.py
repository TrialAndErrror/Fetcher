import logging
import os

from src.FetcherModel import MultiFetcher, download_file
from src.file_actions import find_files, find_links


def run_single_url(url, audio):
    """
    Download a single url.
    Accessible from GUI or using the -u parameter.

    :param audio: bool
    :param url: str
    :return: None
    """
    output_dir = os.path.join(os.getcwd(), 'Downloads')
    os.makedirs(output_dir, exist_ok=True)
    download_file(url, output_dir, audio)
    print(f'Downloaded {url}')


def run_single_sheet(file, audio_only):
    """
    Same as Run Fetch, but providing a list of one sheet as the files parameter.
    Accessible from GUI or using the -f parameter.

    :param audio_only: bool
    :param file: str
    :param args: dict
    :return: count_sheets: int, count_videos: int
    """
    output_dir, urls = find_links(file)
    fetcher_obj = MultiFetcher(urls, audio_only, output_dir)
    return fetcher_obj.fetch()


def run_fetch(args):
    """
    Perform Video Fetch.

    audio is optional param that indicates whether to just download audio.
    :return: None
    """
    files_found, files_list = find_files()
    if files_found:
        logging.info(f'Files list: {files_list}')
        files_count = 0
        for file_name in files_list:
            audio_only = file_name.startswith('[AUDIO]') or args.get('audio', False)
            print(f'Working on {file_name}')
            files_count += run_single_sheet(file_name, audio_only)
        return files_count
    else:
        logging.warning('No files found; please place CSV files in this directory')
        return 0, 0
