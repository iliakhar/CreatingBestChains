from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import (QFont, QPixmap, QIcon)
import sys

class GrammarWidget(QWidget):

    def __init__ (self):
        super().__init__()
        self.initUI()

    def initUI(self):
        mainHLay = QHBoxLayout()
        grammarVLay = QVBoxLayout()
        btnHLay = QHBoxLayout()
        btnVLay = QVBoxLayout()

        self.grammarFrame = QFrame()
        self.grammarFrame.setFrameShape(QFrame.StyledPanel)
        self.grammarFrame.setLayout(grammarVLay)

        fontBig = QFont('Arial', 15)

        self.title = QLabel('КС - грамматика:')
        self.title.setContentsMargins(0, 0, 0, 0)
        self.title.setFont(fontBig)

        self.grammarText = QTextEdit('Asfasf\r\nsfgsfg\nsgdgd')
        self.grammarText.setAcceptRichText(False)
        self.grammarText.setFont(fontBig)
        self.grammarText.setFrameShape(QFrame.Box)

        self.editBtn = self.CreateBtn('Изменить', fontBig, 50)
        self.saveBtn = self.CreateBtn('Сохранить', fontBig, 50)
        self.loadBtn = self.CreateBtn('Загрузить', fontBig, 50)

        grammarVLay.setSpacing(10)
        mainHLay.addWidget(self.grammarFrame, 1)
        grammarVLay.addWidget(self.title,0)
        grammarVLay.addWidget(self.grammarText,1)
        grammarVLay.addLayout(btnVLay, 0)
        btnHLay.addWidget(self.saveBtn)
        btnHLay.addWidget(self.loadBtn)
        btnVLay.addWidget(self.editBtn)
        btnVLay.addLayout(btnHLay)
        self.setLayout(mainHLay)

    def CreateBtn(self, title: str, font: QFont, minH: int):
        btn = QPushButton(title)
        btn.setFont(font)
        btn.setMinimumHeight(minH)
        return btn
