from LanguageSpecification import operators, lexic, separators, codificationTable
import re

class Scanner:

    def __init__(self, pif, symbolTable, fileManipulator):
        self.pif = pif
        self.symbolTable = symbolTable
        self.fileManipulator = fileManipulator

    def stringWithoutQuotes(self, line, index):
        if index == 0:
            return False
        return line[index - 1] == '\\'

    def lookUp(self, char):
        for operator in operators:
            if char in operator:
                return True
        return False

    def isIdentifier(self, token):
        return re.match(r'^(?=.{1,8}$)_{0,1}[a-zA-Z]+\d*$', token)

    def isConstant(self, token):
        return re.match(r'^(true|false|\d{1}|[+-]{1}[1-9]{1}|[1-9]{1}\d*|[+-]{1}[1-9]{1}\d*|''[a-zA-Z0-9]{1}''|"[a-zA-z0-9 ]*")$', token)

    def detectStringToken(self, line, index):
        quotesNumber = 0
        token = ''

        while index < len(line) and quotesNumber < 2:
            if line[index] == '"' and not self.stringWithoutQuotes(line, index):
                quotesNumber += 1
            token += line[index]
            index += 1

        return token, index

    def detectOperatorToken(self, line, index):
        token = ''

        while index < len(line) and self.lookUp(line[index]):
            token += line[index]
            index += 1

        if token == '-' and self.isConstant(line[index]):
            token += line[index]
            index += 1

        return token, index

    def ifValidLenght(self, token):
       if token and len(token) <= 8:
            return True
       return False


    def detectToken(self, line):
        token = ''
        index = 0
        tokens = []

        while index < len(line):

            if line[index] == '"':
                if token:
                    tokens.append(token)
                token, index = self.detectStringToken(line, index)
                tokens.append(token)
                token = ''

            elif line[index] in separators:
                if token:
                    tokens.append(token)
                token, index = line[index], index + 1
                tokens.append(token)
                token = ''

            elif self.lookUp(line[index]):
                if token:
                    tokens.append(token)
                token, index = self.detectOperatorToken(line, index)
                tokens.append(token)
                token = ''

            else:
                token += line[index]
                index += 1

        if token:
            tokens.append(token)
        return tokens

    def scan(self, filename):
        errors = []
        with open(filename, 'r') as file:
            lineNumber = 0
            for line in file:
                lineNumber += 1
                for token in self.detectToken(line[0:-1]):
                    if token in lexic:
                        self.pif.add(codificationTable[token], -1)
                    elif self.isIdentifier(token):
                        id = self.symbolTable.add(token)
                        self.pif.add(codificationTable['identifier'], id)
                    elif self.isConstant(token):
                        id = self.symbolTable.add(token)
                        self.pif.add(codificationTable['constant'], id)
                    else:
                        errors.append('This ' + token + 'does not exists.')

        if len(errors) == 0:
            print("There are no errors!\n")
        else:
            print("ERRORS: \n")
            print(errors)

        print("Codification table: \n", codificationTable)

        print('Program Internal Form: \n', self.pif)
        self.fileManipulator.writePifToFile(self.pif)
        result = []
        for p in self.pif.getPIF():
            result.append(str(p[0]))
        print("PIF", result)
        print('Symbol Table: \n', self.symbolTable)
        self.fileManipulator.writeSymbolTableToFile(self.symbolTable)