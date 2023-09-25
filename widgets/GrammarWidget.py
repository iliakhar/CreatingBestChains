from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import (QFont, QPixmap, QIcon)
from widgets.GrammarEditorWidget import *
from Grammar import *
import sys

class GrammarWidget(QWidget):
    changeKsGrammar = QtCore.pyqtSignal(str)
    def __init__ (self):
        super().__init__()
        self.ksGr: KSGrammar = None
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

        self.grammarText = QTextEdit()
        self.grammarText.setReadOnly(True)
        # self.grammarText.setAcceptRichText(False)
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

        self.editBtn.clicked.connect(self.OpenEditWind)
        self.saveBtn.clicked.connect(self.SaveToFile)
        self.loadBtn.clicked.connect(self.LoadFromFile)

    def SaveToFile(self):
        if self.ksGr is not None:
            filename, _ = QFileDialog.getSaveFileName(None, "Save File", ".", "Text Files (*.txt);;All Files (*)")
            self.ksGr.SaveToFile(filename)
    def LoadFromFile(self):
        if self.ksGr is None: self.ksGr = KSGrammar()
        filename, _ = QFileDialog.getOpenFileName(None, "Open File", ".", "Text Files (*.txt);;All Files (*)")
        self.ksGr.LoadFromFile(filename)
        self.grammarText.setText(self.ksGr.GetKSGrammText())
        self.changeKsGrammar.emit('')
    def CreateBtn(self, title: str, font: QFont, minH: int):
        btn = QPushButton(title)
        btn.setFont(font)
        btn.setMinimumHeight(minH)
        return btn

    @QtCore.pyqtSlot()
    def OpenEditWind(self):
        dlg = GrammarEditorWidget(self.ksGr)
        dlg.setWindowTitle("Изменение грамматики")
        dlg.exec()
        if dlg.isGoodGrammar == True:
            self.ksGr = copy.deepcopy(dlg.ksGr)
            self.grammarText.setText(self.ksGr.GetKSGrammText())
            self.changeKsGrammar.emit('')