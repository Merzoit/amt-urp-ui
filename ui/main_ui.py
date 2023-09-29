# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1116, 798)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(189, 185, 178);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sst = QtWidgets.QLabel(self.centralwidget)
        self.sst.setGeometry(QtCore.QRect(480, 20, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.sst.setFont(font)
        self.sst.setObjectName("sst")
        self.version = QtWidgets.QLabel(self.centralwidget)
        self.version.setGeometry(QtCore.QRect(480, 40, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.version.setFont(font)
        self.version.setObjectName("version")
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(50, 100, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.startBtn.setFont(font)
        self.startBtn.setAutoFillBackground(False)
        self.startBtn.setStyleSheet("background-color: rgb(0, 200, 0); border-radius: 10px")
        self.startBtn.setObjectName("startBtn")
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setGeometry(QtCore.QRect(240, 100, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.stopBtn.setFont(font)
        self.stopBtn.setAutoFillBackground(False)
        self.stopBtn.setStyleSheet("background-color:rgb(200, 0, 0); border-radius: 10px")
        self.stopBtn.setObjectName("stopBtn")
        self.console = QtWidgets.QTextBrowser(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(20, 170, 421, 591))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.console.setFont(font)
        self.console.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.console.setObjectName("console")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 140, 441, 16))
        self.line.setStyleSheet("background-color: black")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.first_audio_path = QtWidgets.QLineEdit(self.centralwidget)
        self.first_audio_path.setGeometry(QtCore.QRect(710, 130, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.first_audio_path.setFont(font)
        self.first_audio_path.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.first_audio_path.setText("")
        self.first_audio_path.setObjectName("first_audio_path")
        self.first_audio_path_l = QtWidgets.QLabel(self.centralwidget)
        self.first_audio_path_l.setGeometry(QtCore.QRect(590, 130, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.first_audio_path_l.setFont(font)
        self.first_audio_path_l.setObjectName("first_audio_path_l")
        self.first_script_path_l = QtWidgets.QLabel(self.centralwidget)
        self.first_script_path_l.setGeometry(QtCore.QRect(590, 150, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.first_script_path_l.setFont(font)
        self.first_script_path_l.setObjectName("first_script_path_l")
        self.first_script_path = QtWidgets.QLineEdit(self.centralwidget)
        self.first_script_path.setGeometry(QtCore.QRect(710, 150, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.first_script_path.setFont(font)
        self.first_script_path.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.first_script_path.setText("")
        self.first_script_path.setObjectName("first_script_path")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(850, 110, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.second_script_path_l = QtWidgets.QLabel(self.centralwidget)
        self.second_script_path_l.setGeometry(QtCore.QRect(590, 230, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.second_script_path_l.setFont(font)
        self.second_script_path_l.setObjectName("second_script_path_l")
        self.second_script_path = QtWidgets.QLineEdit(self.centralwidget)
        self.second_script_path.setGeometry(QtCore.QRect(710, 230, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.second_script_path.setFont(font)
        self.second_script_path.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.second_script_path.setText("")
        self.second_script_path.setObjectName("second_script_path")
        self.second_audio_path_l = QtWidgets.QLabel(self.centralwidget)
        self.second_audio_path_l.setGeometry(QtCore.QRect(590, 210, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.second_audio_path_l.setFont(font)
        self.second_audio_path_l.setObjectName("second_audio_path_l")
        self.second_audio_path = QtWidgets.QLineEdit(self.centralwidget)
        self.second_audio_path.setGeometry(QtCore.QRect(710, 210, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.second_audio_path.setFont(font)
        self.second_audio_path.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.second_audio_path.setText("")
        self.second_audio_path.setObjectName("second_audio_path")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(850, 190, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(590, 310, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.editPromt = QtWidgets.QTextEdit(self.centralwidget)
        self.editPromt.setGeometry(QtCore.QRect(710, 280, 341, 81))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.editPromt.setFont(font)
        self.editPromt.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.editPromt.setObjectName("editPromt")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(700, 110, 1, 271))
        self.line_2.setStyleSheet("background-color: black")
        self.line_2.setLineWidth(1)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(1010, 420, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(900, 426, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(940, 720, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(940, 740, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.clearBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn.setGeometry(QtCore.QRect(460, 160, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clearBtn.setFont(font)
        self.clearBtn.setStyleSheet("background-color: rgb(185, 185, 185)")
        self.clearBtn.setObjectName("clearBtn")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(800, 400, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.streamid = QtWidgets.QLineEdit(self.centralwidget)
        self.streamid.setGeometry(QtCore.QRect(870, 399, 171, 21))
        self.streamid.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.streamid.setObjectName("streamid")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "URP v0.3.0"))
        self.sst.setText(_translate("MainWindow", "AiMediaTech"))
        self.version.setText(_translate("MainWindow", "UnityResourceProvider"))
        self.startBtn.setText(_translate("MainWindow", "Начать"))
        self.stopBtn.setText(_translate("MainWindow", "Остановить"))
        self.console.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.first_audio_path_l.setText(_translate("MainWindow", "Путь к аудио:"))
        self.first_script_path_l.setText(_translate("MainWindow", "Путь к сценарию:"))
        self.label_4.setText(_translate("MainWindow", "Первая папка"))
        self.second_script_path_l.setText(_translate("MainWindow", "Путь к сценарию:"))
        self.second_audio_path_l.setText(_translate("MainWindow", "Путь к аудио:"))
        self.label_10.setText(_translate("MainWindow", "Вторая папка"))
        self.label.setText(_translate("MainWindow", "Промт:"))
        self.editPromt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Calibri\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Интервал поиска:"))
        self.label_3.setText(_translate("MainWindow", "Model: gpt-3.5-turbo"))
        self.label_5.setText(_translate("MainWindow", "Provider: Wewordle"))
        self.clearBtn.setText(_translate("MainWindow", "X"))
        self.label_6.setText(_translate("MainWindow", "ID стрима:"))