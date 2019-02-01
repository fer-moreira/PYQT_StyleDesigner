import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui

from Lib.Script.st_preview import Ui_preview


app = QApplication(sys.argv)
app.processEvents()

class Editor(QMainWindow,Ui_preview):
    def __init__(self, parent = None):
        super(Editor,self).__init__(parent)
        self.setupUi(self)
        self._default_style = open(r'assets\_stylesheet.css','r').read()
        self.input.setPlainText(str(self._default_style))
        self.setStyle()
        self.showMaximized()




        self.build.clicked.connect(self.setStyle)

    def setStyle (self):
        _style = self.input.toPlainText()
        self.setStyleSheet(str(_style))

Main_GUI = Editor()
sys.exit(app.exec_())