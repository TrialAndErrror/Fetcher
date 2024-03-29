import os
import shutil
import sys

from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

from src.file_actions import find_files
from src.gui.WindowForms.fetcher import Ui_Form as WindowUI
from src.gui.gui_tools import get_file_names, open_folder, process_one_sheet
from src.gui.models.ProgressWindow import ProgressDisplay


class FetcherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = WindowUI()
        self.ui.setupUi(self)
        self.setWindowTitle('Fetcher')

        self.progress_window = None
        self.output_dir = None

        self.connect_buttons()
        self.initialize_window()

        self.show()

    def set_all_disabled(self, status):
        self.ui.lineEdit_url.setDisabled(status)
        self.ui.comboBox_sheetname.setDisabled(status)
        self.ui.pushButton_fetch.setDisabled(status)
        self.ui.radioButton_sheet.setDisabled(status)
        self.ui.radioButton_url.setDisabled(status)
        self.ui.radioButton_fetch.setDisabled(status)

    def enable_boxes(self):
        if self.ui.radioButton_fetch.isChecked():
            self.ui.lineEdit_url.setText('')
            self.ui.lineEdit_url.setDisabled(True)
            self.ui.comboBox_sheetname.setCurrentText('')
            self.ui.comboBox_sheetname.setDisabled(True)

        elif self.ui.radioButton_url.isChecked():
            self.ui.lineEdit_url.setText('')
            self.ui.lineEdit_url.setEnabled(True)
            self.ui.comboBox_sheetname.setCurrentText('')
            self.ui.comboBox_sheetname.setDisabled(True)

        elif self.ui.radioButton_sheet.isChecked():

            self.ui.lineEdit_url.setText('')
            self.ui.lineEdit_url.setDisabled(True)

            self.ui.comboBox_sheetname.clear()
            self.ui.comboBox_sheetname.addItems(get_file_names())

            self.ui.comboBox_sheetname.setCurrentIndex(0)
            self.ui.comboBox_sheetname.setEnabled(True)

    def connect_buttons(self):
        self.ui.pushButton_fetch.clicked.connect(self.run_fetcher)
        # self.ui.pushButton_fetch.clicked.connect(self.new_run_fetcher)

        self.ui.radioButton_url.clicked.connect(self.enable_boxes)
        self.ui.radioButton_sheet.clicked.connect(self.enable_boxes)
        self.ui.radioButton_fetch.clicked.connect(self.enable_boxes)

        self.ui.lineEdit_url.textChanged.connect(lambda: self.ui.radioButton_url.setChecked(True))

    def initialize_window(self):
        self.ui.comboBox_sheetname.addItems(get_file_names())

        self.ui.radioButton_fetch.setChecked(True)
        self.ui.lineEdit_url.setDisabled(True)
        self.ui.comboBox_sheetname.setDisabled(True)

    def run_fetcher(self):
        self.set_all_disabled(True)
        output_dir = 'Downloads'
        file = None

        if self.ui.radioButton_fetch.isChecked():
            """
            Fetch:

            Get list of filenames from current working directory,
            then process each file found.
            """
            self.fetch_all()

        elif self.ui.radioButton_url.isChecked():
            """
            Process one URL:

            Get URL from the drop-down menu,
            then create a progress display for just that URL.
            """
            audio = self.ui.checkBox_audio.isChecked()
            self.progress_window = ProgressDisplay(output_dir, urls=[self.ui.lineEdit_url.text()], audio=audio)

        elif self.ui.radioButton_sheet.isChecked():
            """
            Process one sheet:
            
            Get filename from the drop-down menu,
            then process the sheet with that filename.
            """
            file = self.ui.comboBox_sheetname.currentText()
            audio = bool(file.startswith('[AUDIO]') or self.ui.checkBox_audio.isChecked())
            self.progress_window = process_one_sheet(file, audio)
            output_dir = self.progress_window.output_dir

        """
        Set output directory based on sheet name, or leave as 'Downloads' if just one url.
        Make the directory if it does not exist.
        """
        if file:
            self.output_dir = f'{os.getcwd()}/{output_dir}'
            os.makedirs(self.output_dir, exist_ok=True)
            shutil.move(file, self.output_dir)

            """
            Connect the ProgressDisplay.done signal to the finish_fetch function below
            """
            self.progress_window.done.connect(self.finish_fetch)

    def fetch_all(self):
        file = None
        output_dir = 'Downloads'

        files_found, self.video_files = find_files()
        if files_found:
            file = self.video_files.pop(0)
            audio = bool(file.startswith('[AUDIO]') or self.ui.checkBox_audio.isChecked())
            self.progress_window, output_dir = process_one_sheet(file, audio)

        if file:
            self.output_dir = f'{os.getcwd()}/{output_dir}'
            os.makedirs(self.output_dir, exist_ok=True)
            shutil.move(file, self.output_dir)

            """
            Connect the ProgressDisplay.done signal to the finish_fetch function below
            """
            self.progress_window.done.connect(self.finish_fetch)

    def close_windows(self):
        """
        Close ProgressDisplay, and open output folder.
        """
        self.progress_window.close()
        open_folder(self.output_dir)

        """
        Make popup window showing count of items downloaded.
        """
        message = QMessageBox(QMessageBox.Information, 'Fetcher: Download Complete', f'Download Complete! Fetcher downloaded {count} videos.')
        message.exec_()

        self.set_all_disabled(False)
        self.initialize_window()

    def finish_fetch(self, count):
        """
        Steps to run after ProgressDisplay is finished.

        :param count: int
        :return: None
        """

        """
        Close ProgressDisplay, and open output folder.
        """
        self.progress_window.close()
        open_folder(self.output_dir)

        """
        Make popup window showing count of items downloaded.
        """
        message = QMessageBox(QMessageBox.Information, 'Fetcher: Download Complete', f'Download Complete! Fetcher downloaded {count} videos.')
        message.exec_()

        """
        Re-enable all buttons.
        """
        if len(self.video_files) > 0:
            self.fetch_all()
        else:
            self.set_all_disabled(False)
            self.initialize_window()


def run_gui():
    app = QApplication(sys.argv)
    screen = FetcherWindow()
    screen.show()
    sys.exit(app.exec_())
