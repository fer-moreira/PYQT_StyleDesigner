# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Lib\Layout\st_edit.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Editor(object):
    def setupUi(self, Editor):
        Editor.setObjectName("Editor")
        Editor.setWindowModality(QtCore.Qt.WindowModal)
        Editor.resize(496, 624)
        self.grid = QtWidgets.QWidget(Editor)
        self.grid.setObjectName("grid")
        self.gridLayout = QtWidgets.QGridLayout(self.grid)
        self.gridLayout.setObjectName("gridLayout")
        self.input = QtWidgets.QPlainTextEdit(self.grid)
        self.input.setObjectName("input")
        self.gridLayout.addWidget(self.input, 0, 0, 1, 3)
        self.b_build = QtWidgets.QPushButton(self.grid)
        self.b_build.setMinimumSize(QtCore.QSize(0, 40))
        self.b_build.setMaximumSize(QtCore.QSize(16777215, 40))
        self.b_build.setObjectName("b_build")
        self.gridLayout.addWidget(self.b_build, 1, 0, 1, 1)
        self.b_save = QtWidgets.QPushButton(self.grid)
        self.b_save.setMinimumSize(QtCore.QSize(0, 40))
        self.b_save.setMaximumSize(QtCore.QSize(16777215, 40))
        self.b_save.setObjectName("b_save")
        self.gridLayout.addWidget(self.b_save, 1, 1, 1, 1)
        self.b_import = QtWidgets.QPushButton(self.grid)
        self.b_import.setMinimumSize(QtCore.QSize(0, 40))
        self.b_import.setMaximumSize(QtCore.QSize(16777215, 40))
        self.b_import.setObjectName("b_import")
        self.gridLayout.addWidget(self.b_import, 1, 2, 1, 1)
        Editor.setCentralWidget(self.grid)

        self.retranslateUi(Editor)
        QtCore.QMetaObject.connectSlotsByName(Editor)

    def retranslateUi(self, Editor):
        _translate = QtCore.QCoreApplication.translate
        Editor.setWindowTitle(_translate("Editor", "MainWindow"))
        Editor.setToolTip(_translate("Editor", "QMainWindow"))
        self.grid.setToolTip(_translate("Editor", "QWidget"))
        self.input.setToolTip(_translate("Editor", "QPlainTextEdit"))
        self.b_build.setToolTip(_translate("Editor", "QPushButton"))
        self.b_build.setText(_translate("Editor", "BUILD"))
        self.b_build.setShortcut(_translate("Editor", "F9"))
        self.b_save.setToolTip(_translate("Editor", "QPushButton"))
        self.b_save.setText(_translate("Editor", "SAVE"))
        self.b_save.setShortcut(_translate("Editor", "Ctrl+S"))
        self.b_import.setToolTip(_translate("Editor", "QPushButton"))
        self.b_import.setText(_translate("Editor", "IMPORT"))
        self.b_import.setShortcut(_translate("Editor", "Ctrl+W"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Editor = QtWidgets.QMainWindow()
    ui = Ui_Editor()
    ui.setupUi(Editor)
    Editor.show()
    sys.exit(app.exec_())
