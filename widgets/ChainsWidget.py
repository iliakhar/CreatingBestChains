from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import (QFont, QPixmap, QIcon)
import sys

class ChainsWidget(QWidget):

    def __init__ (self):
        super().__init__()
        self.initUI()

    def initUI(self):
        mainHLay = QHBoxLayout()
        chainsVLay = QVBoxLayout()
        rangeHLay = QHBoxLayout()
        btnHLay = QHBoxLayout()
        btnVLay = QVBoxLayout()

        self.chainsFrame = QFrame()
        self.chainsFrame.setFrameShape(QFrame.StyledPanel)
        self.chainsFrame.setLayout(chainsVLay)

        fontBig = QFont('Arial', 15)

        self.title = QLabel('Цепочки:')
        self.title.setFont(fontBig)

        self.rangeLbl = QLabel('Диапазон:')
        self.rangeLbl.setFont(fontBig)

        self.fromLbl = QLabel('от')
        self.fromLbl.setFont(fontBig)

        self.fromField = QSpinBox()
        self.fromField.setFont(fontBig)
        self.fromField.setFixedWidth(80)
        self.fromField.setMaximum(500)

        self.toLbl = QLabel('до')
        self.toLbl.setFont(fontBig)

        self.toField = QSpinBox()
        self.toField.setFont(fontBig)
        self.toField.setFixedWidth(80)
        self.toField.setMaximum(500)

        self.chainsList = QListWidget()
        self.chainsList.setFont(fontBig)
        self.chainsList.addItems(['afdsf','afadfazcxvz'])

        self.createBtn = self.CreateBtn('Составить', fontBig, 50)
        self.clearBtn = self.CreateBtn('Очистить', fontBig, 50)

        chainsVLay.setSpacing(10)
        mainHLay.addWidget(self.chainsFrame, 1)
        chainsVLay.addWidget(self.title,0)
        chainsVLay.addLayout(rangeHLay)
        rangeHLay.addWidget(self.rangeLbl)
        rangeHLay.addWidget(self.fromLbl)
        rangeHLay.addWidget(self.fromField)
        rangeHLay.addSpacing(10)
        rangeHLay.addWidget(self.toLbl)
        rangeHLay.addWidget(self.toField)
        rangeHLay.addStretch(1)
        chainsVLay.addWidget(self.chainsList)
        chainsVLay.addLayout(btnVLay, 0)
        btnHLay.addWidget(self.createBtn)
        btnHLay.addWidget(self.clearBtn)
        btnVLay.addLayout(btnHLay)
        self.setLayout(mainHLay)

    def CreateBtn(self, title: str, font: QFont, minH: int):
        btn = QPushButton(title)
        btn.setFont(font)
        btn.setMinimumHeight(minH)
        return btn
