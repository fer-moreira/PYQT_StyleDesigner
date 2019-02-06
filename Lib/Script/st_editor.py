# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Lib\Layout\st_editor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_editor(object):
    def setupUi(self, editor):
        editor.setObjectName("editor")
        editor.resize(566, 632)
        self.centralwidget = QtWidgets.QWidget(editor)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.build = QtWidgets.QPushButton(self.centralwidget)
        self.build.setMinimumSize(QtCore.QSize(0, 30))
        self.build.setObjectName("build")
        self.gridLayout.addWidget(self.build, 0, 0, 1, 1)
        self.import_2 = QtWidgets.QPushButton(self.centralwidget)
        self.import_2.setMinimumSize(QtCore.QSize(0, 30))
        self.import_2.setObjectName("import_2")
        self.gridLayout.addWidget(self.import_2, 0, 1, 1, 1)
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setMinimumSize(QtCore.QSize(0, 30))
        self.save_btn.setObjectName("save_btn")
        self.gridLayout.addWidget(self.save_btn, 0, 2, 1, 1)
        self.input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input.setMinimumSize(QtCore.QSize(0, 0))
        self.input.setPlainText("")
        self.input.setObjectName("input")
        self.gridLayout.addWidget(self.input, 1, 0, 1, 3)
        editor.setCentralWidget(self.centralwidget)

        self.retranslateUi(editor)
        QtCore.QMetaObject.connectSlotsByName(editor)

    def retranslateUi(self, editor):
        _translate = QtCore.QCoreApplication.translate
        editor.setWindowTitle(_translate("editor", "MainWindow"))
        self.build.setText(_translate("editor", "BUILD"))
        self.build.setShortcut(_translate("editor", "F9"))
        self.import_2.setText(_translate("editor", "IMPORT"))
        self.import_2.setShortcut(_translate("editor", "Ctrl+W"))
        self.save_btn.setText(_translate("editor", "SAVE"))
        self.save_btn.setShortcut(_translate("editor", "Ctrl+S"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editor = QtWidgets.QMainWindow()
    ui = Ui_editor()
    ui.setupUi(editor)
    editor.show()
    sys.exit(app.exec_())

