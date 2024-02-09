import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
import secrets
import string
import hashlib
from getpass import getpass


# USING QT DESIGNER


ACCOUNT_DETAILS_FILEPATH = "users.txt"
PASSWORD_LENGTH = 8


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
        if not authenticate_user(email, password):
            print("Invalid username or password") # let them try again
        else:
            print("Successfully logged in with email: ", email, " and password: ", password)
            self.close()
            self.open_diary()

    def do_signup(self):
        create_acc = CreateAcc()
        widget.addWidget(create_acc)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def open_diary(self):
        diary = Diary()
        widget.addWidget(diary)
        widget.setCurrentIndex(widget.currentIndex() + 1)


def authenticate_user(username, password):
    with open(ACCOUNT_DETAILS_FILEPATH, "r") as f:
        for line in f:
            parts = line.split()
            if parts[0] == username:
                hashed_password = parts[1]
                if hashed_password == hash_password(password):
                    return True
                else:
                    return False
    return False


class Diary(QDialog):

    def __init__(self):
        super(Diary, self).__init__(None)
        uic.loadUi("diary.ui", self)
        self.submit_date_button.clicked.connect(self.open_new_entry)
        self.save_button.clicked.connect(self.save_entry)

    def open_new_entry(self):
        if self.date.toPlainText() == "":
            warning = QMessageBox()
            warning.setText("Please fill in the date.")
            warning.exec_()
        else:
            self.entry_box.setStyleSheet("background-color: rgb(241, 251, 250)")
            self.entry_box.setEnabled(True)

    def save_entry(self):
        make_message_box(f'Your entry for {self.date.toPlainText()} has been saved')
        # Will save the data


class CreateAcc(QDialog):

    def __init__(self):
        super(CreateAcc, self).__init__(None)
        uic.loadUi("create_acc.ui", self)
        self.signup_button.clicked.connect(self.create_acc_func)
        self.password.setEchoMode(QLineEdit.Password)
        self.password_confirm.setEchoMode(QLineEdit.Password)

    def create_acc_func(self):
        email = self.email.text()
        if self.password.text() == self.password_confirm.text():
            password = self.password.text()
            # print("Successfully created account with email: ", email, " and password: ", password)
            hashed_password = hash_password(password)
            save_user(self.email, hashed_password)
            make_message_box(f'Successfully created account for account {email}. Will redirect to log in.')
            self.close()
            login = Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex() + 1)
        else:
            print("Passwords do not match. Please try again.")


def hash_password(pwd):
    # hash a password using SHA-256 algorithm
    pwd_bytes = pwd.encode('utf-8')
    hashed_pwd = hashlib.sha256(pwd_bytes).hexdigest()
    return hashed_pwd


def save_user(email, hashed_pwd):
    # save to file
    with open(ACCOUNT_DETAILS_FILEPATH, "a") as f:
        f.write(f"{email} {hashed_pwd}\n")


def make_message_box(message):
    popup = QMessageBox()
    popup.setText(message)
    popup.exec_()


app = QApplication(sys.argv)
main_window = Login()
widget = QtWidgets.QStackedWidget()  # makes a stack of diff dialogs, can incr. index & change screen
widget.addWidget(main_window)
widget.setFixedWidth(500)
widget.setFixedHeight(600)
widget.show()

app.exec_()

