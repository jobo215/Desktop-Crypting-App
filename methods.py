import tkinter
import tkinter.messagebox
import random
import sqlite3
from datetime import datetime

class Methods():
      def dictFromText(self, text):
            combination = {}
            j = 0
            keys = []
            values = []
            for i in text:
                  if j % 2 == 0:
                        keys.append(i)
                  else:
                        values.append(i)
                  j = j + 1
            for i in range(len(keys)):
                  combination[keys[i]] = values[i]
            return combination
