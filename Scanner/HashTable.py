import math
class HashTable:
    def __init__(self):
        self.dict = {}
        self.size = 1001
        for i in range(self.size):
            self.dict[i] = []

    def __str__(self):
        return str(self.dict)

    def hashingFunction(self, value):
        sumOfCharsInt = 0

        for elementChar in value:
            sumOfCharsInt += ord(elementChar)
        return sumOfCharsInt % self.size

    def find(self, token):
        key = self.hashingFunction(token)
        if token in self.dict[key]:
            return key
        return None

    def add(self, value):
        token = self.find(value)
        if token:
            return token

        key = self.hashingFunction(value)
        if self.dict[key]:
            self.dict[key].append(value)
        else:
            self.dict[key] = []
            self.dict[key].append(value)
        return key, len(self.dict[key]) - 1

    def getHashTable(self):
        return self.dict