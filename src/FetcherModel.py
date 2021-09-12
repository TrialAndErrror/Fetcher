import os
from threading import Thread

from src.video_actions import make_pafy_object


class MultiFetcher:
    def __init__(self, urls, audio_only, output_dir):
        self.urls: list = urls
        self.fetcher_list = list()
        self.output_dir = output_dir
        self.audio_only = audio_only

        os.makedirs(self.output_dir, exist_ok=True)

    def fetch(self):
        for url in self.urls:
            self.fetcher_list.append(
                Thread(group=None,
                       target=download_file,
                       name=None,
                       args=(url, self.output_dir, self.audio_only),
                       kwargs=None,
                       daemon=None
                       )
            )
        obj: Thread

        for obj in self.fetcher_list:
            obj.start()

        for obj in self.fetcher_list:
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
    video_stream = make_pafy_object(url, audio_only)
    video_stream.download(filepath=output_dir, quiet=False)
