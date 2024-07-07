from PyQt5.QtWidgets import QApplication
from IDidentify.mainframe import MainDialog
import sys


class ID_identifyApp(QApplication):
    def __init__(self):
        super(ID_identifyApp, self).__init__(sys.argv)
        self.dialog = MainDialog()
        self.dialog.show()
