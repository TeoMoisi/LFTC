from pip._vendor.distlib.compat import raw_input

import Grammar


class FiniteAutomata:

    epsilon = 'E'

    def __init__(self, Q, E, S, q0, F):
        self.Q = Q #states
        self.E = E #alphabet
        self.q0 = q0 #initial state
        self.F = F #final state
        self.S = S #transitions

    def __str__(self):
        return 'Q = { ' + ', '.join(self.Q) + ' }\n' \
               + 'E = { ' + ', '.join(self.E) + ' }\n' \
               + 'F = { ' + ', '.join(self.F) + ' }\n' \
               + 'S = { ' + ', '.join([' -> '.join([str(part) for part in trans]) for trans in self.S]) + ' }\n' \
               + 'q0 = ' + str(self.q0) + '\n'

    @staticmethod
    def readConsoleLine(str):
        elements = []
        elem = raw_input(str)
        while elem != '':
            elements.append(elem)
            elem = raw_input(str)
        return elements

    def isState(self, val):
        return val in self.Q

    def printTransitions(self):
        for trans in self.S:
            print(trans)

    @classmethod
    def getFAFromFile(self, filename):
        with open(filename, mode='r') as f:
            Q = f.readline().strip().split(' ')
            E = f.readline().strip().split(' ')
            q0 = f.readline().strip()
            F = f.readline().strip().split(' ')
            S = []
            for line in f:
                s, d, a = line.strip().split(' ')
                S.append(((s, d), a))
        return FiniteAutomata(Q, E, S, q0, F)

    @staticmethod
    def getFAFromConsole():
        print('Enter an empty string when you are done: ')
        Q = FiniteAutomata.readConsoleLine("Q: ")
        E = FiniteAutomata.readConsoleLine("E: ")
        q0 = raw_input('Initial state q0: ')
        F = FiniteAutomata.readConsoleLine("F: ")
        S = FiniteAutomata.readTransitions("S: ")

        return FiniteAutomata(Q, E, S, q0, F)

    @staticmethod
    def readTransitions(str):
        transitions = []

        triple = raw_input(str)
        while triple != '':
            triple = triple.strip().split(' ')
            transitions.append(((triple[0], triple[1]), triple[2]))
            triple = raw_input(str)

        return transitions

    @staticmethod
    def convertRGtoFA(rg):
        rg.N.append('K')
        Q = rg.N
        E = rg.E
        q0 = rg.S
        F = list()
        F.append('K')
        S = []

        for production in rg.P:
            secondState = 'K'
            firstState, rhs = production
            if rhs[0] == FiniteAutomata.epsilon:
                if firstState == q0.strip():
                    F.append(firstState)
                #continue

            symbol = rhs[0]

            if len(rhs) == 2:
                secondState = rhs[1]

            S.append(((firstState, symbol), secondState))

        return FiniteAutomata(Q, E, S, q0, F)

class FAMenu(object):
    def __init__(self, finiteAutomata):
        self.finiteAutomata = finiteAutomata

    def go(self):
        print(self.menu())
        choice = raw_input('Choice: ')
        while choice != '7':
            if choice == '1':
                print('States:')
                print('Q = { ' + ', '.join(self.finiteAutomata.Q) + ' }\n')
            elif choice == '2':
                print('Alphabet:')
                print('E = { ' + ', '.join(self.finiteAutomata.E) + ' }\n')
            elif choice == '3':
                print('Transitions set:')
                print(self.finiteAutomata.S)
            elif choice == '4':
                print(self.finiteAutomata.q0)
            elif choice == '5':
                print(self.finiteAutomata.__str__())
            elif choice == '6':
                print('F = { ' + ', '.join(self.finiteAutomata.F) + ' }\n')
            print ('-' * 20)
            choice = raw_input('Choice: ')

    def menu(self):
        return ''.join([
            '1. States\n',
            '2. Alphabet\n',
            '3. Transitions\n',
            '4. Initial state\n',
            '5. Print the FA\n',
            '6. Print the set of the final states\n',
            '7. Exit\n'
        ])

def main():
    #fa = FiniteAutomata.getFAFromConsole()
    g = Grammar.Grammar.getGrammarFromFile('grammar.txt')
    fa = FiniteAutomata.convertRGtoFA(g)
    #fa = FiniteAutomata.getFAFromFile('finiteAutomata.txt')
    fam = FAMenu(fa)
    fam.go()


if __name__ == "__main__":
    main()

