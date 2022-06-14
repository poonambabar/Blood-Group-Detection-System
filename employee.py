
from datetime import date
import sqlite3
from tkinter import *
from tkinter import messagebox,filedialog
import re
import entrymenu
import phonenumbers
import sqlite3 as sql


class Employee:
    def __init__(self):
        self.ws = Tk()
        self.ws.title('Employee')
        self.ws.config(bg='#0B5A81')

        self.f= ('Times', 14)
        self.var = StringVar()
        self.var1 = StringVar()
        self.var.set('male')
        self.var1.set('Yes')

        #self.currentdate=date.today()
        self.option = []
        self.variable = StringVar()
#world = open('countries.txt', 'r')
#self.for country in world:
#    country = country.rstrip('\n')
#    countries.append(country)
#variable.set(countries[22])
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
            text="Select State", 
            bg='#CCCCCC',
            font=self.f
            ).grid(row=4, column=0, sticky=W, pady=10)

        Label(
              right_frame,
              text="Password",
              bg='#CCCCCC',
              font=self.f
              ).grid(row=5, column=0, sticky=W, pady=10)

        Label(
              right_frame,
              text="Confirm Password",
              bg='#CCCCCC',
              font=self.f
              ).grid(row=6, column=0, sticky=W, pady=10)



        gender_frame = LabelFrame(
            right_frame,
            bg='#CCCCCC',
            padx=10, 
            pady=10,
            )

        self.employee_name = Entry(
            right_frame, 
            font=self.f
            )

        self.employee_email = Entry(
            right_frame, 
            font=self.f
            )

        self.employee_mobile = Entry(
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
         
        

        self.option=["Maharashtra",
                     "Punjab",
                     "Karnataka",
                     "Gujarat",
                     "Rajasthan",
                     "UP",
                     "MP",
                     "Delhi"]

        self.employee_country = OptionMenu(
            right_frame,
            self.variable,
            *self.option)

        self.employee_country.config(
           width=15,
           font=('Times', 12)
        )

        self.employee_password = Entry(
            right_frame, 
            font=self.f
            )
        self.employee_cpassword = Entry(
            right_frame, 
            font=self.f
            )

        

        self.register_btn = Button(
            right_frame, 
            width=15, 
            text='Insert', 
            font=self.f, 
            relief=SOLID,
            cursor='hand2',
            command=self.insert_record
        )


        self.employee_name.grid(row=0, column=1, pady=10, padx=20)
        self.employee_email.grid(row=1, column=1, pady=10, padx=20) 
        self.employee_mobile.grid(row=2, column=1, pady=10, padx=20)
        self.employee_country.grid(row=4, column=1, pady=10, padx=20)
        self.employee_password.grid(row=5,column=1, pady=10, padx=20)
        self.employee_cpassword.grid(row=6,column=1, pady=10, padx=20)
        self.register_btn.grid(row=8, column=1, pady=10, padx=20)
        right_frame.pack()
        gender_frame.grid(row=3, column=1, pady=10, padx=20)
        self.male_rb.pack(expand=True, side=LEFT)
        self.female_rb.pack(expand=True, side=LEFT)
        self.others_rb.pack(expand=True, side=LEFT)

    import re

    # Make a regular expression
    # for validating an Email
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    
    def isValid(self,s):

        
        Pattern = re.compile("[7-9][0-9]{9}")
       
        return Pattern.match(s)
        
           

    # Define a function for
    # for validating an Email

    def check(self,email):
        warn=""
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        # pass the regular expression
        # and the string into the fullmatch() method
        if (re.fullmatch(regex, email)):
            warn = "Valid Email"
            print(warn)
            return 1

        else:
            
            return 0
        
        
        
    def insert_record(self):
            check_counter=0
            warn = ""
            if self.employee_name.get() == "":
                warn = "Name can't be empty"
            else:
                check_counter += 1
                #messagebox.showinfo("heloo",self.register_name.get())        
        
            if self.employee_email.get() == "":
                warn = "Email can't be empty"
            else:
                check_counter += 1
                #messagebox.showinfo("heloo",self.register_email.get()) 
                
            con = sql.connect("BloodDetails.db")
            cur = con.cursor()

            statement = "SELECT Email from Register WHERE Email='" +self.employee_email.get()  + "';"
            cur.execute(statement)
            if cur.fetchone():

                 messagebox.showinfo('confirmation', 'Email id already exists')

                 mainwindow = entrymenu.entrymenu()
                 
                 self.ws.destroy()
                 mainwindow.run()    

            if self.employee_mobile.get() == "":
                warn = "Contact can't be empty"
            else:
                check_counter += 1
                #messagebox.showinfo("heloo",self.register_mobile.get())  
    
            if self.var.get() == "":
                warn = "Select Gender"
            else:
                check_counter += 1
                #messagebox.showinfo("heloo",self.var.get())  

            if self.variable.get() == "":
                warn = "Select State"
            else:
                check_counter += 1
                #messagebox.showinfo("heloo",self.variable.get())  
                
            if self.employee_password.get()=="":
                warn = "Password can't be empty"
            else:
                check_counter += 1
                
                  
            if self.employee_cpassword.get()=="":
                warn = "Confirm Password can't be empty"
                
                
            else:
                check_counter += 1    
                
           
                 


            if check_counter == 7:
                
               
                try:
                     con = sqlite3.connect('BloodDetails.db')
                     nm=self.employee_name.get()
                     em=self.employee_email.get()


                     mb=self.employee_mobile.get()
                     gn=self.var.get()
                     st=self.variable.get()
                     ps=self.employee_password.get()
                     cur = con.cursor()
                     insert_stmt = (
                     "insert into Employee(Name,Email,Contact_Number,Gender,State,Password)""values(?,?,?,?,?,?)")
                     data = (nm,em,mb,gn,st,ps)

                     em1 = self.check(self.employee_email.get())
                     
                    
                         
                     if em1 == 0 :
                         warn = "Invalid Email"
                         messagebox.showerror('Error', warn)
                       
                         
                     elif (self.isValid(mb) == None) :
                         warn1 = "Invalid Mobile Number"
                         messagebox.showerror('Error', warn1)
                         
                         

                     else :
                        cur.execute(insert_stmt, data)
                        con.commit()
                        messagebox.showinfo('BloodDetails','Record Save')
                        mainwindow = entrymenu.entrymenu()
                        
                        self.ws.destroy()
                        mainwindow.run()
                except Exception as ep:
                    messagebox.showerror('Error',format(ep)) 
            else:
                    messagebox.showerror('Error', warn)

    def run(self):
        self.ws.mainloop()



#r=Employee()
#r.run()
