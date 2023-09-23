from Interface import *


class KSGrammar:
    term: str
    start: str
    nterm: dict

    def __init__(self):
        self.nterm = dict()
        self.chains = []
        self.chainsCreationPath = []
        self.sizeRange: [int, int]
        self.emptyChar = '*'

    def SetSizeRange(self, sizeRange: [int, int]):
        self.sizeRange = sizeRange
    def FindFirstNTermSymb(self, symbs: str):
        for i, symb in enumerate(symbs):
            if symb in self.nterm:
                return i
        return -1

    def CheckForDublicate(self, variants, chain):
        equalElemCount = 0
        for var in variants:
            # print(var[0], chain)
            if chain == var[0]: equalElemCount+=1
            if equalElemCount == 2: return 1
        return 0

    def GetChains(self):
        variants = [[self.start, 0]]
        while len(variants) != 0:
            # print(variants)

            if self.CheckForDublicate(variants, variants[-1][0]):
                variants.pop(-1)
                continue

            prevChain = variants[-1][0][:]
            prevChain = prevChain.replace(self.emptyChar, '')
            if len(prevChain) > self.sizeRange[1]+1:
                variants.pop(-1)
                continue
            nTermPos=self.FindFirstNTermSymb(prevChain)
            if nTermPos != -1:
                curNtermSymb = prevChain[nTermPos]
                if variants[-1][1] == len(self.nterm[curNtermSymb]):
                    variants.pop(-1)
                    continue
                newChain = prevChain[:nTermPos] + self.nterm[curNtermSymb][variants[-1][1]] + prevChain[nTermPos + 1:]
                variants[-1][1] += 1
                variants.append([newChain, 0])
            else:
                if (not prevChain in self.chains) and (self.sizeRange[0]<=len(prevChain)<=self.sizeRange[1]):
                    # print('AAA:', variants[rowInd][0])
                    self.chains.append(prevChain)
                    self.chainsCreationPath.append([])
                    self.chainsCreationPath[-1] = [var[0] for var in variants]

                variants.pop(-1)

    def CheckValid(self):
        if self.sizeRange[0] > self.sizeRange[1]: return False #Диапазон
        if not self.start in self.nterm.keys(): return False
        for key, value in self.nterm.items():
            if key in self.term: return False#Нетерм не является еще и терм
            for rule in value:#Используются ли только доступные терм и нетерм символы
                for symb in rule:
                    if (not symb in self.nterm) and (not symb in self.term):
                        return False
        return True

    def GetKSGrammText(self):
        text = 'G( {'
        text += ', '.join(list(self.term))
        text += '}, {'
        text += ', '.join(self.nterm.keys())
        text += '}, P, '+self.start+')\nP:\n\t'
        for key, value in self.nterm.items():
            text += key + ': ' + ' | '.join(value) + '\n\t'
        return text

    def SaveToFile(self, path: str):
        with open(path, 'w') as f:
            f.write(self.term+'\n')
            f.write(self.start+'\n')
            for key, value in self.nterm.items():
                f.write(key + ' ' + ' '.join(value) + '\n')

    def LoadFromFile(self, path: str):
        with open(path, 'r') as f:
            for i, line in enumerate(f):
                if i == 0: self.term = line[:-1]# без \n
                elif i == 1: self.start = line[:-1]
                elif line != '':
                    ntermInLst = line[:-1].split()
                    self.nterm.update({ntermInLst[0]:ntermInLst[1:]})
                    print(self.nterm.items())



if __name__ == "__main__":
    # app = QApplication(sys.argv)
    # win = MainWindow()
    # win.show()
    # sys.exit(app.exec_())
    ksGr = KSGrammar()
    # ksGr.term = '0123456789-+='
    # ksGr.nterm.update({'S': ['T', '+T', '-T'],
    #                    'T': ['F', 'TF'],
    #                    'F': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']})

    # ksGr.nterm.update({'S': ['T', '+T', '-T'],
    #                    'T': ['ST', 'FST'],
    #                    'F': ['ST']})
    # ksGr.start = 'S'
    ksGr.SetSizeRange([1, 2])
    ksGr.LoadFromFile('SavedKS.txt')
    print(ksGr.GetKSGrammText())
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

