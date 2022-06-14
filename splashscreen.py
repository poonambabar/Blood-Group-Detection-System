
from tkinter import *
import login
# Create object
splash_root = Tk()
   

splash_root.geometry("300x300")
Tk_Width = 350
Tk_Height = 150
x_Left = int(splash_root.winfo_screenwidth()/2 - Tk_Width/2)

y_Top = int(splash_root.winfo_screenheight()/2 - Tk_Height/2)
splash_root.geometry("+{}+{}".format(x_Left, y_Top))
splash_root.title("Blood Group Detection")
bg = PhotoImage(file = "splashscreenlogo.png")
logo_label=Label(splash_root,image=bg)
splash_label = Label(splash_root,text="Blood Group Detection",font=18)
version_label=Label(splash_root,text="Version 1",font=15)
logo_label.pack()
splash_label.pack()
version_label.pack()


# main window function
def main(): 
    # destroy splash window
    splash_root.destroy()
 
    # Execute tkinter
    mainwindow = login.login()
    mainwindow.run()
       
    # Adjust size
    #root.geometry("400x400")
 
# Set Interval
splash_root.after(3000,main)
 
# Execute tkinter
mainloop()