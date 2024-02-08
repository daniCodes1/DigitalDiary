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


    def do_login(self):
        email = self.email.text()
        password = self.password.text()
        print("Successfully logged in with email: ", email, " and password: ", password)
        self.close()



app = QApplication(sys.argv)
main_window = Login()
widget = QtWidgets.QStackedWidget()  # makes a stack of diff dialogs, can incr. index & change screen
widget.addWidget(main_window)
widget.setFixedWidth(500)
widget.setFixedHeight(600)
widget.show()

app.exec_()

