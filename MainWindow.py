# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
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
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(12, 12, 12, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.product1 = QtWidgets.QPushButton(self.widget)
        self.product1.setMinimumSize(QtCore.QSize(0, 80))
        self.product1.setObjectName("product1")
        self.verticalLayout_2.addWidget(self.product1)
        self.product2 = QtWidgets.QPushButton(self.widget)
        self.product2.setMinimumSize(QtCore.QSize(0, 80))
        self.product2.setObjectName("product2")
        self.verticalLayout_2.addWidget(self.product2)
        self.product3 = QtWidgets.QPushButton(self.widget)
        self.product3.setMinimumSize(QtCore.QSize(0, 80))
        self.product3.setObjectName("product3")
        self.verticalLayout_2.addWidget(self.product3)
        self.product4 = QtWidgets.QPushButton(self.widget)
        self.product4.setMinimumSize(QtCore.QSize(0, 80))
        self.product4.setObjectName("product4")
        self.verticalLayout_2.addWidget(self.product4)
        self.product5 = QtWidgets.QPushButton(self.widget)
        self.product5.setMinimumSize(QtCore.QSize(0, 80))
        self.product5.setObjectName("product5")
        self.verticalLayout_2.addWidget(self.product5)
        self.verticalLayout_3.addWidget(self.widget, 0, QtCore.Qt.AlignTop)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.MainContent)
        self.horizontalLayout.addWidget(self.MainWidget)
        MainWindow.setCentralWidget(self.CentralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "BurgerBurger"))
        self.product1.setText(_translate("MainWindow", "PushButton"))
        self.product2.setText(_translate("MainWindow", "PushButton"))
        self.product3.setText(_translate("MainWindow", "PushButton"))
        self.product4.setText(_translate("MainWindow", "PushButton"))
        self.product5.setText(_translate("MainWindow", "PushButton"))
import resources_rc
