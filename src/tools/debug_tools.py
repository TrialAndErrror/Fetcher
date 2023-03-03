import datetime
import time
import logging

import youtube_dl


def timer(func):
    """
    Creates timer decorator to display download time.
    :param func: function
    :return: wrapper: function
    """
    def wrapper():
        start_logging()

        start = time.perf_counter()
        logging.info(f'Performance timer started at {datetime.datetime.now()}\n')

        func()

        stop = time.perf_counter()
        logging.info(f'\nPerformance timer stopped at {datetime.datetime.now()}\n\n')

        duration, unit = calculate_duration(start, stop)
        print(f'Downloaded videos in {duration:0.4f} {unit}')

    def calculate_duration(start, stop):
        """
        Calculate duration of downloads based on start and stop time.
        Returns human-readable number.

        :param start: float
        :param stop: float
        :return: float, str
        """
        duration = stop - start
        if duration > 60:
            duration /= 60
            unit = 'minutes'
        else:
            unit = 'seconds'
        return duration, unit

    return wrapper


def start_logging(debug_mode=False):
    """
    Configure logging and determine level.
    Include "True" as a positional argument to enable debug-level logging.

    :param debug_mode: bool
    :return:
    """
    log_format = '%(asctime)s:%(levelname)s:%(message)s'
    if debug_mode:
        logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=log_format)
    else:
        logging.basicConfig(filename='info.log', level=logging.INFO, format=log_format)


def report_success_or_failure(num_videos):
    """
    Provide command-line feedback to success or failure of fetch process.

    :param num_videos: int
    :return:
    """
    if num_videos > 0:
        print(f'\nSuccess! Downloaded {num_videos} videos.')
    else:
        print('\nNo videos detected. Make sure your csv files have valid youtube links in them.')


def clear_youtube_cache():
    """
    Clearing the cache to avoid the 403: Forbidden error when running fetch tests.

    See https://github.com/mps-youtube/pafy/issues/264

    :return: None
    """
    with youtube_dl.YoutubeDL({}) as ydl:
        ydl.cache.remove()
