import logging
import os
from pathlib import Path

from src.FetcherModel import MultiFetcher, download_file
from src.file_actions import find_files, find_youtube_links
from src.models.base_models import SingleFetcher, ListFetcher


def run_single_url(url: str, audio: bool):
    """
    Download a single url.
    Accessible from GUI or using the -u parameter.

    :param audio: bool
    :param url: str
    :return: None
    """
    output_dir = Path(os.getcwd(), 'Downloads')
    output_dir.mkdir(parents=True, exist_ok=True)
    fetcher = SingleFetcher(download_func=download_file, out_path=output_dir)
    fetcher.get_video_files()


def run_single_csv(file: str, audio_only: bool = False):
    """
    Same as Run Fetch, but providing a list of one sheet as the files parameter.
    Accessible from GUI or using the -f parameter.

    :param audio_only: bool
    :param file: str
    :return: count_sheets: int, count_videos: int
    """
    full_path = Path(os.getcwd(), file)
    output_dir = f'{full_path[:-4]}/'.strip()

    fetcher = ListFetcher(
        download_func=download_file,
        link_gather_func=find_youtube_links,
        out_path=output_dir,
        audio_only=audio_only
    )
    fetcher.get_links(full_path)
    fetcher.get_video_files()


def run_all_csvs(audio_only=False):
    files_found, files_list = find_files()
    if not files_found:
        logging.warning('No files found; please place CSV files in this directory')
        return 0

    logging.info(f'Files list: {files_list}')
    for file_name in files_list:
        audio_only = file_name.startswith('[AUDIO]') or audio_only
        run_single_csv(file_name, audio_only)
    return len(files_list)
