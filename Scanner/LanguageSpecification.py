operators = ['+', '-', '/', '%', '*', '<', '>', '=', '<=', '>=', '==', '!=', '++', '--', ',']
separators = ['[', ']', '{', '}', ';', ':', '(', ')', ' ']
reservedWords = ['array', 'integer', 'string', 'if', 'do', 'else', 'while', 'write', 'read', 'then', 'for',
                 'true', 'false', 'char', 'new', 'const', 'boolean','const', 'begin', 'end']
#operators = ['=']
# separators = [';', ':', '(', ')', ' ']
# reservedWords = ['var', 'integer', 'write']

lexic = operators + separators + reservedWords
codificationTable = {}
codificationTable['identifier'] = 0
codificationTable['constant'] = 1
for i in range(0, len(lexic)):
    codificationTable[lexic[i]] = i + 2