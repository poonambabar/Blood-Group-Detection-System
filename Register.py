from datetime import date
import sqlite3 as sql
from tkinter import *
from tkinter import messagebox,filedialog
import Detection
import re



class Register:
    global fname
    def __init__(self):
        
        self.ws = Tk()
        self.ws.title('Register')
        self.ws.config(bg='#0B5A81')

        self.f= ('Times', 14)
        self.var = StringVar()
        self.var1 = StringVar()
        self.var.set('male')
        self.var1.set('Yes')

        self.currentdate=date.today()
        self.option = []
        self.variable = StringVar()

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
            text="Enter Name", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=0, column=0, sticky=W, pady=10)

        Label(
            right_frame, 
            text="Enter Email", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=1, column=0, sticky=W, pady=10)

        Label(
            right_frame, 
            text="Contact Number", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=2, column=0, sticky=W, pady=10)

        Label(
            right_frame, 
            text="Select Gender", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=3, column=0, sticky=W, pady=10)

        Label(
              right_frame,
              text="Enter Date",
              bg='#CCCCCC',
              font=self.f
              ).grid(row=4, column=0, sticky=W, pady=10)



        Label(
            right_frame, 
            text="Select State", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=5, column=0, sticky=W, pady=10)

        Label(
              right_frame,
              text="Select Blood Sample",
              bg='#CCCCCC',
              font=self.f
              ).grid(row=7, column=0, sticky=W, pady=10)

        Label(
              right_frame,
              text="Donar",
              bg='#CCCCCC',
              font=self.f
              ).grid(row=6, column=0, sticky=W, pady=10)



        gender_frame = LabelFrame(
            right_frame,
            bg='#CCCCCC',
            padx=10, 
            pady=10,
            )


        self.register_name = Entry(
            right_frame, 
            font=self.f
            )

        self.register_email = Entry(
            right_frame, 
            font=self.f
            )

        self.register_mobile = Entry(
            right_frame, 
            font=self.f
            )


        self.male_rb = Radiobutton(
            gender_frame, 
            text='Male',
            bg='#CCCCCC',
            variable=self.var,
            value='male',
            font=('Times', 10),
            
        )

        self.female_rb = Radiobutton(
            gender_frame,
            text='female',
            bg='#CCCCCC',
            variable=self.var,
            value='self.female',
            font=('Times', 10),
          
        )

        self.others_rb = Radiobutton(
            gender_frame,
            text='Others',
            bg='#CCCCCC',
            variable=self.var,
            value='others',
            font=('Times', 10)
           
        )

        self.option=["Maharashtra","Punjab","Karnataka","Gujarat","Rajasthan","UP","MP","Delhi"]

        self.register_country = OptionMenu(
            right_frame, 
            self.variable, 
            *self.option)

        self.register_country.config(
           width=15, 
           font=('Times', 12)
        )

        self.dates=Entry(
            right_frame,
            font=self.f    
            )
        self.dates.insert(0,self.currentdate)
        #dates.state=DISABLED    

        #image=self.filedialog.askopenself.filename()


        donar_frame = LabelFrame(
            right_frame,
            bg='#CCCCCC',
            padx=10, 
            pady=10,
            )

        self.donate_yes = Radiobutton(
            donar_frame, 
            text='Yes',
            bg='#CCCCCC',
            variable=self.var1,
            value='Yes',
            font=('Times', 10),
            
        )

        self.donate_no = Radiobutton(
            donar_frame,
            text='NO',
            bg='#CCCCCC',
            variable=self.var1,
            value='No',
            font=('Times', 10),
          
        )


        self.register_btn = Button(
            right_frame, 
            width=15, 
            text='Select Slide', 
            font=self.f, 
            relief=SOLID,
            cursor='hand2',
            command=self.insert_record
        )

        


        self.register_name.grid(row=0, column=1, pady=10, padx=20)
        self.register_email.grid(row=1, column=1, pady=10, padx=20) 
        self.register_mobile.grid(row=2, column=1, pady=10, padx=20)
        self.dates.grid(row=4, column=1, pady=10, padx=20)
        self.register_country.grid(row=5, column=1, pady=10, padx=20)
       



        self.register_btn.grid(row=7, column=1, pady=10, padx=20)
        right_frame.pack()

        gender_frame.grid(row=3, column=1, pady=10, padx=20)
        self.male_rb.pack(expand=True, side=LEFT)
        self.female_rb.pack(expand=True, side=LEFT)
        self.others_rb.pack(expand=True, side=LEFT)

        donar_frame.grid(row=6,column=1,padx=10,pady=10)
        self.donate_yes.pack(expand=True, side=LEFT)
        self.donate_no.pack(expand=True, side=LEFT)

        self.currentdate=date.today()
        self.filenames=""

    def check(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        # pass the regular expression
        # and the string into the fullmatch() method
        warn = ""
        if (re.fullmatch(regex, email)):
            
            warn = "Valid Email"
            print(warn)
            return 1

        else:
            
            return 0
        
       
    def isValid(self,s):

         Pattern = re.compile("[7-9][0-9]{9}")
        
         return Pattern.match(s)


    def insert_record(self):
            check_counter=0
            warn = ""
            if self.register_name.get() == "":
                warn = "Name can't be empty"
            else:
                check_counter += 1
                
        
            if self.register_email.get() == "":
                warn = "Email can't be empty"
            else:
                check_counter += 1

            con = sql.connect("BloodDetails.db")
            cur = con.cursor()

            statement = "SELECT Email from Register WHERE Email='" +self.register_email.get()  + "';"
            cur.execute(statement)
            if cur.fetchone():

                messagebox.showinfo('confirmation', 'Email id already exists')

                mainwindow = entrymenu.entrymenu()
                
                self.ws.destroy()
                mainwindow.run()
                

            #else:
                #messagebox.showinfo('confirmation', 'New patient proceed')
               

            if self.register_mobile.get() == "":
                warn = "Contact can't be empty"
            else:
                check_counter += 1
              
            if self.var.get() == "":
                warn = "Select Gender"
            else:
                check_counter += 1
               
                   
            if self.dates.get() == "":
                warn = "Date"
            else:
                check_counter += 1   
                
         
            if self.variable.get() == "":
                warn = "Select State"
            else:
                check_counter += 1
                
            #if self.filenames =="":
              # warn="Blood Sample not Selected"
            #else:
               #check_counter=check_counter
               
              # messagebox.showinfo("heloo",self.var1.get())  
            if check_counter == 6:
               self.detect_open()
            else:
               messagebox.showerror('Error', warn)



    def run(self):
        self.ws.mainloop()
        
    def detect_open(self):
       
        global pname
        global em

        global mob
        global gen
        global dt
        global sra
        global dn
        pname=self.register_name.get()
        em=self.register_email.get()

        mob=self.register_mobile.get()
        gen=self.var.get()
        sra=self.variable.get()
        dt=dt=self.currentdate
        dn=self.var1.get()

        em1 = self.check(self.register_email.get())

        if em1 == 0 :
         
             warn = "Invalid Email"
             messagebox.showerror('Error', warn)
           
             
        elif (self.isValid(mob) == None) :
           
             warn1 = "Invalid Mobile Number"
             messagebox.showerror('Error', warn1)
             
        else:

            self.ws.destroy()
            mainwindow =Detection.Detection(pname,em,mob,gen,dt,sra,dn)
            mainwindow.run()



#r=Register()
#r.run()
