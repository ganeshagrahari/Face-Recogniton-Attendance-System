
from tkinter import* #for Gui inter face
from tkinter import ttk #for stylish tools
from PIL import Image,ImageTk #for images settings and crop
import tkinter
from students import Student
from train import train
from face_recognition import face_recognition
from attendance import Attendance
import os
import webbrowser


#MAKING INTERFACE:---
class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")#giving dimentions for appearing width*height+x-axis+y-axis
        self.root.title("FRAS")
      #image-1
        img =Image.open(r"images\A.jpg")
        img=img.resize((500,185),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg) #for implementing image on application window
        f_lbl.place(x=0,y=0,width=500,height=185) #for showing img
      #image-2
        img1 =Image.open(r"images\B.jpeg")
        img1=img1.resize((500,185),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1) #for implementing image on application window
        f_lbl.place(x=500,y=0,width=500,height=185) #for showing img
      #image-3
        img2 =Image.open(r"images\C.jpg")
        img2=img2.resize((550,185),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2) #for implementing image on application window
        f_lbl.place(x=1000,y=0,width=550,height=185) #for showing img
      #Background image:-
        img3 =Image.open(r"images\E.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3) #for implementing image on application window
        bg_img.place(x=0,y=185,width=1530,height=710) #We want to put this image below previous three images so we kept y axis after three img's height as we start y axis =185


        #For title label:-
        title_lbl=Label(bg_img,text="Face Recognition Attendence System",font=("Cascadia Code",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=70)


        #fuction buttons:-

        #1->student button-
        img4 =Image.open(r"images\N.png")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_deatils,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220,)

        b_1=Button(bg_img,text="Students Details",command=self.student_deatils,cursor="hand2",font=("Century",15,"bold"),bg="black",fg="white")
        b_1.place(x=200,y=300,width=220,height=40)
        #2->dectect face button-
        img5 =Image.open(r"images\F.jpeg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=220,height=220)

        b_2=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("Century",15,"bold"),bg="black",fg="white")
        b_2.place(x=500,y=300,width=220,height=40)
        #3->Attendence button- #there is 300px distence beteen 2 buttons in x-axis
        img6 =Image.open(r"images\G.png")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b2=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.Attendance_data)
        b2.place(x=800,y=100,width=220,height=220)

        b_2=Button(bg_img,text="Attendance",cursor="hand2",command=self.Attendance_data,font=("Century",15,"bold"),bg="black",fg="white")
        b_2.place(x=800,y=300,width=220,height=40)
        #4->help desk button- #there is 300px distence beteen 2 buttons in x-axis
        img7 =Image.open(r"images\H.png")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b2=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.open_html2)
        b2.place(x=1100,y=100,width=220,height=220)

        b_2=Button(bg_img,text="Help desk",cursor="hand2",command=self.open_html2,font=("Century",15,"bold"),bg="black",fg="white")
        b_2.place(x=1100,y=300,width=220,height=40)
        #5->train button- yaha par vertically neeche ja rahe hai to x axis ki starting 200px se hoga than y axis ko neeche karenge
        img8 =Image.open(r"images\I.png")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b2=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b2.place(x=200,y=350,width=220,height=220)

        b_2=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("Century",15,"bold"),bg="black",fg="white")
        b_2.place(x=200,y=550,width=220,height=40)

        #6->photos button
        img9 =Image.open(r"images\J.png")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b2=Button(bg_img,image=self.photoimg9,command=self.open_img,cursor="hand2")
        b2.place(x=500,y=350,width=220,height=220)

        b_2=Button(bg_img,text="Photos",command=self.open_img,cursor="hand2",font=("Century",15,"bold"),bg="black",fg="white")
        b_2.place(x=500,y=550,width=220,height=40)
        #7->devoleper button
        img10 =Image.open(r"images\K.png")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b2=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_html)
        b2.place(x=800,y=350,width=220,height=220)

        b_2=Button(bg_img,text="Developer",cursor="hand2",command=self.open_html,font=("Century",15,"bold"),bg="black",fg="white")
        b_2.place(x=800,y=550,width=220,height=40)
        #8->Exit-button
        img11 =Image.open(r"images\L.png")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b2=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.Iexit)
        b2.place(x=1100,y=350,width=220,height=220)

        b_2=Button(bg_img,text="Exit",cursor="hand2",command=self.Iexit,font=("Century",15,"bold"),bg="black",fg="white")
        b_2.place(x=1100,y=550,width=220,height=40)

    



        

        #-----function buttons-----
    def student_deatils(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)   


       
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=train(self.new_window)
    def Attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognition(self.new_window)  
        
    def open_img(self):
        os.startfile("data")    

    def open_html(self):
        # Path to the HTML file you want to open
        url = 'https://ganesh-portfolio-site.vercel.app/'
        # Open the file in the default web browser
        webbrowser.open(url)
    def open_html2(self):
        # Path to the HTML file you want to open
        url='mailto:ganeshagrahari108@gmail.com'
        # Open the file in the default web browser
        webbrowser.open(url)

    def Iexit(self):
        self.Iexit=tkinter.messagebox.askyesno("FRAS","Are you sure to exit from FRAS!",parent=self.root)   
        if self.Iexit>0:
            self.root.destroy()
        else:
            return    

           
        

      

    
    



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)#making class object
    root.mainloop()