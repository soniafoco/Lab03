import time

import multiDictionary as md
from dictionary import Dictionary

class SpellChecker:

    def __init__(self):
        self.dizionario = None

    def handleSentence(self, txtIn, language):
        self.dizionario = Dictionary(language)
        self.dizionario.loadDictionary("resources/" + language + ".txt")
        multiDizionario = md.MultiDictionary()
        multiDizionario.addDictionary(language, self.dizionario)

        txtIn = replaceChars(txtIn)

        print("______________________________\n" + "Using Contains")
        list_richWords, time = multiDizionario.searchWord(txtIn, language)
        for word in list_richWords:
            if word.corretta() == False:
                print(word.__str__())
        print(time)

        print("______________________________\n" + "Using Linear search")
        list_richWords, time = multiDizionario.searchWordLinear(txtIn, language)
        for word in list_richWords:
            if word.corretta() == False:
                print(word.__str__())
        print(time)

        print("______________________________\n" + "Using Dichotomic search")
        list_richWords, time = multiDizionario.searchWordDichotomic(txtIn, language)
        for word in list_richWords:
            if word.corretta() == False:
                print(word.__str__())
        print(time)

        multiDizionario.printDic(language)

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text



