import os
from pathlib import Path
import time

import subprocess, sys

from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox

import sys
from src.fetcher_gui import Ui_Form as WindowUI
from src.gui_api import process_gui_command
from src.gui.ProgressWindow import ProgressDisplay

from src.file_actions import find_files
from src.fetch import read_spreadsheet


def get_file_names():
    file_names = os.listdir(os.getcwd())
    return [file for file in file_names
            if file.endswith('.xls')
            or file.endswith('.csv')
            or file.endswith('.xlsx')]


def open_folder(output_dir):
    if sys.platform == 'darwin':
        subprocess.call(["open", output_dir])

    elif sys.platform == 'win32':
        os.startfile(output_dir)
    else:
        subprocess.call(["xdg-open", output_dir])

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = WindowUI()
        self.ui.setupUi(self)
        self.setWindowTitle('Fetcher')

        self.progress_window = None
        self.output_dir = f'{os.getcwd()}/'

        self.ui.comboBox_sheetname.addItems(get_file_names())
        self.connect_buttons()
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
        # self.ui.pushButton_fetch.clicked.connect(self.run_fetcher)
        self.ui.pushButton_fetch.clicked.connect(self.new_run_fetcher)

        self.ui.radioButton_url.clicked.connect(self.enable_boxes)
        self.ui.radioButton_sheet.clicked.connect(self.enable_boxes)
        self.ui.radioButton_fetch.clicked.connect(self.enable_boxes)

    def run_fetcher(self):
        self.set_all_disabled(True)

        command = {}
        if self.ui.radioButton_fetch.isChecked():
            command['type'] = 'sheet'
        elif self.ui.radioButton_url.isChecked():
            command['type'] = 'url'
            command['url'] = self.ui.lineEdit_url.text()
        elif self.ui.radioButton_sheet.isChecked():
            command['type'] = 'sheet'
            command['file'] = self.ui.comboBox_sheetname.currentText()
        command['audio'] = self.ui.checkBox_audio.isChecked()

        time.sleep(1)

        process_gui_command(command)
        self.ui.label_status.setText(f'Downloads complete.')
        self.set_all_disabled(False)

    def new_run_fetcher(self):
        self.set_all_disabled(True)
        output_dir = ''

        if self.ui.radioButton_fetch.isChecked():
            # Process fetch all
            files_found, video_files = find_files()
            if files_found:
                for file in video_files:
                    audio = False
                    if file.startswith('[AUDIO]') or self.ui.checkBox_audio.isChecked():
                        audio = True
                    output_dir, video_files = read_spreadsheet(file)
                    video_set = set(video_files)
                    cleaned_video_urls = list(video_set)
                    self.progress_window = ProgressDisplay(output_dir, urls=cleaned_video_urls, audio=audio)

        elif self.ui.radioButton_url.isChecked():
            # Process one url
            audio = self.ui.checkBox_audio.isChecked()
            self.progress_window = ProgressDisplay('', urls=[self.ui.lineEdit_url.text()], audio=audio)

        elif self.ui.radioButton_sheet.isChecked():
            # process one sheet
            file = self.ui.comboBox_sheetname.currentText()
            audio = False
            if file.startswith('[AUDIO]') or self.ui.checkBox_audio.isChecked():
                audio = True
            output_dir, video_files = read_spreadsheet(file)
            video_set = set(video_files)
            cleaned_video_urls = list(video_set)
            self.progress_window = ProgressDisplay(output_dir, urls=cleaned_video_urls, audio=audio)

        self.output_dir = f'{os.getcwd()}/{output_dir}'

        self.progress_window.done.connect(self.finish_fetch)

        self.set_all_disabled(False)

    def finish_fetch(self, count):
        self.progress_window.close()
        message = QMessageBox(QMessageBox.Information, 'Fetcher: Download Complete', f'Download Complete! Fetcher downloaded {count} videos.')
        open_folder(self.output_dir)
        message.exec_()




def run_gui():
    app = QApplication(sys.argv)
    screen = Window()
    screen.show()
    sys.exit(app.exec_())



