from tkinter import *
import sqlite3 as sql
from tkinter import messagebox
import entrymenu

class login:
   def __init__(self):
       self.ws = Tk()
       self.Tk_Width = 350
       self.Tk_Height = 150
       self.x_Left = int(self.ws.winfo_screenwidth()/2 - self.Tk_Width/2)
       self.y_Top = int(self.ws.winfo_screenheight()/2 - self.Tk_Height/2)
       self.ws.geometry("+{}+{}".format(self.x_Left, self.y_Top))
       self.ws.title('Login')
       self.ws.config(bg='#0B5A81')
       self.f = ('Times', 14)

       self.left_frame = Frame(
                       self.ws, 
                       bd=2, 
                       bg='#CCCCCC',   
                       relief=SOLID, 
                       padx=10, 
                       pady=10
                     )

       self.bg = PhotoImage(file = "logsym.png")
       self.bg1=PhotoImage(file="insym.png")
       self.loglabel=Label(self.ws)
       
       Label(
                   self.left_frame, 
                   text="Enter Email", 
                   bg='#CCCCCC',
                   font=self.f).grid(row=0, column=0, sticky=W, pady=10)

       Label(
           self.left_frame, 
            text="Enter Password", 
            bg='#CCCCCC',
           font=self.f
          ).grid(row=1, column=0, pady=10)

       self.email_tf = Entry(
             self. left_frame, 
             font=self.f
                            )
       self.pwd_tf = Entry(
               self. left_frame, 
                font=self.f,
                show='*'
                         )
       self. login_btn = Button(
               self.left_frame,
                 width=40,
                 height=40,
                 bg='#CCCCCC',
                 font=self.f,     
                cursor='hand2',
                image=self.bg1,
                command=self.checklogin
               ).grid(row=4,column=0,pady=10, columnspan=2)

       self.email_tf.grid(row=0, column=1, pady=10, padx=20)
       self.pwd_tf.grid(row=1, column=1, pady=10, padx=20)
       self.left_frame.pack()
   def run(self):
           self.ws.mainloop()

   def checklogin(self):
       un=self.email_tf.get()
       
       ps=self.pwd_tf.get()
       #messagebox.showinfo('confirmation',ps)
       
       con = sql.connect("BloodDetails.db")
       cur = con.cursor()
       #statement = "SELECT Email from Register WHERE Email='"+un+"' AND Password = '{ps}';"
       statement = "SELECT Email from Employee WHERE Email='"+un+"' AND Password = '"+ps+"';"
       cur.execute(statement)
       if cur.fetchone():
          
           messagebox.showinfo('confirmation', 'Login Successful')
           self.ws.destroy()
           e=entrymenu.entrymenu()
           e.run()
       else:
           messagebox.showinfo('confirmation', 'Login UnSuccessful')

       
