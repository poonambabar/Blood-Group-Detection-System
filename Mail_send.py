from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import entrymenu;
import os
from tkinter import *
from tkinter import messagebox,filedialog


class Mail_send:
    def __init__(self,ml,ms):
        self.ws = Tk()
        self.ws.title('Email')
        self.ws.config(bg='#0B5A81')
        self.Text_Area=StringVar()
        self.f= ('Times', 14)
        self.var=StringVar()
        self.var.set(ml)
        self.var1=StringVar()
        self.var1.set(ms)
        
        sub="Blood Group Detection Report"
        To="poonambabar0409@gmail.com"
        
        self.var2=StringVar()
        self.var2.set(sub)
        
        self.var3=StringVar()
        self.var3.set(To)
       

        right_frame = Frame(
            self.ws, 
            bd=2, 
            bg='#CCCCCC',
            relief=SOLID, 
            padx=20, 
            pady=20
            )
        
        Label(
            right_frame, 
            text="Our Mail ID", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=0, column=0, sticky=W, pady=10)

        Label(
            right_frame, 
            text="Password", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=1, column=0, sticky=W, pady=10)
        
        Label(
            right_frame, 
            text="To", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=2, column=0, sticky=W, pady=10)
            
        Label(
            right_frame, 
            text="Subject", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=3, column=0, sticky=W, pady=10)  
        
        Label(
            right_frame, 
            text="Message", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=4, column=0, sticky=W, pady=10)
        
       
      # Label(
           # right_frame, 
           # text="Attachment", 
           # bg='#CCCCCC',
           # font=self.f
           # ).grid(row=5, column=0, sticky=W, pady=10)
       
        
        self.mail = Entry(
            right_frame, 
            font=self.f,
            textvariable=self.var3,
           
            )

        self.passs = Entry(
            right_frame, 
            font=self.f,
            show='*'
            )
        
        self.too = Entry(
            
            right_frame, 
            textvariable=self.var,
            font=self.f            
            )
        
        self.sub = Entry(
            right_frame, 
            textvariable=self.var2,
            font=self.f,
            
            )
        self.message = Entry(
            right_frame, 
            textvariable=self.var1,
            font=self.f,
            
            )
        self.att_btn = Button(
            right_frame, 
            width=15, 
            text='Attachment', 
            font=self.f, 
            relief=SOLID,
            cursor='hand2',
            command=self.open_file
        )

        self.send_btn = Button(
            right_frame, 
            width=15, 
            text='Send', 
            font=self.f, 
            relief=SOLID,
            cursor='hand2',
            command=self.send_msg
        )
        self.mail.grid(row=0, column=1, pady=10, padx=20)
        self.passs.grid(row=1, column=1, pady=10, padx=20) 
        self.too.grid(row=2, column=1, pady=10, padx=20) 
        self.sub.grid(row=3, column=1, pady=10, padx=20)
        self.message.grid(row=4, column=1, pady=10, padx=20)
        #self.att_btn.grid(row=5, column=1, pady=10, padx=20)
        self.send_btn.grid(row=6, column=1, pady=10, padx=20)
        right_frame.pack()

        
        
    
    def open_file(self):            
            self.filenames = filedialog.askopenfilename()  
            
    def send_msg(self):
        subject=self.sub.get()
        body=self.message.get()
        msg="Subject:{}\n\n{}".format(subject, body)
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login(self.mail.get(),self.passs.get())
        smtp.sendmail(self.mail.get(),self.too.get(),msg)
    
    def run(self):
        e=entrymenu.entrymenu()
        e.run()
    
    
    def run(self):
            self.ws.mainloop()
            e=entrymenu.entrymenu()
            e.run()
            
  
        
#M=Mail_send()
#M.run()
        
        
        
        