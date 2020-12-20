from src.fetcher.fetch import fetch
import time
import logging


def fetch_with_timer():
    """
    Start and stop timer for fetch; print results on console.

    :return: None
    """
    logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
    logging.basicConfig(filename='warnings.log', level=logging.WARNING, format='%(asctime)s:%(levelname)s:%(message)s')
    logging.basicConfig(filename='info.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
    start = time.perf_counter()
    fetch()
    stop = time.perf_counter()
    print(f'\n\nDownloaded videos in {stop-start:0.4f} seconds')


if __name__ == '__main__':
    fetch_with_timer()
