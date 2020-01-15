from pip._vendor.distlib.compat import raw_input

import FiniteAutomata


class Grammar:
    arrow_symbol = '->'
    epsilon = 'E'

    def __init__(self, N, E, P, S):
        self.N = N #set of non-terminals
        self.E = E #set of terminals
        self.P = P #set of productions
        self.S = S #starting symbol

    def __str__(self):
        print( 'N = { ' + ', '.join(self.N) + ' }\n' \
               + 'E = { ' + ', '.join(self.E) + ' }\n' \
            + self.printAllProdutcions()
               + 'S = ' + str(self.S) + '\n')

    @staticmethod
    def arrow():
        return ' %s ' % Grammar.arrow_symbol

    @staticmethod
    def readTerminalsAndNonTermianls(str):
        elements = []
        elem = raw_input(str)
        while elem != '':
            elements.append(elem)
            elem = raw_input(str)
        return elements

    @staticmethod
    def readProduction():
        productions = []
        prod = raw_input('Production : ')
        while prod != '':
            lhs, rhs = prod.split(Grammar.arrow())
            lhs = lhs.strip()
            rhs = [value.strip() for value in rhs.split('|')]

            for value in rhs:
                productions.append((lhs, value))
            prod = raw_input('Production: ')

        return productions

    @staticmethod
    def getGrammarFromConsole():
        print('Enter an empty string when you are done: ')
        N = Grammar.readTerminalsAndNonTermianls('Non-termials: ')
        E = Grammar.readTerminalsAndNonTermianls('Terminals: ')
        P = Grammar.readProduction()
        S = 'S = S'

        return Grammar(N, E, P, S)

    @classmethod
    def getGrammarFromFile(cls, filename):
        with open(filename, mode='r') as f:
            nonTerminals = f.readline().strip().split(' ')
            terminals = f.readline().strip().split(' ')
            startingSymbol = f.readline()
            productions = []
            for line in f:
                lhs, rhs = line.strip().split(Grammar.arrow())
                lhs = lhs.strip()
                rhs = [value.strip() for value in rhs.split('|')]

                for value in rhs:
                    productions.append((lhs, value))
        return Grammar(nonTerminals, terminals, productions, startingSymbol)

    @staticmethod
    def convertFAtoRG(fa):
        N = fa.Q
        E = fa.E
        S = fa.q0
        P = []

        #if initial state is amogst the final states
        if fa.q0 in fa.F:
            P.append((fa.q0, 'E'))

        for transition in fa.S:
            lhs, secondState = transition
            firstState, symbol = lhs

            P.append((firstState, symbol + secondState))

            if secondState in fa.F:
                P.append((firstState, symbol))

        return Grammar(N, E, P, S)


    def isNonTerminal(self, val):
        return val in self.N

    def isTerminal(self, val):
        return val in self.E

    def isRegular(self):
        isInRhs = {}
        notAllowedInRhs = []

        for prod in self.P:
            lhs, rhs = prod
            hasTerminal = False
            hasNonTerminal = False

            if len(rhs) > 2:
                return False

            for elem in rhs:
                if self.isNonTerminal(elem):
                    isInRhs[elem] = True
                    hasNonTerminal = True
                elif self.isTerminal(elem):
                    if hasNonTerminal:
                        return False
                    hasTerminal = True

                if elem == self.epsilon:
                    notAllowedInRhs.append(lhs)

            if hasNonTerminal and not hasTerminal:
                return False

        for char in notAllowedInRhs:
            if char in isInRhs:
                return False
        return True

    def getNonTerminalProduction(self, nonTerminal):
        if not self.isNonTerminal(nonTerminal):
            raise Exception('Can only show productions for non-terminals')

        productions = self.getProductions()

        result = nonTerminal + self.arrow() + ' '
        for elem in productions[nonTerminal][0:-1]:
            result += elem + '|'
        result += productions[nonTerminal][-1] + '\n'

        return result

    def getProductions(self):
        productionsDict = {}
        for prod in self.P:
            productionsDict[prod[0]] = []

        for prod in self.P:
            productionsDict[prod[0]].append(prod[1])
        return productionsDict

    def printAllProdutcions(self):
        productions = self.getProductions()
        result = "P:\n { "
        for prod in productions.keys():
            result += prod + self.arrow()
            for elem in productions[prod][0:-1]:
                result += elem + '|'
            result += productions[prod][-1] + '\n'
        result += "}\n"

        return result



class GrammarMenu(object):
    def __init__(self, grammar):
        self.grammar = grammar

    def go(self):
        print(self.menu())
        choice = raw_input('Choice: ')
        while choice != '7':
            if choice == '1':
                print('Non-terminals:')
                print('N = { ' + ', '.join(self.grammar.N) + ' }\n')
            elif choice == '2':
                print('Terminals:')
                print('E = { ' + ', '.join(self.grammar.E) + ' }\n')
            elif choice == '3':
                print('Productions set:')
                print(self.grammar.printAllProdutcions())
            elif choice == '4':
                nonTerminal = raw_input('Please give non-terminal: ')
                print(self.grammar.getNonTerminalProduction(nonTerminal))
            elif choice == '5':
                print(self.grammar.isRegular())
            elif choice == '6':
                self.grammar.__str__()
            print ('-' * 20)
            choice = raw_input('Choice: ')

    def menu(self):
        return ''.join([
            '1. Non-terminals\n',
            '2. Terminals\n',
            '3. Productions\n',
            '4. Productions for non-terminal\n',
            '5. Check if grammar is regular.\n',
            '6. Print the grammar.\n'
            '7. Exit\n'
        ])

def main():
    #g = Grammar.getGrammarFromConsole()
    #fa = FiniteAutomata.FiniteAutomata.getFAFromFile('finiteAutomata.txt')
    g = Grammar.getGrammarFromFile('grammar.txt')
    #g = Grammar.convertFAtoRG(fa)
    gm = GrammarMenu(g)
    gm.go()


if __name__ == "__main__":
    main()
