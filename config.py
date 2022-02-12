# -*- coding: utf-8 -*-
import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QGridLayout, QPushButton, QLineEdit

APPINFO = {
    "Title": "Hypertraductor Config",
    "Width": 500,
    "Height": 600,
    "Background-color": "blue"
}

USERINFO = {
    "OriginPath": None,
    "TranslationPath": None
}


class UI(QWidget):
    def __init__(self):
        super().__init__()

        self.grid = QGridLayout()
        self.origin = QLineEdit()
        self.translation = QLineEdit()
        self.originLocation = QLabel("Fichiers originaux :")
        self.translationLocation = QLabel("Fichiers traduits :")
        self.saveButton = QPushButton("Save")

        self.setGeometry(200, 200, 700, 300)
        self.setWindowTitle(APPINFO["Title"])
        self.setWindowIcon(QIcon('HypertraductorLogo.ico'))
        self.initUI()

    def initUI(self):
        self.grid.addWidget(self.originLocation, 0, 0, 1, 1)
        self.grid.addWidget(self.origin, 0, 1, 1, 2)
        self.grid.addWidget(self.translationLocation, 1, 0, 1, 1)
        self.grid.addWidget(self.translation, 1, 1, 1, 2)
        self.grid.addWidget(self.saveButton, 2, 1, 1, 1)

        self.grid.setSpacing(10)
        self.setLayout(self.grid)
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec())
