import time

from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread
from PyQt5.QtWidgets import QWidget

from src.gui.Worker import Worker

from src.gui.progress import Ui_Form as ProgressUI


class ProgressDisplay(QWidget):
    done = pyqtSignal(int)

    def __init__(self, output_dir, urls=None, audio=False):
        super().__init__()
        self.ui = ProgressUI()
        self.ui.setupUi(self)
        self.output_dir = output_dir
        self.urls = urls
        self.audio = audio
        self.thread = None
        self.threads = {}
        self.worker = None
        self.total = 1

        self.bars = {
            1: self.ui.progressBar_1,
            2: self.ui.progressBar_2,
            3: self.ui.progressBar_3,
            4: self.ui.progressBar_4,
            5: self.ui.progressBar_5
        }

        self.labels = {
            1: self.ui.label_file1,
            2: self.ui.label_file2,
            3: self.ui.label_file3,
            4: self.ui.label_file4,
            5: self.ui.label_file5
        }

        self.ui.pushButton_cancel.clicked.connect(self.cancel_all)
        self.show()

        self.run()

    def run(self):
        print(f"Progress Window URLS {self.urls}")
        # self.thread = QThread()

        for num in range(1, 6):
            self.threads[num] = self.add_thread(num, self.urls.pop(0))

    def add_thread(self, id, url):
        thread = QThread()

        worker = Worker(self.output_dir, url, id)
        worker.moveToThread(thread)

        thread.started.connect(worker.run)
        worker.name.connect(self.process_name_signal)
        worker.finished.connect(thread.exit)
        worker.finished.connect(worker.deleteLater)
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(self.process_finished_signal)
        worker.progress.connect(self.process_progress_signal)

        thread.start()
        return thread, worker

    @pyqtSlot(int, int)
    def process_size_signal(self):
        id = self.sender().id

    @pyqtSlot(int, int)
    def process_progress_signal(self, value, id):
        self.bars[id].setValue(value)

    def process_eta_signal(self):
        id = self.sender().id

    @pyqtSlot(str, int)
    def process_name_signal(self, name, id):
        self.labels[id].setText(name)

    @pyqtSlot(int)
    def process_finished_signal(self, id):
        self.total += 1
        if len(self.urls) > 1:
            self.threads[id] = self.add_thread(id, self.urls.pop(0))
        else:
            self.threads.pop(id)
        if len(self.threads) == 0:
            self.done.emit(self.total)

    def cancel_all(self):
        self.done.emit(self.total)
        self.ui.pushButton_cancel.setText('Cancelling downloads...')
        self.ui.pushButton_cancel.setEnabled(False)