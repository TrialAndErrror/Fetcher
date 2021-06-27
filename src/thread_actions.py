import concurrent.futures
import logging
import time

from src.pafy_fetch import pafy_download_video


def get_all_videos(video_list, output_dir, audio_only):
    """
    Command-line based threading for video downloads.

    Create up to 5 threads at a time to get all videos. Number can be modified in max_workers parameter.

    :param video_list: list
    :param output_dir: str
    :return: None
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        threads_list = []
        for video in video_list:
            make_and_append_thread(executor, output_dir, threads_list, video, audio_only)
        thread_print_when_done(threads_list)


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

        pafy_download_video(item, output_dir_name, audio_only)

        print(f'\nCompleted {item}')
    except Exception as e:
        logging.warning(f'Error downloading {item};\n\nerror {e}')


def thread_print_when_done(threads_list):
    """
    When a thread in the threads list finishes, print the return value.

    :param threads_list:
    :return: None
    """
    for thread in concurrent.futures.as_completed(threads_list):
        logging.debug(thread.result())