# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\gulya\Desktop\Diploma\block_attempt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import block_1_rc
import Ui_block_attempt_2


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()

        self.mainwindow = QtWidgets.QMainWindow()
        self.setupUi(self.mainwindow)
        self.mainwindow.show()
        self.mainwindow.showMaximized()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1920, 1080)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setWhatsThis("")
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/1/7.jpg"))
        QtGui.QPixmapCache.setCacheLimit(2147483647)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 90, 271, 21))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton.setText("")
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 110, 181, 21))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_2.setText("")
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 240, 131, 21))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_3.setText("")
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setEnabled(True)
        self.lineEdit_4.setGeometry(QtCore.QRect(780, 522, 360, 23))
        font = QtGui.QFont()
        font.setKerning(True)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setFrame(True)
        self.lineEdit_4.setReadOnly(False)
        self.lineEdit_4.setClearButtonEnabled(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setGeometry(QtCore.QRect(992, 576, 71, 20))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_5.setText("")
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setEnabled(False)
        self.pushButton_6.setGeometry(QtCore.QRect(430, 200, 141, 20))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_6.setText("")
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setGeometry(QtCore.QRect(560, 80, 121, 31))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_7.setText("")
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(260, 220, 201, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(260, 250, 331, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(260, 280, 201, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(260, 350, 381, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(260, 380, 421, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.label.setPixmap(QtGui.QPixmap(":/1/4.jpg"))
        self.pushButton.clicked.connect(self.click_1)
        self.pushButton_2.clicked.connect(self.click_2)
        self.pushButton_3.clicked.connect(self.click_3)
        self.lineEdit_4.hide()
        self.checkBox.hide()
        self.checkBox_2.hide()
        self.radioButton.hide()
        self.radioButton_2.hide()
        self.radioButton_3.hide()
        self.pushButton_5.clicked.connect(self.click_4)

    def click_1(self):
        self.pushButton.setEnabled(False)
        self.label.setPixmap(QtGui.QPixmap(":/1/5.jpg"))
        self.pushButton_2.setEnabled(True)

    def click_2(self):
        self.pushButton_2.setEnabled(False)
        self.label.setPixmap(QtGui.QPixmap(":/1/6.jpg"))
        self.pushButton_3.setEnabled(True)

    def click_3(self):
        self.pushButton_3.setEnabled(False)
        self.lineEdit_4.show()
        self.label.setPixmap(QtGui.QPixmap(":/1/7.jpg"))
        self.pushButton_5.setEnabled(True)

    def click_4(self):
        self.pushButton_5.setEnabled(False)
        self.lineEdit_4.hide()
        self.lineEdit_4.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/2/9.1.png"))
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.clicked.connect(self.click_5)

    def click_5(self):
        self.pushButton_3.setEnabled(False)
        self.lineEdit_4.show()
        self.label.setPixmap(QtGui.QPixmap(":/2/10.jpg"))
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.clicked.connect(self.click_6)

    def click_6(self):
        self.pushButton_5.setEnabled(False)
        self.lineEdit_4.hide()
        self.lineEdit_4.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/2/10.2.png"))
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.clicked.connect(self.click_7)

    def click_7(self):
        self.pushButton_3.setEnabled(False)
        self.lineEdit_4.show()
        self.label.setPixmap(QtGui.QPixmap(":/2/11.jpg"))
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.clicked.connect(self.click_8)

    def click_8(self):
        self.pushButton_5.setEnabled(False)
        self.lineEdit_4.hide()
        self.lineEdit_4.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/2/11.3.png"))
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.clicked.connect(self.click_9)

    def click_9(self):
        self.pushButton_3.setEnabled(False)
        self.lineEdit_4.show()
        self.label.setPixmap(QtGui.QPixmap(":/2/12.jpg"))
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.clicked.connect(self.click_10)

    def click_10(self):
        self.pushButton_5.setEnabled(False)
        self.lineEdit_4.hide()
        self.lineEdit_4.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/2/12.4.png"))
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.clicked.connect(self.click_11)

    def click_11(self):
        self.pushButton_3.setEnabled(False)
        self.lineEdit_4.show()
        self.label.setPixmap(QtGui.QPixmap(":/2/13.jpg"))
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.clicked.connect(self.click_12)

    def click_12(self):
        self.pushButton_5.setEnabled(False)
        self.lineEdit_4.hide()
        self.lineEdit_4.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/2/13.5.png"))
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.clicked.connect(self.click_3_1)

    def click_3_1(self):
        self.pushButton_3.setEnabled(False)
        self.lineEdit_4.show()
        self.label.setPixmap(QtGui.QPixmap(":/3/14.jpg"))
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.clicked.connect(self.click_3_2)

    def click_3_2(self):
        self.pushButton_5.setEnabled(False)
        self.lineEdit_4.hide()
        self.lineEdit_4.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/3/14.7.png"))
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.clicked.connect(self.click_3_3)

    def click_3_3(self):
        self.pushButton_3.setEnabled(False)
        self.lineEdit_4.show()
        self.label.setPixmap(QtGui.QPixmap(":/3/15.jpg"))
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.clicked.connect(self.click_3_4)

    def click_3_4(self):
        self.pushButton_5.setEnabled(False)
        self.lineEdit_4.hide()
        self.lineEdit_4.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/3/15.8.png"))
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.clicked.connect(self.click_3_5)

    def click_3_5(self):
        self.pushButton_3.setEnabled(False)
        self.lineEdit_4.show()
        self.label.setPixmap(QtGui.QPixmap(":/3/16.jpg"))
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.clicked.connect(self.click_3_6)

    def click_3_6(self):
        self.pushButton_5.setEnabled(False)
        self.lineEdit_4.hide()
        self.lineEdit_4.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/3/16.9.png"))
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.clicked.connect(self.click_3_7)

    def click_3_7(self):
        self.pushButton_3.setEnabled(False)
        self.lineEdit_4.show()
        self.label.setPixmap(QtGui.QPixmap(":/3/17.jpg"))
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.clicked.connect(self.click_3_8)

    def click_3_8(self):
        self.pushButton_5.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.lineEdit_4.hide()
        self.lineEdit_4.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/3/17.10.png"))
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.clicked.connect(self.open_window_2)

    def open_window_2(self):
        self.pushButton_7.setEnabled(False)
        self.window_to_open = Ui_block_attempt_2.Ui_MainWindow()
        self.mainwindow.close()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "block"))
        self.centralwidget.setStatusTip(_translate("MainWindow", "Шаг 1: найти верную кнопку"))
        self.radioButton.setText(_translate("MainWindow", "Активная политика"))
        self.radioButton_2.setText(_translate("MainWindow", "Политика для автономных пользователей"))
        self.radioButton_3.setText(_translate("MainWindow", "Неактивная политика"))
        self.checkBox.setText(_translate("MainWindow", "Наследовать параметры из политики верхнего уровня"))
        self.checkBox_2.setText(_translate("MainWindow", "Форсировать наследование параметров дочерними политиками"))
