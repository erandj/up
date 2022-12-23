import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
import MainWindow
import AccountWindow
import RegistrationWindow


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.account = account

        self.ui.pushButton.clicked.connect(self.MoveToAccountWindow)

    def MoveToAccountWindow(self):
        if self.account != '':
            self.newWindow = Account()
            self.newWindow.show()
            self.close()
        else:
            self.newWindow = Registration()
            self.newWindow.show()
            self.close()


class Registration(QMainWindow):
    def __init__(self):
        super(Registration, self).__init__()
        self.ui = RegistrationWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.number = ''

        self.ui.pushButton_4.clicked.connect(self.MoveBack)
        self.ui.pushButton.clicked.connect(self.CheckNumber)

    def MoveBack(self):
        self.newWindow = Main()
        self.newWindow.show()
        self.close()

    def CheckNumber(self):
        global account

        self.number = self.ui.lineEdit.text()
        self.ui.errorLabel.setText("")

        if self.number == '':
            self.ui.errorLabel.setText("Напишите свой номер!")
            return
        if self.number[0] != '8' or len(self.number) < 10:
            self.ui.errorLabel.setText("Проверьте правильность номера!")
            return

        account = self.number

        self.newWindow = Account()
        self.newWindow.show()
        self.close()


class Account(QMainWindow):
    def __init__(self):
        super(Account, self).__init__()
        self.ui = AccountWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        if account == '':
            self.newWindow = Registration()
            self.newWindow.show()
            self.close()

        if len(account) == 11:
            self.account = account[0] + " (" + account[1:4] + ") " + account[4:7] + "-" + account[7:9] + "-" + account[9:11]
        elif len(account) == 12:
            self.account = account[0] + " (" + account[1:5] + ") " + account[5:8] + "-" + account[8:10] + "-" + account[10:12]

        self.ui.numberLabel.setText(self.account)


account = ''

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
