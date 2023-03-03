import pafy
from pafy.pafy import Pafy
from abc import ABC, abstractmethod


class PafyFetcher(ABC):
    def __init__(self, url):
        self.obj: Pafy = pafy.new(url)

    @abstractmethod
    def get_stream(self):
        ...


class VideoPafyObject(PafyFetcher):
    def get_stream(self):
        return self.obj.getbest('mp4')


class AudioPafyObject(PafyFetcher):
    def get_stream(self):
        return self.obj.getbest('mp4')
