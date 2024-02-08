import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic


# USING QT DESIGNER

class Login(QDialog):

    def __init__(self):
        super(Login, self).__init__(None)
        uic.loadUi("log_in.ui", self)
        self.login_button.clicked.connect(self.do_login)
        self.password.setEchoMode(QLineEdit.Password)
        self.create_acc_button.clicked.connect(self.do_signup)

    def do_login(self):
        email = self.email.text()
        password = self.password.text()
        print("Successfully logged in with email: ", email, " and password: ", password)
        self.close()

    def do_signup(self):
        create_acc = CreateAcc()
        widget.addWidget(create_acc)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class CreateAcc(QDialog):

    def __init__(self):
        super(CreateAcc, self).__init__()
        uic.loadUi("create_acc.ui", self)
        self.signup_button.clicked.connect(self.create_acc_func)
        self.password.setEchoMode(QLineEdit.Password)
        self.password_confirm.setEchoMode(QLineEdit.Password)

    def create_acc_func(self):
        email = self.email.text()
        if self.password.text() == self.password_confirm.text():
            password = self.password.text()
            print("Successfully created account with email: ", email, " and password: ", password)
            self.close()
        else:
            print("Passwords do not match. Please try again.")


app = QApplication(sys.argv)
main_window = Login()
widget = QtWidgets.QStackedWidget()  # makes a stack of diff dialogs, can incr. index & change screen
widget.addWidget(main_window)
widget.setFixedWidth(500)
widget.setFixedHeight(600)
widget.show()

app.exec_()

