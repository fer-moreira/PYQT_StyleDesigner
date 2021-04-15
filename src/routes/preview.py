import sys

from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog,QMessageBox
from PyQt5 import QtGui

from src.build.st_preview import Ui_Preview as PreviewWindow


class Preview (QMainWindow, PreviewWindow):
    def __init__(self, app, config_path, parent = None):
        super(Preview,self).__init__(parent)
        self.setupUi(self)
        self.show()
        self.move(135,150)
        self.app = app

    # def closeEvent (self,sender):
    #     sys.exit(self.app.exec_())

