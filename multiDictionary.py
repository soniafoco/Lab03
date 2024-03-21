import richWord as rw
import time
import dictionary

class MultiDictionary:

    def __init__(self):
        self.dizionari = {}

    def printDic(self, language):
        dict = self.dizionari.get(language).dict() #singolo dizionario

        print(f"Dizionario in lingua {language}")
        for dict_word in dict:
            print(dict_word)

    def searchWord(self, words, language):
        dict = self.dizionari.get(language) #singolo dizionario
        words = words.split(" ")

        start = time.time()

        list = []
        for word in words:
            richW = rw.RichWord(word)
            list.append(richW)
            if dict.contains(word.lower())==True:
                richW.setCorretta(True)
            else:
                richW.setCorretta(False)

        return list, time.time() - start

    def searchWordLinear(self, words, language):
        dict = self.dizionari.get(language).dict()  # singolo dizionario
        words = words.split(" ")

        start = time.time()

        list = []
        for word in words:
            richW = rw.RichWord(word)
            list.append(richW)
            found = False
            for dict_word in dict:
                if word.lower()==dict_word:
                    found = True
            richW.setCorretta(found)

        return list, time.time() - start

    def searchWordDichotomic(self, words, language):
        dict = self.dizionari.get(language).dict()  # singolo dizionario
        words = words.split(" ")

        start = time.time()

        list = []
        for word in words:
            richW = rw.RichWord(word)
            list.append(richW)
            found = False
            n = int(len(dict)/2)
            if dict[n-1] == word:
                found = True
            else:
                if dict[n-1].__lt__(word) == True: #dict[n-1]<word
                    for i in range(n-1, len(dict)):
                        if dict[i] == word:
                            found = True
                else:
                    for i in range(0, n):
                        if dict[i] == word:
                            found = True
            richW.setCorretta(found)

        return list, time.time() - start

    def addDictionary(self, language, dict):
        if language not in self.dizionari.keys():
            self.dizionari[language] = dict

