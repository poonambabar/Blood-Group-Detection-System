
import tkinter as tk
from tkinter import *
import Register
import employee
import Detection
import Mail_send
import Sms
import Display_list
import entrymenu
#import sq


class entrymenu:
    def __init__(self):
      
 
        self.entrywindow=tk.Tk()
  
#getting screen width and height of display
        self.width= self.entrywindow.winfo_screenwidth() 
        self.height= self.entrywindow.winfo_screenheight()
#setting tkinter window size
        self.entrywindow.geometry("%dx%d" % (self.width, self.height))
        self.entrywindow.title("BloodDetection")
        #self.bg = PhotoImage(file = "menubg.png")
        #self.label = tk.Label(self.entrywindow,width=1000,height=1000)
        #self.label.pack()
        self.my_menubar=Menu(self.entrywindow,fg='white')
       
        self.file_menu= Menu(self.my_menubar,tearoff=0)
            
        self.my_menubar.add_cascade(label="New", menu=self.file_menu)
        self.file_menu.add_command(label="Employee",command=self.emp_open)
        self.file_menu.add_command(label="Patient",command=self.regi_open)
        self.file_menu.add_command(label="Donor",command=self.regi_list)
        
        #self.detect_menu= Menu(self.my_menubar,tearoff=0)
        
        #self.my_menubar.add_cascade(label="Detection", menu=self.detect_menu)
        #self.detect_menu.add_command(label="Detection",command=self.detect_open)
       
        """
        self.communicate_menu= Menu(self.my_menubar,tearoff=0)
        self.my_menubar.add_cascade(label="Communication", menu=self.communicate_menu)
        self.communicate_menu.add_command(label="Message",command=self.sms_open)
        self.communicate_menu.add_command(label="Email",command=self.mail_open)
          
        """
        self.exit_menu= Menu(self.my_menubar,tearoff=0)
        self.my_menubar.add_cascade(label="Exit", menu=self.exit_menu)
        self.exit_menu.add_command(label="Exit",command=self.close)
        self.entrywindow.config(menu=self.my_menubar)  
        
        

        
      
    def run(self):  
       self.entrywindow.mainloop()



    def regi_open(self):
        self.entrywindow.destroy();
        mainwindow = Register.Register()
        mainwindow.run()
        
    def emp_open(self):
        self.entrywindow.destroy();
        mainwindow = employee.Employee()
        mainwindow.run()
    def detect_open(self):
        mainwindow =Detection.Detection()
        mainwindow.run()
    def mail_open(self):
        mainwindow =Mail_send.Mail_send()
        mainwindow.run()    
    def sms_open(self):
        mainwindow =Sms.Sms()
        mainwindow.run()

    def regi_list(self):
        #self.entrywindow.destroy();
        mainwindow = Display_list.Display_list()
        mainwindow.run()
        # sq.root()

    def close(self):
        self.entrywindow.destroy()
        
        
#e=entrymenu()
#e.run()