import tkinter
import tkinter.messagebox
import random
import sqlite3
from datetime import datetime
from methods import Methods

class Encode:
      def toUpper(self, in_text):
            return in_text.upper()

      def code(self, in_text, combination):
            out_text = ""
            for ch in in_text:
                  if ch in combination:
                        out_text = out_text + combination[ch]
                  else:
                        out_text = out_text + ch
            return out_text

      def getText(self):
            return input()
