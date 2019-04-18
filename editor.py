import sys

from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog,QMessageBox
from PyQt5 import QtGui

from Lib.Script.st_preview import Ui_Preview
from Lib.Script.st_edit import Ui_Editor

app = QApplication(sys.argv)
app.processEvents()

class Editor(QMainWindow,Ui_Editor):
    def __init__(self, parent = None):
        super(Editor,self).__init__(parent)
        self.setupUi(self)
        self.show()
        self.move(750,150)

        self.preview = Preview()

        self.load_style_from_file()
        self.changeStyle()

        self.b_build.clicked.connect(self.changeStyle)
        self.b_import.clicked.connect(self.import_style_to_input)
        self.b_save.clicked.connect(self.save_style_in_file)

    def save_style_in_file (self):
        styleFile = open(r'assets\_stylesheet.css','w')
        _style = str(self.input.toPlainText())
        styleFile.write(_style)
        styleFile.close()
        
    def import_style_to_input (self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Load Style From file', 'Stylesheet',"Select file (*.txt *.css *.qss)")
            selectFilePath = str(fname[0])
            fileopen = open(r'%s'%selectFilePath,'r')
            _content = str(fileopen.read())
            fileopen.close()

            dialog = QMessageBox.question(self, "WARNING", "Load selected file ?",QMessageBox.Yes,QMessageBox.No)

            if dialog == QMessageBox.Yes:
                self.input.setPlainText(_content)
        except FileNotFoundError:pass


    def load_style_from_file (self):
        styleFile = open(r'assets\_stylesheet.css','r')
        _style = str(styleFile.read())
        self.input.setPlainText(_style)
        styleFile.close()
        
    def changeStyle (self):
        _style = str(self.input.toPlainText())
        app.setStyleSheet(_style)

    def closeEvent(self,sender):
        dialog = QMessageBox.question(self, "Save Style ?   ", "Do you want to save the changes to this document before closing ? \n If you dont save, you changes will be lost.",QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)

        if dialog == QMessageBox.Save       : self.save_style_in_file() ; sender.accept() ; app.exit()
        elif dialog == QMessageBox.Discard  : sender.accept();app.exit()
        elif dialog == QMessageBox.Cancel   : sender.ignore()          


class Preview (QMainWindow,Ui_Preview):
    def __init__(self, parent = None):
        super(Preview,self).__init__(parent)
        self.setupUi(self)
        self.show()
        self.move(135,150)


    def closeEvent (self,sender):
        sender.ignore()

Editor_GUI = Editor()
sys.exit(app.exec_())
