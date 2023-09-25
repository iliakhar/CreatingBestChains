from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import (QFont, QPixmap, QIcon)
from Grammar import KSGrammar
from widgets.AddNtermWidget import *
import copy
import sys

class GrammarEditorWidget(QDialog):

    def __init__ (self, ksGr: KSGrammar = None):
        super().__init__()
        self.isGoodGrammar = False
        self.ksGr = copy.deepcopy(ksGr)
        self.initUI()

    def initUI(self):

        mainVLay = QVBoxLayout()
        hLay = QHBoxLayout()
        lblVLay = QVBoxLayout()
        textVLay = QVBoxLayout()
        ntermHLay = QHBoxLayout()
        btnHLay = QHBoxLayout()
        exitHLay = QHBoxLayout()
        self.setLayout(mainVLay)
        mainVLay.setSpacing(10)

        self.setMinimumWidth(500)

        fontBig = QFont('Arial', 15)

        self.beginWithLbl = QLabel('Начинать с: ')
        self.beginWithLbl.setFont(fontBig)

        self.beginWithText = QLineEdit()
        self.beginWithText.setMaximumWidth(100)
        self.beginWithText.setFont(fontBig)
        self.beginWithText.setMaxLength(1)

        # self.beginWithText.setFrameShape(QFrame.Box)

        self.termLbl = QLabel('Терминальные: ')
        self.termLbl.setFont(fontBig)

        self.termText = QLineEdit()
        self.termText.setFont(fontBig)
        # print('AAA')

        self.ntermLbl = QLabel('Правила: ')
        # self.title.setContentsMargins(0, 0, 0, 0)
        self.ntermLbl.setFont(fontBig)

        self.ntermList = QListWidget()
        self.ntermList.setFont(fontBig)
        self.ntermList.setSpacing(6)

        self.addBtn = self.CreateBtn('Добавить', fontBig, 45)
        self.editBtn = self.CreateBtn('Изменить', fontBig, 45)
        self.delBtn = self.CreateBtn('Удалить', fontBig, 45)
        self.acceptBtn = self.CreateBtn(' Готово ', fontBig, 45,120)
        self.cancelBtn = self.CreateBtn(' Отмена ', fontBig, 45, 120)

        mainVLay.addLayout(hLay)
        mainVLay.addLayout(ntermHLay)
        mainVLay.addWidget(self.ntermList)
        mainVLay.addLayout(btnHLay)
        mainVLay.addLayout(exitHLay)
        hLay.addLayout(lblVLay)
        hLay.addLayout(textVLay)
        lblVLay.addWidget(self.beginWithLbl)
        lblVLay.addWidget(self.termLbl)
        textVLay.addWidget(self.beginWithText)
        textVLay.addWidget(self.termText)
        ntermHLay.addWidget(self.ntermLbl)
        ntermHLay.addStretch(1)
        btnHLay.addWidget(self.addBtn)
        btnHLay.addWidget(self.editBtn)
        btnHLay.addWidget(self.delBtn)
        exitHLay.addStretch(1)
        exitHLay.addWidget(self.acceptBtn)
        exitHLay.addWidget(self.cancelBtn)

        if self.ksGr is None:
            self.ksGr = KSGrammar()
        else:
            self.termText.setText(self.ksGr.term)
            self.beginWithText.setText(self.ksGr.start)
            for key, val in self.ksGr.nterm.items():
                self.ntermList.addItem(key + ': ' + '|'.join(val))

        self.addBtn.clicked.connect(self.AddNterm)
        self.editBtn.clicked.connect(self.EditNterm)
        self.delBtn.clicked.connect(self.DelNterm)
        self.acceptBtn.clicked.connect(self.Accept)
        self.cancelBtn.clicked.connect(self.Cancel)

    def Accept(self):
        self.ksGr.start = self.beginWithText.text()
        self.ksGr.term = self.termText.text()
        self.isGoodGrammar = self.ksGr.CheckValid()
        if self.isGoodGrammar == True:
            self.close()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Information MessageBox")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText('Ошибка')
            msg.exec_()
    def Cancel(self):
        self.close()

    def AddNterm(self):
        dlg = AddNtermWidget(self.ksGr.nterm.keys())
        dlg.setWindowTitle("Добавление нетерминального символа")
        dlg.exec()
        if len(dlg.nterm) != 0:
            key = dlg.nterm[0]
            val = list(filter(None, dlg.nterm[1].split('|')))
            self.ksGr.nterm.update({key:val})
            self.ntermList.addItem(key+': '+'|'.join(val))

    def DelNterm(self):
        curItem = self.ntermList.currentItem()
        if curItem is not None:
            self.ksGr.nterm.pop(curItem.text()[0])
            self.ntermList.takeItem(self.ntermList.currentIndex().row())



    def EditNterm(self):
        curItem = self.ntermList.currentItem()
        if curItem is not None:
            dlg = AddNtermWidget(self.ksGr.nterm.keys(), curItem.text())
            dlg.setWindowTitle("Добавление нетерминального символа")
            dlg.exec()
            if len(dlg.nterm) != 0:
                print(self.ksGr.nterm.items())
                key = dlg.nterm[0]
                val = list(filter(None, dlg.nterm[1].split('|')))
                self.ksGr.nterm.update({key:val})
                curItem.setText(key+': '+'|'.join(val))
                # print(self.ksGr.nterm.items())

    def CreateBtn(self, title: str, font: QFont, minH: int, minW = -1):
        btn = QPushButton(title)
        btn.setFont(font)
        btn.setMinimumHeight(minH)
        if minW!=-1:
            btn.setMinimumWidth(minW)
        return btn
