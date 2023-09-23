from PyQt5.QtWidgets import *
from PyQt5.QtGui import (QFont, QPixmap, QIcon)
from PyQt5.QtCore import *
from widgets.GrammarWidget import GrammarWidget
from widgets.ChainsWidget import ChainsWidget
import sys

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.InitUi()
    def InitUi(self):

        self.setWindowTitle('Построение дерева вывода')
        self.setWindowIcon(QIcon('icon/tree.png'))
        self.move(300, 300)
        self.resize(1000, 1000)

        controlVLay = QVBoxLayout()
        mainHLay = QHBoxLayout()

        self.grammarWid = GrammarWidget()
        self.chainsWid = ChainsWidget()


        mainHLay.addLayout(controlVLay)

        controlVLay.addWidget(self.grammarWid,3)
        controlVLay.addWidget(self.chainsWid,4)
        # mainHLay.addWidget(self.workSpaceFrame, 6)
        self.setLayout(mainHLay)