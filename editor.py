import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow,QMenuBar,QAction
from PyQt5 import QtGui

from Lib.Script.st_preview import Ui_preview
from Lib.Script.st_editor import Ui_editor


app = QApplication(sys.argv)
app.processEvents()


class Editor(QMainWindow,Ui_editor):
    def __init__(self, parent = None):
        super(Editor,self).__init__(parent)
        self.setupUi(self)
        self.show()

        self.preview = Preview()
        self.load_style_from_file()

        self.build.clicked.connect(self.changeStyle)
        self.import_2.clicked.connect(self.import_style_to_input)
        self.save_btn.clicked.connect(self.save_style_in_file)


    def save_style_in_file (self):
        styleFile = open(r'assets\_stylesheet.css','w')
        _style = str(self.input.toPlainText())
        styleFile.write(_style)
        styleFile.close()
    def import_style_to_input (self):
        print("* DEV")
    def load_style_from_file (self):
        styleFile = open(r'assets\_stylesheet.css','r')
        _style = str(styleFile.read())
        self.input.setPlainText(_style)
        styleFile.close()
    def changeStyle (self):
        _style = str(self.input.toPlainText())
        app.setStyleSheet(_style)

    

# ------------------------------------------------------------------------------------------------------------------------------

class Preview(QMainWindow,Ui_preview):
    def __init__(self, parent = None):
        super(Preview,self).__init__(parent)
        self.setupUi(self)
        self.show()



Editor_GUI = Editor()
sys.exit(app.exec_())