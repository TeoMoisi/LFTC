
class ProgramInternalForm:
    def __init__(self):
        self._pifContent = []

    def __str__(self):
        return str(self._pifContent)

    def add(self, code, id):
        self._pifContent.append((code, id))

    def getPIF(self):
        return self._pifContent