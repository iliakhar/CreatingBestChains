from Interface import *
from Grammar import KSGrammar





if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
    # ksGr = KSGrammar()
    # ksGr.term = '0123456789-+='
    # ksGr.nterm.update({'S': ['T', '+T', '-T'],
    #                    'T': ['F', 'TF'],
    #                    'F': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']})
    # ksGr.start = 'S'
    # ksGr.SetSizeRange([3, 3])
    # for i in range(ksGr.chains):
    #     print(i)
    # ksGr.nterm.update({'S': ['T', '+T', '-T'],
    #                    'T': ['ST', 'FST'],
    #                    'F': ['ST']})
    # ksGr.LoadFromFile('SavedKS.txt')
    # print(ksGr.GetKSGrammText())
    # ksGr.SaveToFile('SavedKS.txt')


    # ksGr.term = 'abc'
    # ksGr.nterm.update({'A': ['aBbbC', '*'],
    #                    'B': ['aaBb', '*'],
    #                    'C': ['cC', '*']})
    # ksGr.start = 'A'

    # ksGr.term = 'ab*'
    # ksGr.nterm.update({'S': ['A'],
    #                    'A': ['BB', '0', '*'],
    #                    'B': ['AA', '1', '*']})
    # ksGr.start = 'S'

    # ksGr.term = 'ab*'
    # ksGr.nterm.update({'S': ['A'],
    #                    'A': ['B', '0B', '*'],
    #                    'B': ['A', '1', '*']})
    # ksGr.start = 'S'

    # ksGr.GetChains()
    # for i in range(len(ksGr.chains)):
    #     print(i,')', ksGr.chains[i],': ',ksGr.chainsCreationPath[i])

