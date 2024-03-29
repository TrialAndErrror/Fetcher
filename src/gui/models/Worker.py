import pafy
from PyQt5.QtCore import QObject, pyqtSignal


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
        print(f"Finished downloading on thread {self.id}")
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
        video = pafy.new(self.url)
        self.name.emit(video.title, self.id)
        print(f'Starting on thread {self.id}')

        if self.audio:
            try:
                video_stream = video.getbestaudio('m4a', False)
            except AttributeError as e:
                print('Does this video exist?')
                print(e)
            else:
                video_stream.download(self.output_dir, callback=self.callback)

        else:
            try:
                video_stream = video.getbest('mp4', False)
            except AttributeError as e:
                print('Does this video exist?')
                print(e)
            else:
                video_stream.download(self.output_dir, callback=self.callback)
