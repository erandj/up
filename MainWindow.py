# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

conn = sqlite3.connect("db.db")


class Ui_MainWindow(object):
    def __init__(self):
        self.cur = conn.cursor()
        self.data = self.cur.execute("SELECT * FROM products;")
        self.res = self.data.fetchall()
        self.productCounts = len(self.res)

        self.buttons = []
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(414, 736)
        self.CentralWidget = QtWidgets.QWidget(MainWindow)
        self.CentralWidget.setStyleSheet("#MainWidget{\n"
"    background-color:rgb(63, 61, 60)\n"
"}\n"
"\n"
"QLabel{\n"
"    color:rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    color:rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 20);\n"
"}")
        self.CentralWidget.setObjectName("CentralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.CentralWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.MainWidget = QtWidgets.QWidget(self.CentralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainWidget.sizePolicy().hasHeightForWidth())
        self.MainWidget.setSizePolicy(sizePolicy)
        self.MainWidget.setStyleSheet("")
        self.MainWidget.setObjectName("MainWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MainWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Header = QtWidgets.QWidget(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Header.sizePolicy().hasHeightForWidth())
        self.Header.setSizePolicy(sizePolicy)
        self.Header.setMinimumSize(QtCore.QSize(0, 0))
        self.Header.setMaximumSize(QtCore.QSize(16777215, 62))
        self.Header.setObjectName("Header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Header)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Logo = QtWidgets.QWidget(self.Header)
        self.Logo.setObjectName("Logo")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Logo)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.Logo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(48, 44))
        self.label.setMaximumSize(QtCore.QSize(48, 44))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setPixmap(QtGui.QPixmap(":/icons/icons/burger-svgrepo-com.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.Logo)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_2.addWidget(self.Logo)
        self.AccountWidget = QtWidgets.QWidget(self.Header)
        self.AccountWidget.setStyleSheet("QPushButton{\n"
"    background-color:rgba(0,0,0,0);\n"
"}")
        self.AccountWidget.setObjectName("AccountWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.AccountWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.AccountWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(44, 44))
        self.pushButton.setMaximumSize(QtCore.QSize(44, 44))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/abstract-user-flat-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(44, 44))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_2.addWidget(self.AccountWidget)
        self.verticalLayout.addWidget(self.Header)
        self.MainContent = QtWidgets.QWidget(self.MainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainContent.sizePolicy().hasHeightForWidth())
        self.MainContent.setSizePolicy(sizePolicy)
        self.MainContent.setAutoFillBackground(True)
        self.MainContent.setStyleSheet("")
        self.MainContent.setObjectName("MainContent")
        self.scrollArea = QtWidgets.QScrollArea(self.MainContent)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 414, 674))
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setStyleSheet("#scrollAreaWidgetContents{\n"
"    background-color:rgb(63, 61, 60)\n"
"}")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 414, 674))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(0, 674))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(12, 12, 12, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 674))
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame)
        self.pushButton_10.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_10.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/burger-svgrepo-com.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_10.setIcon(icon1)
        self.pushButton_10.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_2.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.frame)
        self.pushButton_11.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_11.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setIcon(icon1)
        self.pushButton_11.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_2.addWidget(self.pushButton_11)
        self.pushButton_21 = QtWidgets.QPushButton(self.frame)
        self.pushButton_21.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_21.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setIcon(icon1)
        self.pushButton_21.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_21.setObjectName("pushButton_21")
        self.verticalLayout_2.addWidget(self.pushButton_21)
        self.pushButton_20 = QtWidgets.QPushButton(self.frame)
        self.pushButton_20.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_20.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setIcon(icon1)
        self.pushButton_20.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_20.setObjectName("pushButton_20")
        self.verticalLayout_2.addWidget(self.pushButton_20)
        self.pushButton_19 = QtWidgets.QPushButton(self.frame)
        self.pushButton_19.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_19.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setIcon(icon1)
        self.pushButton_19.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_19.setObjectName("pushButton_19")
        self.verticalLayout_2.addWidget(self.pushButton_19)
        self.pushButton_18 = QtWidgets.QPushButton(self.frame)
        self.pushButton_18.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_18.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setIcon(icon1)
        self.pushButton_18.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_18.setObjectName("pushButton_18")
        self.verticalLayout_2.addWidget(self.pushButton_18)
        self.pushButton_17 = QtWidgets.QPushButton(self.frame)
        self.pushButton_17.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_17.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setIcon(icon1)
        self.pushButton_17.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_17.setObjectName("pushButton_17")
        self.verticalLayout_2.addWidget(self.pushButton_17)
        self.pushButton_16 = QtWidgets.QPushButton(self.frame)
        self.pushButton_16.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_16.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setIcon(icon1)
        self.pushButton_16.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_16.setObjectName("pushButton_16")
        self.verticalLayout_2.addWidget(self.pushButton_16)
        self.pushButton_15 = QtWidgets.QPushButton(self.frame)
        self.pushButton_15.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_15.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setIcon(icon1)
        self.pushButton_15.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_15.setObjectName("pushButton_15")
        self.verticalLayout_2.addWidget(self.pushButton_15)
        self.pushButton_14 = QtWidgets.QPushButton(self.frame)
        self.pushButton_14.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_14.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setIcon(icon1)
        self.pushButton_14.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_2.addWidget(self.pushButton_14)
        self.pushButton_13 = QtWidgets.QPushButton(self.frame)
        self.pushButton_13.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_13.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setIcon(icon1)
        self.pushButton_13.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_13.setObjectName("pushButton_13")
        self.verticalLayout_2.addWidget(self.pushButton_13)
        self.pushButton_12 = QtWidgets.QPushButton(self.frame)
        self.pushButton_12.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_12.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setIcon(icon1)
        self.pushButton_12.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_2.addWidget(self.pushButton_12)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_9.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setIcon(icon1)
        self.pushButton_9.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_2.addWidget(self.pushButton_9)
        self.verticalLayout_3.addWidget(self.frame, 0, QtCore.Qt.AlignTop)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_2 = QtWidgets.QPushButton(self.MainContent)
        self.pushButton_2.setGeometry(QtCore.QRect(107, 600, 200, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/shopping-cart.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("background-color:rgba(0, 0, 0, 70); border-radius: 10px")
        self.pushButton_2.setVisible(False)
        self.verticalLayout.addWidget(self.MainContent)
        self.horizontalLayout.addWidget(self.MainWidget)
        MainWindow.setCentralWidget(self.CentralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Update()

    def Update(self):
        buttonHeight = 100
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 414, (buttonHeight+self.verticalLayout_2.spacing())*self.productCounts+self.verticalLayout_2.spacing()))
        for i in reversed(range(self.verticalLayout_2.count())):
            self.verticalLayout_2.itemAt(i).widget().setParent(None)
        for i in range(self.productCounts):
            self.buttons.append(QtWidgets.QPushButton(self.frame))
            self.buttons[i].setMinimumSize(QtCore.QSize(0, buttonHeight))
            self.buttons[i].setMaximumSize(QtCore.QSize(16777215, buttonHeight))

            font = QtGui.QFont()
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.buttons[i].setFont(font)

            icon1 = QtGui.QIcon()
            icon1.addPixmap(QtGui.QPixmap(self.res[i][3]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.buttons[i].setIcon(icon1)
            self.buttons[i].setIconSize(QtCore.QSize(66, 66))

            self.buttons[i].setObjectName(self.res[i][1])
            self.buttons[i].setText(self.res[i][1] + " - " + str(self.res[i][2]) + "руб.")
            self.buttons[i].setStyleSheet("text-align: left; border-radius: 5px")
            self.verticalLayout_2.addWidget(self.buttons[i])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "BurgerBurger"))
        self.pushButton_10.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_10.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.pushButton_11.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_11.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.pushButton_21.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_21.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.pushButton_20.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_20.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.pushButton_19.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_19.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.pushButton_18.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_18.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.pushButton_17.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_17.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.pushButton_16.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_16.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.pushButton_15.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_15.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.pushButton_14.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_14.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.pushButton_13.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_13.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.pushButton_12.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_12.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.pushButton_9.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_9.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.pushButton_2.setText(_translate("MainWindow", "Корзина (0)"))
import resources_rc
