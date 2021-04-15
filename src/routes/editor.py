import sys
import json
from PyQt5.QtCore import pyqtSlot,Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog,QMessageBox
from PyQt5 import QtGui

from src.build.st_edit import Ui_Editor as EditorWindow

class Editor(QMainWindow, EditorWindow):
    def __init__(self, app, config_path, parent = None):
        super(Editor,self).__init__(parent)
        self.setupUi(self)
        self.show()

        self.app = app
        self.preview = None

        self.config_file = open(config_path,"r")
        self.config = json.loads(self.config_file.read())

        self.load_style()

        self.b_build.clicked.connect(self.build_style)
        self.b_save.clicked.connect(self.save_style)
        self.b_import.clicked.connect(self.import_style)

        

    def import_style (self):
        try:
            fname = QFileDialog.getOpenFileName(self, 'Load Style From file', 'Stylesheet',"Select file (*.txt *.css *.qss)")
            selected_file = str(fname[0])

            file_stream = open(selected_file, 'r')
            
            selected_file_data = file_stream.read()
            file_stream.close()

            dialog = QMessageBox.question(
                self, 
                "WARNING", 
                "Load selected file ?",
                QMessageBox.Yes,
                QMessageBox.No
            )

            if dialog == QMessageBox.Yes: 
                self.load_style(False, selected_file_data)
            else: pass

        except FileNotFoundError:pass

    def build_style (self):
        input_content = str(self.input.toPlainText())
        self.app.setStyleSheet(input_content)

    def save_style (self):
        input_content = str(self.input.toPlainText())
        css_file_path = self.config.get("css-file-dir")

        with open(css_file_path, 'w') as css_file:
            css_file.write(input_content)
        
    def load_style (self, from_file=True, css=""):
        if from_file:
            self.input.setPlainText(self.read_css_file())
            self.app.setStyleSheet(self.read_css_file())
        else:
            self.input.setPlainText(css)
            self.app.setStyleSheet(css)

    def read_css_file (self):
        css_file_path = self.config.get("css-file-dir")
        css_data = ""

        with open(css_file_path, "r") as css_file:
            css_data = css_file.read()
        
        return css_data


    def closeEvent(self,sender):
        dialog = QMessageBox.question(
            self, 
            "Exit", 
            "Do you want to save the changes to this document before closing ? \n If you dont save, you changes will be lost.", 
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
        )

        if dialog   == QMessageBox.Save: 
            self.save_style()
            sender.accept()
            self.app.exit()
        elif dialog == QMessageBox.Discard: 
            sender.accept()
            self.app.exit()
        elif dialog == QMessageBox.Cancel: 
            sender.ignore()
        else:
            sender.ignore()
