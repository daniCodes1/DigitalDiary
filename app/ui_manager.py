
from PyQt5.QtWidgets import *


def make_message_box(message):
    popup = QMessageBox()
    popup.setText(message)
    popup.exec_()

