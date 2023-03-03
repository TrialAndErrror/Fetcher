from PyQt5.QtCore import QObject, pyqtSignal
from src.pafy_fetcher.video_actions import make_pafy_object


class Worker(QObject):
    finished = pyqtSignal(int)
    size = pyqtSignal(int, int)
    progress = pyqtSignal(int, int)
    eta = pyqtSignal(int, int)
    name = pyqtSignal(str, int)

    def __init__(self, output_dir, url, id, audio=False):
        super().__init__()

        self.output_dir = output_dir
        self.id = id
        self.url = url
        self.video = None
        self.audio = audio
        self.stream = None

    def callback(self, total, recvd, ratio, rate, eta):
        self.progress.emit(int((recvd/total)*100), self.id)

    def run(self):
        self.pafy_download_video()
        self.reset_progress_bar()

    def reset_progress_bar(self):
        self.name.emit('', self.id)
        self.progress.emit(0, self.id)
        self.finished.emit(self.id)

    def pafy_download_video(self):
        """
        Determine if audio only or not, then download accordingly.

        :return: None
        """
        video = make_pafy_object(self.url, self.audio)

        self.name.emit(video.title, self.id)

        video.download(self.output_dir, callback=self.callback)
