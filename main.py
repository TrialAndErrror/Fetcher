from src.fetcher.fetch import fetch
import time


def fetch_with_timer():
    """
    Start and stop timer for fetch; print results on console.

    :return: None
    """
    start = time.perf_counter()
    fetch()
    stop = time.perf_counter()
    print(f'\n\nDownloaded videos in {stop-start:0.4f} seconds')


if __name__ == '__main__':
    fetch_with_timer()
