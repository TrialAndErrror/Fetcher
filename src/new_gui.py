from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QProgressBar
from PyQt5.QtCore import Qt, QObject, QRunnable, pyqtSlot, QThreadPool, QTimer
import traceback, sys
import datetime
import pafy

# this may be a long sample but you can copy and pase it for test
# the different parts of code are commented so it can be clear what it does

class WorkerSignals(QObject):
    finished = QtCore.pyqtSignal()
    size = QtCore.pyqtSignal(int)
    progress = QtCore.pyqtSignal(int)
    eta = QtCore.pyqtSignal(int)
    name = QtCore.pyqtSignal(str)

class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn # Get the function passed in
        self.args = args # Get the arguments passed in
        self.kwargs = kwargs # Get the keyword arguments passed in
        self.signals = WorkerSignals() # Create a signal class

    @pyqtSlot()
    def run(self): # our thread's worker function
        result = self.fn(*self.args, **self.kwargs) # execute the passed in function with its arguments
        # self.signals.finished.emit(result)  # return result
        self.signals.finished.emit()  # emit when thread ended

    def callback(self, total, recvd, ratio, rate, eta):
        print(f'Emmitting a signal from {self.id}')
        self.signals.progress.emit(int((recvd/total)*100))
        self.signals.eta.emit(eta)
        self.signals.size.emit(total)

    def fn(self):
        self.url = 'https://www.youtube.com/watch?v=fHpp5hR1a9s'
        self.video = pafy.new(self.url)
        self.signals.name.emit(self.video.title)
        print(f'Starting on thread')
        if self.audio:
            try:
                video_stream = self.video.getbestaudio('m4a', False)
            except AttributeError as e:
                print('Does this video exist?')
                print(e)
            else:
                video_stream.download(self.kwargs.get('Output Dir'), callback=self.callback)
        else:
            try:
                video_stream = self.video.getbest('mp4', False)
            except AttributeError as e:
                print('Does this video exist?')
                print(e)
            else:
                video_stream.download(self.output_dir, callback=self.callback)
        print(f"Finished downloading on thread {self.id}")
        self.finished.emit()

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs): #-----------------------------------------
        super(MainWindow, self).__init__(*args, **kwargs) #                        |
        self.threadpool = QThreadPool() #                                          |
        print("Maximum Threads : %d" % self.threadpool.maxThreadCount()) #         |
        self.layout = QVBoxLayout() #                                              |
        self.time_label = QLabel("Start") #                                        |
        self.btn_thread = QPushButton("Run Download") #                            |
        self.bar = QProgressBar()                                                # |
        self.btn_thread.pressed.connect(self.threadRunner) #                       |----- These are just some initialization
        self.layout.addWidget(self.time_label) #                                   |
        self.layout.addWidget(self.bar) #                                          |
        self.layout.addWidget(self.btn_thread) #                                   |
        w = QWidget() #                                                            |
        w.setLayout(self.layout) #                                                 |
        self.setCentralWidget(w) #                                                 |
        self.show() #                                                              |
        self.timer = QTimer() #                                                    |
        self.timer.setInterval(10) #                                               |
        self.timer.timeout.connect(self.time) #                                    |
        self.timer.start() #-------------------------------------------------------



    def foo_thread(self, num):
        pass

        # we'll use this function in window ( window = main thread )
        # it will take around 5 seconds to process
    def foo_window(self, num):
        # some long processing
        print("Window Processing...")
        for i in range(50000000):
            num += 10
        # add a label to layout
        label = QLabel("Result from Window is : "+str(num))
        self.layout.addWidget(label)
        return num

        # we'll use this function when 'finished' signal is emited
    def thread_finished(self):
        print("Finished signal emited.")
        self.btn_thread.setText("Using Thread")

        # we'll use this function when 'result' signal is emited
    def thread_result(self, s):
        # add a label to layout
        label = QLabel("Result from Thread is : "+str(s))
        self.layout.addWidget(label) # add a new label to window with the returned result from our thread

        # in this function we create our thread and run it
    def threadRunner(self):
        worker = Worker(self.foo_thread, num=1) # create our thread and give it a function as argument with its args
        # worker.signals.result.connect(self.thread_result) # connect result signal of our thread to thread_result
        worker.signals.finished.connect(self.thread_finished) # connect finish signal of our thread to thread_complete
        self.threadpool.start(worker) # start thread

        # this function just gets current time and displays it in Window
    def time(self):
        now = datetime.datetime.now().time() # current time
        self.time_label.setText("Current Time: "+ str(now)) # desplay current time

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    app.exec_()