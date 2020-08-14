import tkinter
import tkinter.messagebox
import random
import sqlite3
from datetime import datetime

class Combination:
      def __init__(self):
            alphabet = self.addChars()
            newList = self.addChars()
            self.shuffle(newList)
            combination = self.makeDict(alphabet, newList)
            self.key = self.toDB(combination)
            self.c = combination

      def shuffleDict(self, combination):
            keys = list(combination.keys())
            random.shuffle(keys)
            shuffledDict = {}
            for key in keys:
                  shuffledDict.update({key : combination[key]})
            return shuffledDict

      def addChars(self):
            alphabet = []
            for i in range(65, 91):
                  alphabet.append(chr(i))
            for i in range(48, 58):
                  alphabet.append(chr(i))
            return alphabet

      def shuffle(self, newList):
            random.shuffle(newList)

      def makeDict(self, alphabet, newList):
            combination = {}
            for i in range(len(newList)):
                  combination[alphabet[i]] = newList[i]
            combination = self.shuffleDict(combination)
            return combination

      def getKey(self):
            return self.key

      def getComb(self):
            return self.c

      def dictToString(self, combination):
            text = ""
            for key, value in combination.items():
                  text = text + key
                  text = text + value
            return text

      def currentDate(self):
            d = datetime.now()
            return str(d.day) + str(d.month) + str(d.year) + str(d.hour) + str(d.minute) + str(d.second)

      def toDB(self, combination):
            letters = self.dictToString(combination)
            key = self.currentDate()
            try:
                  conn = sqlite3.connect('combination.db')
                  c = conn.cursor()
                  c.execute('INSERT INTO comb VALUES (?, ?)', (key, letters))
                  conn.commit()
            except Exception as e:
                  raise e
            finally:
                  return key
