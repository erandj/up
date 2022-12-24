import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
import MainWindow
import AccountWindow
import RegistrationWindow
import BasketWindow
import sqlite3


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.account = account
        self.basket = basket

        self.ui.pushButton.clicked.connect(self.MoveToAccountWindow)
        self.ui.pushButton_2.clicked.connect(self.Buy)

        for i in range(self.ui.productCounts):
            self.ui.buttons[i].clicked.connect(self.AddToBasket)

    def AddToBasket(self):
        self.basket.append(self.sender().objectName())
        self.ui.pushButton_2.setText(f'Корзина ({len(self.basket)})')
        self.ui.pushButton_2.setVisible(True)

    def Buy(self):
        global basket
        basket = self.basket
        self.newWindow = Basket()
        self.newWindow.show()
        self.close()

    def MoveToAccountWindow(self):
        if self.account != '':
            self.newWindow = Account(account)
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

        cur = conn.cursor()

        res = cur.execute("SELECT phone FROM accounts").fetchall()
        if not (self.number,) in res:
            cur.execute("INSERT INTO accounts(phone) VALUES (?)", (self.number,))
            conn.commit()



        self.newWindow = Account(self.number)
        self.newWindow.show()
        self.close()


class Account(QMainWindow):
    def __init__(self, account):
        super(Account, self).__init__()
        self.ui = AccountWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.account = account

        if len(account) == 11:
            self.account = account[0] + " (" + account[1:4] + ") " + account[4:7] + "-" + account[7:9] + "-" + account[9:11]
        elif len(account) == 12:
            self.account = account[0] + " (" + account[1:5] + ") " + account[5:8] + "-" + account[8:10] + "-" + account[10:12]

        self.ui.numberLabel.setText(self.account)

        self.ui.pushButton_4.clicked.connect(self.MoveBack)

    def MoveBack(self):
        self.newWindow = Main()
        self.newWindow.show()
        self.close()


class Basket(QMainWindow):
    def __init__(self):
        super(Basket, self).__init__()
        self.ui = BasketWindow.Ui_MainWindow(basket)
        self.ui.setupUi(self)

        self.ui.pushButton_4.clicked.connect(self.MoveBack)

    def MoveBack(self):
        self.newWindow = Main()
        self.newWindow.show()
        self.close()

account = ''
basket = []
conn = sqlite3.connect('db.db')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
