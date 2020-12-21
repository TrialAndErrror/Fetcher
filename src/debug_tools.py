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
        start = time.perf_counter()
        print(f'Performance timer started at {datetime.datetime.now()}')
        func()
        stop = time.perf_counter()
        print(f'Performance timer stopped at {datetime.datetime.now()}\n\nDownloaded videos in {stop-start:0.4f} seconds')
    return wrapper


def start_logging():
    log_format = '%(asctime)s:%(levelname)s:%(message)s'
    logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=log_format)
    logging.basicConfig(filename='warnings.log', level=logging.WARNING, format=log_format)
    logging.basicConfig(filename='info.log', level=logging.INFO, format=log_format)
