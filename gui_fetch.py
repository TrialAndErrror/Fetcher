import sys

from PyQt5.QtWidgets import QApplication

from src.gui.models.FetcherWindow import FetcherWindow


def run_gui():
    app = QApplication(sys.argv)
    screen = FetcherWindow()
    screen.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    """
    GUI Fetch is a separate application built in PyQt5 that uses QThreads to download video files
    """
    run_gui()
