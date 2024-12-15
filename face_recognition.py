from tkinter import* #for Gui inter face
from tkinter import ttk #for stylish tools
from PIL import Image,ImageTk #for images settings and crop
from tkinter import messagebox
import mysql.connector
import cv2#isme 2500 se jada ml algos hai for images reconition project types,, in this project we are using haar cascades algorithm:eye and face
import os
import numpy as np
from time import strftime
from datetime import datetime

#MAKING INTERFACE:---
class face_recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")#giving dimentions for appearing width*height+x-axis+y-axis
        self.root.title("FRAS")

        #For title label:-
        title_lbl=Label(self.root,text="Face Recognizer",font=("Century",28,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)

         # Load the back button image
        back_img = Image.open(r"images\back.png")
        back_img = back_img.resize((40, 40), Image.Resampling.LANCZOS)
        self.photoimg_back = ImageTk.PhotoImage(back_img)

        # Create the back button
        back_btn = Button(self.root, image=self.photoimg_back, command=self.back_to_main,  borderwidth=0)
        back_btn.place(x=5, y=2, width=40, height=40)
        #putting an image:-
        #1st
        img_top =Image.open(r"images\T.jpeg")
        img_top=img_top.resize((500,500))
        self.photoimg_left=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_left) #for implementing image on application window
        f_lbl.place(x=70,y=100,width=500,height=500)

        #recognize button
        b1_1=Button(self.root,text=" Click here to Recognize!",command=self.face_recognization,width=18,font=("Yu Gothic UI Semibold",18,"bold"),bg="#23282D",fg="white",cursor="hand2")
        b1_1.place(x=70,y=600,width=500,height=40)

        #2nd

        img_right =Image.open(r"images\U.jpg")
        img_right=img_right.resize((950,700))
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(self.root,image=self.photoimg_right) #for implementing image on application window
        f_lbl.place(x=650,y=50,width=950,height=700)

       #----Attendence marks-----------
    def mark_attendance(self,n,r,d):
        with open("Attendance.csv","r+",newline="\n") as f:
            mydatalist=f.readlines()
            name_list=[]
            for line in mydatalist:
                entry=line.split((","))
                name_list.append(entry[0])
            if((n not in name_list)) and ((r not in name_list)) and ((d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtstring=now.strftime("%H:%M:%S")
                f.writelines(f"\n{n},{r},{d},{dtstring},{d1},Present")

            

        #----face recognization fxn-----
    def face_recognization(self):
        def draw_boundry(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="123456", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(map(str, i))  # Convert each item in the tuple to a string

                my_cursor.execute("select Name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(map(str, n))  # Convert each item in the tuple to a string

                my_cursor.execute("select Roll_No from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(map(str, r))  # Convert each item in the tuple to a string

                my_cursor.execute("select Dep from student where Student_id=" +str(id))
                d =my_cursor.fetchone()
                d="+".join(d)

                

                



                if confidence>78:
                    cv2.putText(img,f"StudentID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-58),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-11),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    
                    self.mark_attendance(n,r,d)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face!",(x,y-25),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)   

                coord=[x,y,w,h]    

            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundry(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier(r"Model\haarcascade_frontalface_default.xml")    
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifire.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome!",img)
            

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
                    



              

    def back_to_main(self):
        self.root.destroy()
        import main
        main.main() 


if __name__ == "__main__":
    root=Tk()
    obj=face_recognition(root)#making class object
    root.mainloop()