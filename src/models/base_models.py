from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Callable


class BaseFetcher(ABC):
    out_path: Path
    audio_only: bool
    download_func: Callable

    def __init__(self, out_path, audio_only=False):
        self.out_path = out_path
        self.audio_only = audio_only

    @abstractmethod
    def get_video_files(self):
        ...


class SingleFetcher(BaseFetcher):
    url: str
    download_func: Callable[[str, Path], None]

    def __init__(self, download_func, out_path, audio_only=False):
        super().__init__(out_path, audio_only)
        self.download_func = download_func

    def get_video_files(self):
        self.download_func(self.url, self.out_path)
        print(f'Single Fetcher: Downloaded {self.url}')


class ListFetcher(BaseFetcher):
    urls: List[str]
    download_func: Callable[[List[str], Path], None]
    link_gather_func: Callable[[Path], List[str]]

    def __init__(self, download_func, link_gather_func, out_path, audio_only=False):
        super().__init__(out_path, audio_only)
        self.download_func = download_func
        self.link_gather_func = link_gather_func

    def get_links(self, file):
        self.urls = self.link_gather_func(file)

    def get_video_files(self):
        self.download_func(self.urls, self.out_path)