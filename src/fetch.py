import concurrent.futures
import logging
import time

from .debug_tools import report_success_or_failure
from .video_actions import download_video, create_video_object
from .file_actions import find_files, read_list_path


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
        num_sheets, num_videos = download_all_videos(files_list, audio=audio)
    else:
        logging.warning('No files found; please place CSV files in this directory')
    return num_sheets, num_videos


def download_all_videos(files_list, audio=False):
    """
    Download all videos in all files for a given list of files.

    audio param is optional flag to indicate only audio downloads.
    :param files_list: list(str)
    :param audio: bool
    :return: None
    """
    count_sheets = len(files_list)
    count_videos = 0
    file: str
    # audio = False
    for file in files_list:
        if file.startswith('[AUDIO]') or audio:
            print(f'Working on Audio Spreadsheet {file[7:]}')
            audio = True
        else:
            print(f'\nWorking on {file}')
        output_dir_name, current_video_files = read_spreadsheet(file)
        count_videos += len(current_video_files)
        get_all_videos(current_video_files, output_dir_name, audio)
    return count_sheets, count_videos


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


def get_all_videos(video_list, output_dir, audio_only):
    """
    Create up to 5 threads at a time to get all videos. Max_workers can be modified or removed.
    :param video_list: list
    :param output_dir: str
    :return: None
    """

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        threads_list = []
        for video in video_list:
            make_and_append_thread(executor, output_dir, threads_list, video, audio_only)
        thread_print_when_done(threads_list)


def thread_print_when_done(threads_list):
    """
    When a thread in the threads list finishes, print the return value.

    :param threads_list:
    :return: None
    """
    for thread in concurrent.futures.as_completed(threads_list):
        logging.debug(thread.result())


def make_and_append_thread(executor, output_dir, threads_list, video, audio_only):
    """
    Make thread, and add to list if successful

    :param executor: concurrent.futures.ThreadPoolExecutor()
    :param output_dir: str
    :param threads_list: list
    :param video: str?
    :return:
    """
    try:
        thread = executor.submit(download_file, video, output_dir, audio_only)
    except Exception as e:
        logging.warning(f'Error making thread for {video};\n\n error code {e}')
    else:
        threads_list.append(thread)
        time.sleep(.3)


def download_file(item, output_dir_name, audio_only):
    """
    Function that runs on the thread; download item parameter to output directory.

    :param item: str
    :param output_dir_name: str
    :param audio_only: bool
    :return: None
    """
    try:
        print(f'\nStarting downloading {item}')
        logging.info(f'Working on {item}')
        current_video = create_video_object(item)
        download_video(current_video, output_dir_name, audio_only)
        print(f'\nCompleted {item}')
        return f'Done working on {item}'
    except Exception as e:
        logging.warning(f'Error downloading {item};\n\nerror {e}')


def download_single_video(url, audio_only):
    download_file(url, 'Downloads', audio_only)


def run_single_sheet(args):
    return download_all_videos([args["file"]], audio=args.get("audio", False))


def run_single_file(args):
    download_single_video(args["url"], args.get("audio", False))
    num_sheets = 0
    num_videos = 1
    return num_sheets, num_videos