import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox,filedialog
from PIL import Image, ImageFont,ImageTk, ImageOps
import cv2
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import sqlite3
import PIL
import Mail_send
from keras.models import load_model
import cv2
import numpy as np


def tile(filename,  dir_out, d):
    name, ext = os.path.splitext(filename)
    img = Image.open( filename)
    w, h = img.size
    #grid = product(range(0, h - h % d, d), range(0, w - w % d, d))
    count = 1
    i = 0
    j = 0
    for k in range(0, 3):
        box = (j, i, j + d, i + d)
        j = j + d

        out = os.path.join(dir_out, str(count) + ".jpg")
        img.crop(box).save(out)
        count += 1

class Detection:
    def __init__(self,pname,em,mob,gen,dt,sra,dn):
        self.filenames=" "
        self.ws = Tk()
        self.ws.title('Detection')
        self.ws.config(bg='#0B5A81')
        self.msg="Your Blood Group Test Result"+"\n"
        self.f= ('Times', 14)
       
        self.fn=""
        self.fnimpr=""
        self.fnm=" "
        self.em=em
        self.mob=mob
        self.gen=gen
        self.dt=dt
        self.sta=sra
        self.dn=dn
        self.pnm=pname

        right_frame = Frame(
            self.ws, 
            bd=2, 
            bg='#CCCCCC',
            relief=SOLID, 
            padx=20, 
            pady=20,
            height=1000,
            width=1000
            )

        self.pname=Label(
             right_frame,
             text="Patient Name:"
         )    
        self.p1name=Label(
              right_frame,
              text=pname
              
         )
        self.imgdis=Label(
            right_frame,  
            
            
            )
        
        """
        self.gredis=Label(
           right_frame
           
           )
        self.thrdis=Label(
           right_frame
           )"""
        
        self.thradis=Label(
           right_frame
           
           )

        self.thradis1 = Label(
            right_frame

        )
        self.thradis2 = Label(
            right_frame

        )
        
        self.morh=Label(
            right_frame
            )
        self.morh=Label(
            right_frame
            )

        

        
        self.open_btn = Button(
            right_frame, 
            width=15, 
            text='Select Slide', 
            font=self.f, 
            relief=SOLID,
            cursor='hand2' ,
            command=self.setimage
        )
        
        
        self.thresh_btn1 = Button(    
            right_frame,
            width=15, 
            text='Split Image' , 
            font=self.f, 
            relief=SOLID,
            cursor='hand2',
            command=self.split_image
        )
       
        self.morp=Button(
            right_frame,
            width=15, 
            text='SIFT Distance',
            font=self.f, 
            relief=SOLID,
            cursor='hand2',
            command=self.detection
            
            )
        self.pred=Button(
            right_frame,
            width=15, 
            text='Classifer Prediction',
            font=self.f, 
            relief=SOLID,
            cursor='hand2',
            command=self.prediction
            
            )
        
        self.store=Button(
            right_frame,
            width=15, 
            text='Store', 
            font=self.f, 
            relief=SOLID,
            cursor='hand2',
            command=self.insert_record
            
            )
        self.pname.grid(row=1,column=1,pady=10,padx=20)
        self.p1name.grid(row=1,column=2,pady=10,padx=20)
        self.open_btn.grid(row=3, column=1, pady=10, padx=20)
        
        self.thresh_btn1.grid(row=9,column=1,padx=20)
        self.morp.grid(row=11,column=1,padx=20)
        self.pred.grid(row=3,column=4,padx=20)
       
        self.imgdis.grid(row=3,column=2,sticky='nwse')
       
        self.thradis.grid(row=9,column=2)
        self.thradis1.grid(row=9, column=3)
        self.thradis2.grid(row=9, column=4)
        self.morh.grid(row=12,column=2)
        self.pred.grid(row=3,column=4,padx=20)
        self.store.grid(row=4,column=4,padx=20)
        
       
        right_frame.pack()
      

        
    def run(self):
           self.ws.mainloop()
           
           
    def setimage(self):
        self.filenames = filedialog.askopenfilename()
        self.nm=self.filenames
        src = cv2.imread(self.filenames)
        cv2.imwrite("Data/test/tests/to_test.jpg", src)
        im = Image.open(self.filenames)
        resized=im.resize((350,150),Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(resized)
        self.imgdis.configure(image=tkimage)
        self.imgdis.image=tkimage
       
        
    def split_image(self):
        img = cv2.imread(self.filenames,0)

        img1 = Image.open(os.path.join(self.filenames))

        width, height = img1.size
        tile(self.filenames, "output/", int(width / 3))
        #thresh2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,
                                    #cv2.THRESH_BINARY,11,2)
               
        #cv2.imwrite('./setgenerated/threshad.png',thresh2)
        im = Image.open("output/1.jpg")
        resized=im.resize((150,150),Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(resized)
        self.thradis.configure(image=tkimage)
        self.thradis.image=tkimage

        im = Image.open("output/2.jpg")
        resized = im.resize((150, 150), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(resized)
        self.thradis1.configure(image=tkimage)
        self.thradis1.image = tkimage

        im = Image.open("output/3.jpg")
        resized = im.resize((150, 150), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(resized)
        self.thradis2.configure(image=tkimage)
        self.thradis2.image = tkimage

    def  detection(self):
        img = cv2.imread(self.filenames, 0)
        #kernel = np.ones((5,5), np.uint8)
        #img_dilation = cv2.dilate(img, kernel, iterations=1)
        #cv2.imwrite('./setgenerated/morph.png',img_dilation)

        dict = []
        dic11 = []
        for ind in range(1, 4):
            img1 = cv2.imread('output/' + str(ind) + ".jpg")
            # img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
            img2 = cv2.imread('standard/std.jpg')
            # img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

            # create SIFT object
            # sift = cv2.xfeatures2d.SIFT_create()
            sift = cv2.ORB_create(nfeatures=1500)
            # detect SIFT features in both images
            keypoints_1, descriptors_1 = sift.detectAndCompute(img1, None)
            keypoints_2, descriptors_2 = sift.detectAndCompute(img2, None)
            # create feature matcher
            bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
            # match descriptors of both images
            matches = bf.match(descriptors_1, descriptors_2)
            # sort matches by distance
            matches = sorted(matches, key=lambda x: x.distance)
            # print(len(matches))

            dict.append(len(matches))



            # draw first 50 matches
            matched_img = cv2.drawMatches(img1, keypoints_1, img2, keypoints_2, matches[:50], img2, flags=2)
            # show the image
            cv2.imshow('image', matched_img)
            cv2.waitKey(0)
            # save the image

            # cv2.waitKey(0)
            cv2.destroyAllWindows()

        
        cv2.imwrite("matched_images.jpg", matched_img)
        im = Image.open("matched_images.jpg")
        resized = im.resize((350, 150), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(resized)
        self.morh.configure(image=tkimage)
        self.morh.image = tkimage
        print(self.filenames, dict)
        

        t1 = int(dict[0])
        t2 = int(dict[1])
        t3 = int(dict[2])

        print("Comparing with std1")
        dict1 = []
        for ind in range(1, 4):
            img1 = cv2.imread('output/' + str(ind) + ".jpg")
            img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            img2 = cv2.imread('standard/std1.jpg')
            img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

            # create SIFT object
            sift = cv2.xfeatures2d.SIFT_create()
            # sift= cv2.ORB_create(nfeatures=1500)
            # detect SIFT features in both images
            keypoints_1, descriptors_1 = sift.detectAndCompute(img1, None)
            keypoints_2, descriptors_2 = sift.detectAndCompute(img2, None)
            # create feature matcher
            bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
            # match descriptors of both images
            matches = bf.match(descriptors_1, descriptors_2)
            # sort matches by distance
            matches = sorted(matches, key=lambda x: x.distance)
            # print(len(matches))

            dict1.append(len(matches))


        t1 = int(dict[0])
        t2 = int(dict[1])
        t3 = int(dict[2])

        t11 = int(dict1[0])
        t22 = int(dict1[1])
        t33 = int(dict1[2])

        print(t1)
        print(t2)
        print(t3)
        if ((t1 == 0 and t2 == 0) or (t1 == 1 and t2 == 0) or (t1 == 0 and t2 == 1)):

            print("O group")
            group = "O"
        else:
            if (t1 >= 10 and t2 >= 9):  # or (t11 <5 and t22 <7):
                group = "AB"
                print("AB group")
            else:

                if ((t1 - t2) >= 4) and (t2 >= 0 and t2 <= 7):  # or t2<=4) :
                    print("A group")
                    group = "A"

                else:
                    if ((t1 >= 0 and t1 <= 5) or (t2 - t1) > 10):
                        print("B group")
                        group = "B"

        if (t3 >= 0 and t3 <= 2):
            rh = "-"

        else:
            if (t3 > 4):
                rh = "+"

        print(rh)
        self.fnimpr = group+" "+rh
        messagebox.showinfo('BloodDetails', group+" "+rh)



    def prediction(self):
       import cv2


       # np.set_printoptions(suppress=True)
       # model =load_model('Bloodset_model.h5')
       # data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
       # image = Image.open(self.filenames)
       # size = (224, 224)
       # image = ImageOps.fit(image, size, Image.ANTIALIAS)
       # #turn the image into a numpy array
       # image_array = np.asarray(image)
       # # display the resized image
       # #image.show()
       #
       # # Normalize the image
       # normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
       # # Load the image into the array
       # data[0] = normalized_image_array
       # #print(data[0])

       from keras.models import Sequential
       from keras.models import model_from_json
       from sklearn.metrics import classification_report

       model_file = open('Data/Model/model.json', 'r')
       model = model_file.read()
       model_file.close()
       model = model_from_json(model)
       # Getting weights
       model.load_weights("Data/Model/weights.h5")
       # Y = predict(model, X)
       import numpy as np

       labels = ['tests']
       img_size = 224
       import os


       def get_data(data_dir):
           data = []
           for label in labels:
               path = os.path.join(data_dir, label)
               class_num = labels.index(label)
               for img in os.listdir(path):
                   try:
                       img_arr = cv2.imread(os.path.join(path, img))[..., ::-1]  # convert BGR to RGB format
                       resized_arr = cv2.resize(img_arr, (img_size, img_size))  # Reshaping images to preferred size
                       data.append([resized_arr, class_num])
                   except Exception as e:
                       print(e)
           return np.array(data)

       val = get_data('Data/Test')
       x_val = []
       y_val = []
       for feature, label in val:
           x_val.append(feature)
           y_val.append(label)

       x_val = np.array(x_val) / 255
       x_val.reshape(-1, img_size, img_size, 1)
       y_val = np.array(y_val)

       predictions = model.predict(x_val)
       # predictions = predictions.reshape(1,-1)[0]
       print(predictions)


       # run the inference
       #prediction = model.predict(data)
       res=np.argmax(predictions)
       
      # messagebox.showinfo('BloodDetails',res) 
       if res==0:
           self.fn="A+"
           messagebox.showinfo('BloodDetails',"A+") 
       elif res==1:
           self.fn=res="A-"
           messagebox.showinfo('BloodDetails',"A-") 
       elif res==2:
           self.fn="AB+"
           messagebox.showinfo('BloodDetails',"AB+")
       elif res==3:
           self.fn="AB-"
           messagebox.showinfo('BloodDetails',"AB-")
       elif res==4:
           self.fn="B+"
           messagebox.showinfo('BloodDetails',"B+")
       elif res==5:
           self.fn="B-"
           messagebox.showinfo('BloodDetails',"B-")
       elif res==6:
           self.fn="O+"
           messagebox.showinfo('BloodDetails',"O+")
       elif res==7:
           self.fn="O-"
           messagebox.showinfo('BloodDetails',"O-")

       self.msg=self.msg+"Blood Group: "+self.fn+"\n"+ "Thanks for visiting binary pathology Lab"      
           
              
           

    def insert_record(self):
              
                 try:
                       con = sqlite3.connect('BloodDetails.db')
                       nm=self.pnm
                     
                       em=self.em
                      
                       mb=self.mob
                       
                       gn=self.gen
                      
                       st=self.sta
                      
                       dt=self.dt
                      
                       sp=self.filenames
                       
                       dn=self.dn
                     
                       bg=self.fn


                       cur = con.cursor()

                       statement = "SELECT Email from Register WHERE Email='" + em + "';"
                       cur.execute(statement)
                       if cur.fetchone():
                           messagebox.showinfo('confirmation', 'Email id already exists')

                           self.ws.destroy()
                      
                       cur = con.cursor()
                       
                       insert_stmt = (
                       "insert into Register(Name,Email,Contact_Number,Gender,State,Regi_Date,Slide_Path,Donar,BloodGroup)""values(?,?,?,?,?,?,?,?,?)")
                      
                       data = (nm,em,mb,gn,st,dt,sp,dn,bg)
                       
                       cur.execute(insert_stmt, data)
                       
                       con.commit()
                       
                       messagebox.showinfo('BloodDetails','Record Save') 
                       
                       self.mailsend()  
                      
                     
                 except Exception as ep:
                      messagebox.showerror('Error',format(ep))      
                      
                      
               
    def run(self):
        self.ws.mainloop()
    
    def mailsend(self):
        self.ws.destroy()
        global mail
        global mess
        mess=self.msg
        mail=self.em
        mainwindow =Mail_send.Mail_send(mail,mess)
        mainwindow.run()  
       
#
#r=Detection()
#r.run()
