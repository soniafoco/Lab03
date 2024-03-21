class Dictionary:
    def __init__(self, language):
        self._dict = []
        self._language = language

    def loadDictionary(self,path):
        file = open(path, "r", encoding="utf-8")
        riga = file.readline()
        while riga != "":
            self._dict.append(riga.strip())
            riga = file.readline()
        file.close()

    def printAll(self):
        pass

    def contains(self, word):
        return self._dict.__contains__(word)

    def dict(self):
        return self._dict