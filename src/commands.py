import logging

from src.file_actions import find_files, read_spreadsheet
from src.FetcherModel import Fetcher


def run_single_sheet(args):
    """
    Same as Run Fetch, but providing a list of one sheet as the files parameter.
    Accessible from GUI or using the -f parameter.

    :param args: dict
    :return: count_sheets: int, count_videos: int
    """
    return download_list_of_videos([args["file"]], args.get("audio", False))


def run_fetch(audio=False):
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
        num_sheets, num_videos = download_list_of_videos(files_list, audio)
    else:
        logging.warning('No files found; please place CSV files in this directory')
    return num_sheets, num_videos


def download_list_of_videos(files_list, audio_only=False):
    """
    Download all videos in all files for a given list of files.

    Also accessed by run_single_sheet, with a files_list that only contains one file.

    audio parameter is optional flag to indicate only audio downloads.
    :param files_list: list(str)
    :param audio_only: bool
    :return: count_sheets: int, count_videos: int
    """
    count_sheets = len(files_list)
    count_videos = 0
    file: str

    for file in files_list:
        """
        Set audio parameter if it's an audio only sheet
        """
        if file.startswith('[AUDIO]'):
            audio_only = True

        """
        Describe type of sheet to console and log.
        """
        if audio_only:
            message = f'Working on Audio Spreadsheet {file[7:]}'
        else:
            message = f'\nWorking on {file}'
        print(message)
        logging.info(message)

        """
        Setup output directory, and add count of videos for the final report
        """
        output_dir_name, current_video_files = read_spreadsheet(file)
        count_videos += len(current_video_files)
        """
        Download all videos
        """
        fetcher_obj = Fetcher(current_video_files, output_dir_name, audio_only)
        fetcher_obj.get_videos_using_threads()

    """
    Returning counts for the final report
    """
    return count_sheets, count_videos


def run_single_url(args):
    """
    Download a single url.
    Accessible from GUI or using the -u parameter.

    :param args: dict
    :return: num_sheets: int, num_videos: int
    """
    fetcher_obj = Fetcher([args["url"]], 'Downloads', args.get("audio", False))
    fetcher_obj.get_videos_using_threads()

    num_sheets = 0
    num_videos = 1
    return num_sheets, num_videos
