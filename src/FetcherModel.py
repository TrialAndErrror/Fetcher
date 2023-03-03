import os
from threading import Thread
from typing import List

from src.pafy_fetcher.video_actions import VideoPafyObject, AudioPafyObject


class MultiFetcher:
    fetcher_list: List[Thread]

    def __init__(self, urls, audio_only, output_dir):
        self.urls: list = urls
        self.output_dir = output_dir
        self.audio_only = audio_only

        os.makedirs(self.output_dir, exist_ok=True)

    def fetch(self):
        self.fetcher_list = [
            Thread(
                target=download_file,
                args=(url, self.output_dir, self.audio_only),
            ) for url in self.urls
        ]

        for obj in self.fetcher_list:
            obj.start()
            obj.join()

        return len(os.listdir(self.output_dir))


def download_file(url, output_dir, audio_only):
    """
    Function that runs on the thread; download item parameter to output directory.

    :param audio_only: bool
    :param output_dir: str
    :param url: str
    :return: None
    """

    model = AudioPafyObject if audio_only else VideoPafyObject
    obj = model(url)

    video_stream = obj.get_stream()

    video_stream.download(filepath=output_dir, quiet=False)
