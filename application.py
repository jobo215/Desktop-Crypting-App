import tkinter
import tkinter.messagebox
import random
import sqlite3
from datetime import datetime
from combination import Combination
from encoder import EncodeR
from methods import Methods
from decode import Decode

class Application:

      def loginForm(self):
            app = tkinter.Tk()
            app.title("LOGIN")
            app.resizable(False, False)
            lb_user = tkinter.Label(app, text = "USERNAME ")
            lb_user.grid(row = 0, column = 0, padx = 3, pady = 3)
            ent_user = tkinter.Entry(app)
            ent_user.grid(row = 0, column = 1, padx = 3, pady = 3)
            lb_pass = tkinter.Label(app, text = "PASSWORD ")
            lb_pass.grid(row = 1, column = 0, padx = 3, pady = 3)
            ent_pass = tkinter.Entry(app, show = '*')
            ent_pass.grid(row = 1, column = 1, padx = 3, pady = 3)
            ent_pass.bind("<Return>", (lambda event: self.log(ent_user.get(), ent_pass.get(), app)))
            bt_log = tkinter.Button(app, text = "LOGIN", command = lambda: self.log(ent_user.get(), ent_pass.get(), app))
            bt_log.grid(row = 2, column = 0, pady = 3)

      def mainForm(self):
            app = tkinter.Tk()
            app.title("MAIN FORM")
            app.resizable(False, False)
            bt_encode = tkinter.Button(app, text = "ENCODE", command = lambda: self.encode(app, False), width = 30)
            bt_encode.grid(row = 0, column = 0)
            bt_decode = tkinter.Button(app, text = "DECODE", command = lambda: self.decode(app, False), width = 30)
            bt_decode.grid(row = 1, column = 0)

      def adminMain(self):
            app = tkinter.Tk()
            app.title("ADMIN MAIN FORM")
            app.resizable(False, False)
            bt_encode = tkinter.Button(app, text = "ENCODE", command = lambda: self.encode(app, True), width = 30)
            bt_encode.grid(row = 0, column = 0)
            bt_decode = tkinter.Button(app, text = "DECODE", command = lambda: self.decode(app, True), width = 30)
            bt_decode.grid(row = 1, column = 0)
            bt_add = tkinter.Button(app, text = "ADD NEW COMBINATION", command = lambda: self.addNew(app), width = 30)
            bt_add.grid(row = 2, column = 0)
            bt_new = tkinter.Button(app, text = "ADD NEW PERSON", command = lambda: self.newP(app), width = 30)
            bt_new.grid(row = 3, column = 0)

      def newP(self, prev_app):
            prev_app.destroy()
            app = tkinter.Tk()
            app.title("NEW PERSON")
            lb_user = tkinter.Label(app, text = "USERNAME ")
            lb_user.grid(row = 0, column = 0)
            lb_pass = tkinter.Label(app, text = "PASSWORD ")
            lb_pass.grid(row = 1, column = 0)
            ent_user = tkinter.Entry(app)
            ent_user.grid(row = 0, column = 1, pady = 1)
            ent_pass = tkinter.Entry(app)
            ent_pass.grid(row = 1, column = 1, pady = 1)
            bt_add = tkinter.Button(app, text = "ADD", command = lambda: self.doAdd(ent_user.get(), ent_pass.get(), app))
            bt_add.grid(row = 1, column = 2)

      def doAdd(self, username, password, prev_app):
            if username == "" or password == "":
                  tkinter.messagebox.showwarning("ERROR", "EMPTY USERNAME OR PASSWORD")
            else:
                  try:
                        conn = sqlite3.connect('combination.db')
                        cursor = conn.cursor()
                        cursor.execute('SELECT * FROM users')
                        rows = cursor.fetchall()
                        users = self.usersList(rows)
                        if username in users:
                              tkinter.messagebox.showinfo("ERROR", "USERNAME ALREADY EXSISTS")
                        else:
                              cursor.execute('INSERT INTO users VALUES (?, ?)', (username, password))
                              conn.commit()
                              tkinter.messagebox.showinfo("ADDING PERSON","PERSON SUCCESSFULY ADDED")
                              prev_app.destroy()
                              self.adminMain()
                  except Exception as e:
                        raise e

      def usersList(self, rows):
            usersList = [x[0] for x in rows]
            return usersList

      def addNew(self, prev_app):
            prev_app.destroy()
            app = tkinter.Tk()
            app.title("ADD NEW COMBINATION")
            app.resizable(False, False)
            bt_add = tkinter.Button(app, text = "ADD", command = lambda: self.add(app), width = 30)
            bt_add.grid(row = 0, column = 0)

      def add(self, prev_app):
            a = Combination()
            tkinter.messagebox.showinfo("ADDED", "SUCCESSFULY ADDED TO DATABASE")
            prev_app.destroy()
            self.adminMain()

      
      def decode(self, prev_app, value):
            prev_app.destroy()
            app = tkinter.Tk()
            app.title("DECODE")
            app.resizable(False, False)
            lb_e = tkinter.Label(app, text = "ENTER YOUR TEXT HERE --->")
            lb_e.grid(row = 0, column = 0)
            tf = tkinter.Text(app, height = 10, width = 30)
            tf.grid(row = 0, column = 1, padx = 3, pady = 3)
            lb_o = tkinter.Label(app, text = "YOUR OUTPUT ------>")
            lb_o.grid(row = 1, column = 0)
            tf_e = tkinter.Text(app, height=10, width=30)
            tf_e.grid(row = 1, column = 1)
            bt_e = tkinter.Button(app, text = "DO IT!", command = lambda: self.doDecode(tf_e, tf.get("1.0", "end")))
            bt_e.grid(row = 3, column = 0)
            bt_c = tkinter.Button(app, text = "CLEAR", command = lambda: self.clear(tf_e))
            bt_c.grid(row = 3, column = 1)
            bt_b = tkinter.Button(app, text = "MAIN MENU", command = lambda: self.backToMain(app, value))
            bt_b.grid(row = 3, column = 2)

      def backToMain(self, app, value):
            app.destroy()
            if value is True:
                  self.adminMain()
            else:
                  self.mainForm()

      def doDecode(self, tf_e, text):
            try:
                  d = Decode(text)
                  tf_e.insert(tkinter.END, d.getMessage())
            except TypeError:
                  tkinter.messagebox.showwarning("ERROR", "THERE ARE NO TEXT")

      def encode(self, prev_app, value):
            prev_app.destroy()
            app = tkinter.Tk()
            app.title("ENCODE")
            app.resizable(False, False)
            lb_e = tkinter.Label(app, text = "ENTER YOUR TEXT HERE --->")
            lb_e.grid(row = 0, column = 0)
            tf = tkinter.Text(app, height = 10, width = 30)
            tf.grid(row = 0, column = 1, padx = 3, pady = 3)
            lb_o = tkinter.Label(app, text = "YOUR OUTPUT ------>")
            lb_o.grid(row = 1, column = 0)
            tf_e = tkinter.Text(app, height = 10, width = 30)
            tf_e.grid(row = 1, column = 1)
            bt_e = tkinter.Button(app, text = "DO IT!", command = lambda: self.doEncode(tf_e, tf.get("1.0", "end")))
            bt_e.grid(row = 3, column = 0)
            bt_c = tkinter.Button(app, text = "CLEAR", command = lambda: self.clear(tf_e))
            bt_c.grid(row = 3, column = 1)
            bt_b = tkinter.Button(app, text = "MAIN MENU", command = lambda: self.backToMain(app, value))
            bt_b.grid(row = 3, column = 2)
            
      
      def clear(self, tf_e):
            clear = "new text"
            tf_e.delete('1.0', tkinter.END)

      def doEncode(self, tf_e, text):
            e = EncodeR(text)
            tf_e.insert(tkinter.END, e.getOutText())
      
      def log(self, username, password, app):
            try:
                  conn = sqlite3.connect('combination.db')
                  cursor = conn.cursor()
                  cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
                  rows = cursor.fetchall()
                  if not rows:
                        tkinter.messagebox.showwarning("ERROR", "WRONG USERNAME OR PASSWORD")
                  else:
                        r = rows[0]
                        r1 = r[0]
                        if(r1 == 'admin'):
                              self.adminMain()
                        else:
                              self.mainForm()
                        app.destroy()
            except sqlite3.Error as e:
                  raise e

      def __init__(self):
            self.loginForm()
