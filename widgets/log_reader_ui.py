# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Python\FishPro\widgets\log_reader.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_log_reader_widget(object):
    def setupUi(self, log_reader_widget):
        log_reader_widget.setObjectName("log_reader_widget")
        log_reader_widget.resize(1006, 406)
        self.gridLayout = QtWidgets.QGridLayout(log_reader_widget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_current_time = QtWidgets.QLabel(log_reader_widget)
        self.label_current_time.setObjectName("label_current_time")
        self.gridLayout.addWidget(self.label_current_time, 0, 0, 1, 1)
        self.qtext_logscreen = QtWidgets.QTextEdit(log_reader_widget)
        self.qtext_logscreen.setObjectName("qtext_logscreen")
        self.gridLayout.addWidget(self.qtext_logscreen, 1, 0, 1, 2)
        self.btn_save_logs = QtWidgets.QPushButton(log_reader_widget)
        self.btn_save_logs.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_save_logs.setObjectName("btn_save_logs")
        self.gridLayout.addWidget(self.btn_save_logs, 3, 0, 1, 2)
        self.groupBox_android = QtWidgets.QGroupBox(log_reader_widget)
        self.groupBox_android.setObjectName("groupBox_android")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_android)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_connect_android = QtWidgets.QPushButton(self.groupBox_android)
        self.btn_connect_android.setObjectName("btn_connect_android")
        self.verticalLayout_2.addWidget(self.btn_connect_android)
        self.dropdown_android_devices = QtWidgets.QComboBox(self.groupBox_android)
        self.dropdown_android_devices.setObjectName("dropdown_android_devices")
        self.verticalLayout_2.addWidget(self.dropdown_android_devices)
        self.gridLayout.addWidget(self.groupBox_android, 2, 1, 1, 1)
        self.groupBox_ios = QtWidgets.QGroupBox(log_reader_widget)
        self.groupBox_ios.setObjectName("groupBox_ios")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_ios)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_connect_ios = QtWidgets.QPushButton(self.groupBox_ios)
        self.btn_connect_ios.setObjectName("btn_connect_ios")
        self.verticalLayout.addWidget(self.btn_connect_ios)
        self.dropdown_ios_devices = QtWidgets.QComboBox(self.groupBox_ios)
        self.dropdown_ios_devices.setObjectName("dropdown_ios_devices")
        self.verticalLayout.addWidget(self.dropdown_ios_devices)
        self.gridLayout.addWidget(self.groupBox_ios, 2, 0, 1, 1)

        self.retranslateUi(log_reader_widget)
        QtCore.QMetaObject.connectSlotsByName(log_reader_widget)

    def retranslateUi(self, log_reader_widget):
        _translate = QtCore.QCoreApplication.translate
        log_reader_widget.setWindowTitle(_translate("log_reader_widget", "Form"))
        self.label_current_time.setText(_translate("log_reader_widget", "TextLabel"))
        self.btn_save_logs.setText(_translate("log_reader_widget", "Save logs"))
        self.groupBox_android.setTitle(_translate("log_reader_widget", "Android"))
        self.btn_connect_android.setText(_translate("log_reader_widget", "Connect to Android"))
        self.groupBox_ios.setTitle(_translate("log_reader_widget", "iOS"))
        self.btn_connect_ios.setText(_translate("log_reader_widget", "Connect to iOS"))
