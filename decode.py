import tkinter
import tkinter.messagebox
import random
import sqlite3
from datetime import datetime
from methods import Methods

class Decode:

      def __init__(self, text):
            key, indicator = self.getKey(text)
            message = self.delKey(text, indicator + 1)
            combination = self.getComb(key)
            self.encoded_message = self.getText(combination, message)
            

      def getComb(self, key):
            try:
                  conn = sqlite3.connect('combination.db')
                  cursor = conn.cursor()
                  cursor.execute('SELECT * FROM comb WHERE key = ?', (key, ))
                  rows = cursor.fetchall()
                  row = list(rows[0])
                  text_combination = row[1]
                  m = Methods()
                  combination = m.dictFromText(text_combination)
                  return combination

            except Exception as e:
                  raise e

      def getKey(self, text):
            key = ""
            indicator = 0
            for i in text:
                  if(i == " "):
                        return key, indicator
                  else:
                        key = key + i
                        indicator = indicator + 1

      def getMessage(self):
            return self.encoded_message

      def delKey(self, text, indicator):
            return text[indicator: ]

      def getChar(self, ch, combination):
            if ch == " ":
                  return " "
            else:
              for key, value in combination.items():
                        if value == ch:
                              return str(key)
                  

      def getText(self, combination, message):
            encoded = ""
            for ch in message:
                  if(self.getChar(ch, combination) is None):
                        continue
                  else:
                        encoded = encoded + self.getChar(ch, combination)
            return encoded
