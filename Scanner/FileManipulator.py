from LanguageSpecification import operators, lexic, separators, codificationTable
from prettytable import PrettyTable

class FileManipulator:
    def __init__(self, input, pifFile, stFile):
        self.input = input
        self.pifFile = pifFile
        self.stFile = stFile

    def readFromFile(self, scanner):
        file = open(self.input, 'r')
        for line in file:
            print(line)

        with open(self.input, 'r') as file:
            for line in file:
                print([token for token in scanner.detectToken(line)])

    def writePifToFile(self, pif):
        with open(self.pifFile, 'w') as f:
            f.write('The Program Internal Form:\n')
            pifElements = pif.getPIF()
            t = PrettyTable(['Code', 'ID'])
            for elem in pifElements:
                t.add_row(elem)
            f.write(str(t))
        f.close()

    def writeSymbolTableToFile(self, symbolTable):
        with open(self.stFile, 'w') as f:
            f.write('Symbol Table:\n')
            symbolTableElements = symbolTable.getHashTable()
            t = PrettyTable(['Pos', 'Token'])
            for (key, value) in symbolTableElements.items():
                if value != []:
                    t.add_row((key, value))
            f.write(str(t))
        f.close()