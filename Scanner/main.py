from Scanner import *
from SymbolTable import *
from ProgramInternalForm import *
from FileManipulator import FileManipulator

def main():
    filename = 'input.txt'
    pifFile = 'PIF.txt'
    stFile = 'SymbolTable.txt'

    print(codificationTable)

    symbolTable = SymbolTable()
    pif = ProgramInternalForm()
    fileManipulator = FileManipulator(filename, pifFile, stFile)
    scanner = Scanner(pif, symbolTable, fileManipulator)

    fileManipulator.readFromFile(scanner)
    scanner.scan(filename)

if __name__ == '__main__':
    main()