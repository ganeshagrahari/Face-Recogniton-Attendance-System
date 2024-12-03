from tkinter import* #for Gui inter face
from tkinter import ttk #for stylish tools
from PIL import Image,ImageTk #for images settings and crop
from tkinter import messagebox
import mysql.connector
import cv2#isme 2500 se jada ml algos hai for images reconition project types,, in this project we are using haar cascades algorithm:eye and face
import os
import numpy as np







#MAKING INTERFACE:---
class train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")#giving dimentions for appearing width*height+x-axis+y-axis
        self.root.title("FRAS")


        #For title label:-
        title_lbl=Label(self.root,text="Train Data Set",font=("Century",28,"bold"),bg="#FCE77D",fg="#F96167")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # Load the back button image
        back_img = Image.open(r"images\back.png")
        back_img = back_img.resize((40, 40), Image.Resampling.LANCZOS)
        self.photoimg_back = ImageTk.PhotoImage(back_img)

        # Create the back button
        back_btn = Button(self.root, image=self.photoimg_back, command=self.back_to_main, bg="black", borderwidth=0)
        back_btn.place(x=5, y=2, width=40, height=40)

        #putting an image:-
        img_top =Image.open(r"images\Q.jpg")
        img_top=img_top.resize((800,325))
        self.photoimg_left=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_left) #for implementing image on application window
        f_lbl.place(x=350,y=50,width=800,height=325)

        #train button
        b1_1=Button(self.root,text="Train Data(Click here!)",command=self.train_classifire,width=18,font=("Yu Gothic UI Semibold",20,"bold"),bg="#23282D",fg="white",cursor="hand2")
        b1_1.place(x=350,y=380,width=800,height=60)

  

        img_bottom =Image.open(r"images\S.webp")
        img_bottom=img_bottom.resize((1530,325))
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom) #for implementing image on application window
        f_lbl.place(x=0,y=440,width=1530,height=325)
    

    def train_classifire(self):
        data_dir=('data')
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') #converting in gray scale
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        ids=np.array(ids) 

        #---------Training the classifire and save--------------

        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifire.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!",parent=self.root)
           





    def back_to_main(self):
       self.root.destroy()
       import main
       main.main()





if __name__ == "__main__":
    root=Tk()
    obj=train(root)#making class object
    root.mainloop()        