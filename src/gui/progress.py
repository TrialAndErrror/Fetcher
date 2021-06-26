# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progress.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(537, 238)
        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setGeometry(QtCore.QRect(10, 10, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.pushButton_cancel = QtWidgets.QPushButton(Form)
        self.pushButton_cancel.setGeometry(QtCore.QRect(430, 20, 89, 25))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(330, 60, 191, 171))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.progressBar_1 = QtWidgets.QProgressBar(self.widget)
        self.progressBar_1.setProperty("value", 24)
        self.progressBar_1.setObjectName("progressBar_1")
        self.verticalLayout.addWidget(self.progressBar_1)
        self.progressBar_2 = QtWidgets.QProgressBar(self.widget)
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.verticalLayout.addWidget(self.progressBar_2)
        self.progressBar_3 = QtWidgets.QProgressBar(self.widget)
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.verticalLayout.addWidget(self.progressBar_3)
        self.progressBar_4 = QtWidgets.QProgressBar(self.widget)
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setObjectName("progressBar_4")
        self.verticalLayout.addWidget(self.progressBar_4)
        self.progressBar_5 = QtWidgets.QProgressBar(self.widget)
        self.progressBar_5.setProperty("value", 24)
        self.progressBar_5.setObjectName("progressBar_5")
        self.verticalLayout.addWidget(self.progressBar_5)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(10, 60, 311, 171))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_file1 = QtWidgets.QLabel(self.widget1)
        self.label_file1.setObjectName("label_file1")
        self.verticalLayout_2.addWidget(self.label_file1)
        self.label_file2 = QtWidgets.QLabel(self.widget1)
        self.label_file2.setObjectName("label_file2")
        self.verticalLayout_2.addWidget(self.label_file2)
        self.label_file3 = QtWidgets.QLabel(self.widget1)
        self.label_file3.setObjectName("label_file3")
        self.verticalLayout_2.addWidget(self.label_file3)
        self.label_file4 = QtWidgets.QLabel(self.widget1)
        self.label_file4.setObjectName("label_file4")
        self.verticalLayout_2.addWidget(self.label_file4)
        self.label_file5 = QtWidgets.QLabel(self.widget1)
        self.label_file5.setObjectName("label_file5")
        self.verticalLayout_2.addWidget(self.label_file5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Fetcher Downloads"))
        self.label_title.setText(_translate("Form", "Fetcher Downloads"))
        self.pushButton_cancel.setText(_translate("Form", "Cancel All"))
        self.label_file1.setText(_translate("Form", "File 1"))
        self.label_file2.setText(_translate("Form", "File 2"))
        self.label_file3.setText(_translate("Form", "File 3"))
        self.label_file4.setText(_translate("Form", "File 4"))
        self.label_file5.setText(_translate("Form", "File 5"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
