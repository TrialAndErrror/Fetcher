import threading

from src.fetcher.video_actions import download_video, create_video_object
from src.fetcher.file_actions import find_files, read_list_path


def fetch():
    """
    Perform Video Fetch.
    :return: None
    """
    (files_found, files_list) = find_files()
    if files_found:
        download_all_videos(files_list)
        print('All Done')
    else:
        print('No files found; please place CSV files in this directory')


def download_all_videos(files_list):
    """
    Download all videos in all files for a given list of files.
    :param files_list: list(str)
    :return: None
    """
    file: str
    for file in files_list:
        output_dir_name, current_video_files = read_spreadsheet(file)
        get_all_videos(args=[current_video_files, output_dir_name])


def read_spreadsheet(file):
    """
    Returns output directory and list of video files from the spreadsheet.

    :param file:
    :return: str, list
    """
    output_dir_name = file[:-4]
    current_video_files = read_list_path(file)
    return output_dir_name, current_video_files


def get_all_videos(args):
    """
    Create threads for all videos and join them.
    :param args: list
    :return: None
    """
    active_threads = []

    create_threads(active_threads, args)
    join_all_threads(active_threads)


def join_all_threads(active_threads: list):
    """
    Iterate through active threads and join all.

    :param active_threads: list
    :return:
    """
    thread: threading.Thread
    for thread in active_threads:
        thread.join()


def create_threads(active_threads: list, args: list):
    """
    Create new thread for each video and append it to active threads.

    :param active_threads: list
    :param args: list
    :return: None
    """

    video_list = args[0]
    output_dir = args[1]

    video: str
    for video in video_list:
        thread = threading.Thread(target=download_file, args=[video, output_dir])
        thread.start()
        active_threads.append(thread)


def download_file(item, output_dir_name):
    """
    Function that runs on the thread; download item parameter to output directory.

    :param item: str
    :param output_dir_name: str
    :return:
    """
    try:
        print(f'Working on {item}')
        current_video = create_video_object(item)
        download_video(current_video, output_dir_name)
    except Exception as e:
        print(f'Error downloading {item};\n\nerror {e}')


