# -*- coding: utf-8 -*-
import sys

from PyQt6 import QtCore
from PyQt6.QtGui import QIcon, QPixmap, QFileSystemModel
from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QTextEdit, QGridLayout, QTreeView, QPushButton

import config

APPINFO = {
    "Title": "Hypertraductor",
    "Width": 1600,
    "Height": 700,
    "Background-color": "blue"
}

CONFIG = {
    "OriginPath": config.USERINFO["OriginPath"],
    "TranslationPath": config.USERINFO["TranslationPath"]
}


class UI(QWidget):
    def __init__(self):
        super().__init__()

        self.fileName = None
        self.grid = QGridLayout()
        self.pixmap = QPixmap('PlaceholderImage.jpg').scaledToWidth(650)
        self.imageOrigin = QLabel()
        self.imageTranslation = QLabel()
        self.textOrigin = QTextEdit()
        self.textTranslation = QTextEdit()
        self.labelOrigin = QLabel("Original text :")
        self.labelTranslation = QLabel("Translated text :")
        self.buttonTranslation = QPushButton("Translate")
        self.tree = QTreeView()
        self.model = QFileSystemModel()
        self.setGeometry(200, 200, APPINFO["Width"], APPINFO["Height"])
        self.setWindowTitle(APPINFO["Title"])
        self.setWindowIcon(QIcon('HypertraductorLogo.ico'))
        self.initUI()

    def initUI(self):

        self.textOrigin.setReadOnly(True)
        self.model.setRootPath(CONFIG["OriginPath"])
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(CONFIG["OriginPath"]))
        self.tree.header().setSectionHidden(1, True)
        self.tree.header().setSectionHidden(2, True)
        self.tree.header().setSectionHidden(3, True)
        self.tree.clicked.connect(self.TreeSelector)
        self.tree.setHeaderHidden(True)

        self.imageOrigin.setPixmap(self.pixmap)
        self.imageTranslation.setPixmap(self.pixmap)

        self.buttonTranslation.clicked.connect(self.Translate)

        self.grid.addWidget(self.imageOrigin, 0, 0, 1, 2)
        self.grid.addWidget(self.labelOrigin, 1, 0, 1, 1)
        self.grid.addWidget(self.textOrigin, 2, 0, 1, 2)
        self.grid.addWidget(self.imageTranslation, 0, 2, 1, 2)
        self.grid.addWidget(self.labelTranslation, 1, 2, 1, 1)
        self.grid.addWidget(self.buttonTranslation, 1, 3, 1, 1)
        self.grid.addWidget(self.textTranslation, 2, 2, 1, 2)
        self.grid.addWidget(self.tree, 0, 4, 3, 1)

        self.grid.setSpacing(10)
        self.setLayout(self.grid)
        self.show()

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def TreeSelector(self, index):
        indexItem = self.model.index(index.row(), 0, index.parent())

        self.fileName = self.model.fileName(indexItem)
        filePath = self.model.filePath(indexItem)

        self.GetOriginText(self.fileName)
        self.GetTranslationText(self.fileName)

    def GetOriginText(self, fileName):
        path = CONFIG["OriginPath"] + '\\' + fileName
        try:
            self.textOrigin.setPlainText(open(path).read())
            return
        except:
            print("Please choose a .txt file")
            return

    def GetTranslationText(self, fileName):
        path = CONFIG["TranslationPath"] + '\\' + fileName
        try:
            self.textTranslation.setPlainText(open(path).read())
            return
        except:
            print("Please choose a .txt file")
            return

    def Translate(self):
        try:
            with open(CONFIG["TranslationPath"] + '\\' + self.fileName, 'w') as f:
                f.write(self.textTranslation.toPlainText())
                return
        except:
            print("Error occurred during writing on file")
            return


def main():
    app = QApplication(sys.argv)
    if CONFIG["TranslationPath"] is None and CONFIG["OriginPath"] is None:
        ex1 = config.UI()
    else:
        ex = UI()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
