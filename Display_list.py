from datetime import date
import sqlite3 as sql
from tkinter import *
from tkinter import messagebox,filedialog
import tkinter as tk
import sqlite3
from tkinter import ttk


class Display_list :

    def View(self):
        con1 = sqlite3.connect("BloodDetails.db")
        cur1 = con1.cursor()
        cur1.execute("SELECT name,email,contact_number,bloodgroup FROm register where Donar='Yes'")

        rows = cur1.fetchall()

        for row in rows:
            print(row)

            self.tree.insert("", tk.END, values=row)

        con1.close()

    def __init__(self):

        self.ws = Tk()

        self.tree = ttk.Treeview(self.ws, column=("c1", "c2", "c3", "c4"), show='headings')

        self.tree.column("#1", anchor=tk.CENTER)

        self.tree.heading("#1", text="Name")

        self.tree.column("#2", anchor=tk.CENTER)

        self.tree.heading("#2", text="Email")

        self.tree.column("#3", anchor=tk.CENTER)

        self.tree.heading("#3", text="Contact_Number")
       # self.tree.column("#4", anchor=tk.CENTER)

       # self.tree.heading("#4", text="Gender")

        self.tree.column("#4", anchor=tk.CENTER)

        self.tree.heading("#4", text="Blood Group")

        self.tree.pack()
        self.View()
        #button1 = tk.Button(text="Display data", command=self.View())

        #button1.pack(pady=10)

        #root.mainloop()

    def run(self):
        self.ws.mainloop()