from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import (QFont, QPixmap, QIcon)
from Grammar import KSGrammar
import sys


class AddNtermWidget(QDialog):

    def __init__(self, ntermKeyLst, prevVal = None):
        super().__init__()
        self.nTermKeyLst = ntermKeyLst
        self.prevVal = prevVal
        self.nterm = []
        self.initUI()

    def initUI(self):
        mainVLay = QVBoxLayout()
        hLay = QHBoxLayout()
        lblVLay = QVBoxLayout()
        textVLay = QVBoxLayout()
        exitHLay = QHBoxLayout()
        self.setLayout(mainVLay)
        mainVLay.setSpacing(10)

        self.setMinimumWidth(400)
        self.setMinimumHeight(150)

        fontBig = QFont('Arial', 13)

        self.ntermLbl = QLabel('Символ: ')
        self.ntermLbl.setFont(fontBig)

        self.ntermText = QLineEdit()
        self.ntermText.setFont(fontBig)
        self.ntermText.setMaxLength(1)
        self.ntermText.setMaximumWidth(100)

        self.ruleLbl = QLabel('Правила(через |): ')
        self.ruleLbl.setFont(fontBig)

        self.ruleText = QLineEdit()
        self.ruleText.setFont(fontBig)

        self.acceptBtn = self.CreateBtn(' Готово ', fontBig, 35, 80)
        self.cancelBtn = self.CreateBtn(' Отмена ', fontBig, 35, 80)

        if self.prevVal is not None:
            self.ntermText.setText(self.prevVal[0])
            self.ruleText.setText(self.prevVal[3:])

        mainVLay.addLayout(hLay)
        mainVLay.addLayout(exitHLay,1)
        hLay.addLayout(lblVLay)
        hLay.addLayout(textVLay)
        lblVLay.addWidget(self.ntermLbl)
        textVLay.addWidget(self.ntermText)
        lblVLay.addWidget(self.ruleLbl)
        textVLay.addWidget(self.ruleText)
        exitHLay.addStretch(1)
        exitHLay.addWidget(self.acceptBtn)
        exitHLay.addWidget(self.cancelBtn)

        self.acceptBtn.clicked.connect(self.Accept)
        self.cancelBtn.clicked.connect(self.Cancel)

    def Cancel(self):
        self.close()

    def Accept(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Information MessageBox")
        msg.setStandardButtons(QMessageBox.Ok)
        if self.ntermText.text() == '':
            msg.setText('Поле символ пустое')
            msg.exec_()
        elif self.ruleText.text() == '':
            msg.setText('Поле правила пустое')
            msg.exec_()
        else:
            if self.prevVal is None:
                if self.ntermText.text() in self.nTermKeyLst:
                    msg.setText('Нетермиальный символ уже существует')
                    msg.exec_()
                else:
                    self.nterm = [self.ntermText.text(), self.ruleText.text()]
                    self.close()
            else:
                if (self.ntermText.text() in self.nTermKeyLst) and (self.ntermText.text() != self.prevVal[0]):
                    msg.setText('Нетермиальный символ уже существует')
                    msg.exec_()
                else:
                    self.nterm = [self.ntermText.text(), self.ruleText.text()]
                    self.close()


    def CreateBtn(self, title: str, font: QFont, minH: int, minW=-1):
        btn = QPushButton(title)
        btn.setFont(font)
        btn.setMinimumHeight(minH)
        if minW != -1:
            btn.setMinimumWidth(minW)
        return btn
