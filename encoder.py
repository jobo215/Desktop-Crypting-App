import tkinter
import tkinter.messagebox
import random
import sqlite3
from datetime import datetime
from methods import Methods
from encode import Encode

class EncodeR:

      def __init__(self, text):
            key, combination = self.getFromDB()
            e = Encode()
            text = e.toUpper(text)
            self.out_text = e.code(text, combination)
            self.out_text = key + " " + self.out_text

      def getOutText(self):
            return self.out_text

      def getFromDB(self):
            try:
                  conn = sqlite3.connect('combination.db')
                  cursor = conn.cursor()
                  cursor.execute('SELECT * FROM comb ORDER BY RANDOM() LIMIT 1')
                  rows = cursor.fetchall()
                  row = rows[0]
                  key = row[0]
                  text = row[1]
                  m = Methods()
                  return key, m.dictFromText(text)
            except sqlite3.Error as e:
                  raise e
