from PyQt5.QtWidgets import *
from PyQt5.QtGui import (QFont, QPixmap, QIcon)
from PyQt5.QtCore import *
from widgets.GrammarWidget import GrammarWidget
from widgets.ChainsWidget import ChainsWidget
import copy
import sys
from Grammar import KSGrammar

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.InitUi()
    def InitUi(self):

        self.setWindowTitle('Построение дерева вывода')
        self.setWindowIcon(QIcon('icon/tree.png'))
        self.move(300, 300)
        self.resize(1000, 700)

        controlHLay = QHBoxLayout()
        mainHLay = QHBoxLayout()

        # ksGr = KSGrammar()
        # ksGr.term = '0123456789-+='
        # ksGr.nterm.update({'S': ['T', '+T', '-T'],
        #                    'T': ['F', 'TF'],
        #                    'F': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']})
        # ksGr.start = 'S'
        # ksGr.SetSizeRange([1, 2])

        self.grammarWid = GrammarWidget()
        self.chainsWid = ChainsWidget()
        # self.chainsWid.ksGr = ksGr


        mainHLay.addLayout(controlHLay)

        controlHLay.addWidget(self.grammarWid,2)
        controlHLay.addWidget(self.chainsWid,5)
        # mainHLay.addWidget(self.workSpaceFrame, 6)
        self.setLayout(mainHLay)

        self.grammarWid.changeKsGrammar.connect(self.ChangeKsGrammar)

    def ChangeKsGrammar(self):
        self.chainsWid.ksGr = copy.deepcopy(self.grammarWid.ksGr)