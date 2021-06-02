import os
import time

from PyQt5.QtWidgets import QWidget, QApplication
import sys
from src.fetcher_gui import Ui_Form
from src.gui_api import process_gui_command


def get_file_names():
    file_names = os.listdir(os.getcwd())
    return [file for file in file_names
            if file.endswith('.xls')
            or file.endswith('.csv')
            or file.endswith('.xlsx')]


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('Fetcher')

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
        self.ui.pushButton_fetch.clicked.connect(self.run_fetcher)

        self.ui.radioButton_url.clicked.connect(self.enable_boxes)
        self.ui.radioButton_sheet.clicked.connect(self.enable_boxes)
        self.ui.radioButton_fetch.clicked.connect(self.enable_boxes)

    def run_fetcher(self):
        self.set_all_disabled(True)
        self.ui.label_status.setText('Determining Command')
        time.sleep(1)

        command = {}
        if self.ui.radioButton_fetch.isChecked():
            command['type'] = 'sheet'
            status_name = 'All Videos'
        elif self.ui.radioButton_url.isChecked():
            command['type'] = 'url'
            command['url'] = self.ui.lineEdit_url.text()
            status_name = 'Video from URL'
        elif self.ui.radioButton_sheet.isChecked():
            command['type'] = 'sheet'
            command['file'] = self.ui.comboBox_sheetname.currentText()
            status_name = 'Videos from Spreadsheet'
        command['audio'] = self.ui.checkBox_audio.isChecked()
        if self.ui.checkBox_audio.isChecked():
            audio_status = 'as MP3 file'
        else:
            audio_status = ''

        self.ui.label_status.setText(f'Downloading {status_name} {audio_status}, please wait...')
        time.sleep(1)

        process_gui_command(command)
        self.ui.label_status.setText(f'Downloads complete.')
        self.set_all_disabled(False)


def run_gui():
    app = QApplication(sys.argv)
    screen = Window()
    screen.show()
    sys.exit(app.exec_())



