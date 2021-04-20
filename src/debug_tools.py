import datetime
import time
import logging


def timer(func):
    """
    Creates timer decorator to display download time.
    :param func: function
    :return: wrapper: function
    """
    def wrapper():
        start_logging(True)
        start = time.perf_counter()
        logging.info(f'Performance timer started at {datetime.datetime.now()}\n')
        func()
        stop = time.perf_counter()
        logging.info(f'\nPerformance timer stopped at {datetime.datetime.now()}\n\n')
        duration = stop-start
        unit = 'seconds'
        if duration > 60:
            duration = duration/60
            unit = 'minutes'
        print(f'Downloaded videos in {duration:0.4f} {unit}')
    return wrapper


def start_logging(debug_mode=False):
    log_format = '%(asctime)s:%(levelname)s:%(message)s'
    if debug_mode:
        logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=log_format)
    else:
        logging.basicConfig(filename='logs.log', level=logging.INFO, format=log_format)


def report_success_or_failure(num_sheets, num_videos):
    if num_sheets > 0 and num_videos > 0:
        print(f'\nSuccess! {num_sheets} sheets processed, downloading {num_videos} videos.')
    else:
        print_error_message(num_sheets, num_videos)


def print_error_message(num_sheets, num_videos):
    print(f'\nUh-oh, something went wrong!')
    if num_sheets == 0:
        print('\nNo sheets detected. Make sure you put valid csv files in the root directory.')
        if num_videos > 0:
            print(f'\nWeird, I still downloaded {num_videos} videos...')
    elif num_videos == 0:
        print('\nNo videos detected. Make sure your csv files have valid youtube links in them.')
        if num_sheets > 0:
            print(f'\nI did see {num_sheets} sheets in the directory, but couldn\'t find any video links')