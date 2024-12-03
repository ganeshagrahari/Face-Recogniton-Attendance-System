from tkinter import* #for Gui inter face
from tkinter import ttk #for stylish tools
from PIL import Image,ImageTk #for images settings and crop
from tkinter import messagebox
import mysql.connector
import cv2#isme 2500 se jada ml algos hai for images reconition project types,, in this project we are using haar cascades algorithm:eye and face
from tkcalendar import DateEntry







#MAKING INTERFACE:---
class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")#giving dimentions for appearing width*height+x-axis+y-axis
        self.root.title("FRAS")


        #----------------variables----------
        self.var_Dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_dob=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_rollno=StringVar()

        
        #image-2
        img2 =Image.open(r"images\N.png")
        img2=img2.resize((380,140))
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2) #for implementing image on application window
        f_lbl.place(x=500,y=0,width=400,height=140) #for showing img
        
         #Background image:-
        img3 =Image.open(r"images\E.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3) #for implementing image on application window
        bg_img.place(x=0,y=130,width=1530,height=710) #We want to put this image below previous three images so we kept y axis after three img's height as we start y axis =185


        #For title label:-
        title_lbl=Label(bg_img,text="Student Management System",font=("Century",28,"bold"),bg="#E2DA99",fg="#342800")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        # Load the back button image
        back_img = Image.open(r"images\back.png")
        back_img = back_img.resize((40, 40), Image.Resampling.LANCZOS)
        self.photoimg_back = ImageTk.PhotoImage(back_img)

        back_btn = Button(bg_img, image=self.photoimg_back, command=self.back_to_main, bg="#E2DA99", borderwidth=0)
        back_btn.place(x=5, y=2, width=40, height=40)

        #making frame:-
        main_frame=Frame(bg_img,bd=2)#hmko background img ke upar banana hai
        main_frame.place(x=20,y=50,width=1490,height=600)

        #making left and right label frame:-

        #left label frame:-
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students Details",font=("Yu Gothic UI Semibold",12,"bold"))
        Left_frame.place(x=5,y=5,width=760,height=590)
          #putting an image:-
        img_left =Image.open(r"images\P.png")
        img_left=img_left.resize((400,130))
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left) #for implementing image on application window
        f_lbl.place(x=0,y=0,width=400,height=130)

          #current course information:-
        Current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Info",font=("Yu Gothic UI Semibold",12,"bold"))
        Current_course_frame.place(x=5,y=135,width=730,height=115)
          #Making labels:-
            #deparment
        dep_label=Label(Current_course_frame,text="Department",bg="white",font=("Yu Gothic UI Semibold",12,"bold"),)
        dep_label.grid(row=0,column=0,padx=10,)
        
        dep_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_Dep,font=("Yu Gothic UI Semibold",12,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select Deparment","School of Architecture","School of Computer Application","College of dental Science","School of Engineering")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
            #Course
        course_label=Label(Current_course_frame,text="Course",bg="white",font=("Yu Gothic UI Semibold",12,"bold"),)
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_course,font=("Yu Gothic UI Semibold",12,"bold"),width=17,state="read only")
        course_combo["values"]=("Select Course","BCA","BCA DS&AI","BCA CS&F","Btech CS","Btech IT","Btech Electronic", "Btech Eletrical", "Btech Civil", "Btech Mechanical","BBA","MBA","BDS")
        course_combo.current(0)
        course_combo.grid(row=0,column=2,padx=2,pady=10)
         #Year
        Year_label=Label(Current_course_frame,text="Acadamic Year",bg="white",font=("Yu Gothic UI Semibold",12,"bold"),)
        Year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        Year_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_year,font=("Yu Gothic UI Semibold",12,"bold"),width=17,state="read only")
        Year_combo["values"]=("Select Year","1","2","3","4","5")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=2,pady=10)
            #Semester
        Semester_label=Label(Current_course_frame,text="Semester",bg="white",font=("Yu Gothic UI Semibold",12,"bold"),)
        Semester_label.grid(row=1,column=2,padx=10,sticky=W)
        
        Semester_combo=ttk.Combobox(Current_course_frame,textvariable=self.var_sem,font=("Yu Gothic UI Semibold",12,"bold"),width=17,state="read only")
        Semester_combo["values"]=("Select Semester","1","2")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=2,padx=2,pady=10)
        
        #Class studentd information:-
        Class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Info",font=("Yu Gothic UI Semibold",12,"bold"))
        Class_Student_frame.place(x=5,y=250,width=730,height=308)
        #Student-id
        StudentID_label=Label(Class_Student_frame,text="StudentID:",bg="white",font=("Yu Gothic UI Semibold",12,"bold"),)
        StudentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        StudentID_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_id,width=20,font=("Yu Gothic UI Semibold",12,"bold"))
        StudentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        #Student-name
        StudentName_label=Label(Class_Student_frame,text="Student Name:",bg="white",font=("Yu Gothic UI Semibold",12,"bold"),)
        StudentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        StudentName_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_std_name,width=20,font=("Yu Gothic UI Semibold",12,"bold"))
        StudentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        #Classdivision
        class_div_label=Label(Class_Student_frame,text="Class Division:",bg="white",font=("Yu Gothic UI Semibold",12,"bold"),)
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        #class_div_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_div,width=20,font=("Yu Gothic UI Semibold",12,"bold"))
        #class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        class_div_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_div,font=("Yu Gothic UI Semibold",12,"bold"),width=17,state="read only")
        class_div_combo["values"]=("Select Division","A","B","C","D","F","G","H")
        class_div_combo.current(0)
        class_div_combo.grid(row=1,column=1,padx=10,pady=5)
        #rollno
        rollno_label=Label(Class_Student_frame,text="Roll No:",bg="white",font=("Yu Gothic UI Semibold",12,"bold"),)
        rollno_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        rollno_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_rollno,width=20,font=("Yu Gothic UI Semibold",12,"bold"))
        rollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        #Gender
        gender_label=Label(Class_Student_frame,text="Gender:",bg="white",font=("Yu Gothic UI Semibold",12,"bold"),)
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        #gender_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_gender,width=20,font=("Yu Gothic UI Semibold",12,"bold"))
        #gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        gender_combo=ttk.Combobox(Class_Student_frame,textvariable=self.var_gender,font=("Yu Gothic UI Semibold",12,"bold"),width=17,state="read only")
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5)

        # DOB
        DOB_label = Label(Class_Student_frame, text="DOB:", bg="white", font=("Yu Gothic UI Semibold", 12, "bold"))
        DOB_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        DOB_entry = DateEntry(Class_Student_frame, textvariable=self.var_dob, width=10, font=("Yu Gothic UI Semibold", 10, "bold"), date_pattern='dd/mm/yyyy', background='darkblue', foreground='white', borderwidth=2)
        DOB_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        Email_label = Label(Class_Student_frame, text="Email:", bg="white", font=("Yu Gothic UI Semibold", 12, "bold"))
        Email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        Email_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_email, width=20, font=("Yu Gothic UI Semibold", 12, "bold"))
        Email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        #phone
        Phone_label=Label(Class_Student_frame,text="Phone:",bg="white",font=("Yu Gothic UI Semibold",12,"bold"),)
        Phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        
        Phone_entry=ttk.Entry(Class_Student_frame,textvariable=self.var_phone,width=20,font=("Yu Gothic UI Semibold",12,"bold"))
        Phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Radio butttons:

        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1, text= "Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)


        radiobtn2=ttk.Radiobutton(Class_Student_frame, variable=self.var_radio1,  text="No Photo Sample", value="No")
        radiobtn2.grid(row=5,column=1)

        

         #button frame
        btn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=180,width=700,height=85)

         #save button
        
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=19,font=("Yu Gothic UI Semibold",12,"bold"),bg="#0073E6",fg="white")
        save_btn.grid(row=0,column=0)
         #update button
        update_btn=Button(btn_frame,text="Update",command=self.Update_data,width=18,font=("Yu Gothic UI Semibold",12,"bold"),bg="#0073E6",fg="white")
        update_btn.grid(row=0,column=1)
         #delete button
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=18,font=("Yu Gothic UI Semibold",12,"bold"),bg="#0073E6",fg="white")
        delete_btn.grid(row=0,column=2)
         #reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=("Yu Gothic UI Semibold",12,"bold"),bg="#0073E6",fg="white")
        reset_btn.grid(row=0,column=3)
         #Take photo
        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Photo",width=19,font=("Yu Gothic UI Semibold",12,"bold"),bg="#0073E6",fg="white")
        take_photo_btn.grid(row=1,column=0)
         #update photo button
        update_photo_btn=Button(btn_frame,text="Update Photo Sample",width=18,font=("Yu Gothic UI Semibold",12,"bold"),bg="#0073E6",fg="white")
        update_photo_btn.grid(row=1,column=1)
         
        

        


        
        
        #Right label frame:-
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students Details",font=("Yu Gothic UI Semibold",12,"bold"))
        Right_frame.place(x=780,y=5,width=700,height=590)

        img_Right =Image.open(r"images\M.jpg")
        img_Right=img_Right.resize((500,130))
        self.photoimg_Right=ImageTk.PhotoImage(img_Right)

        f_lbl=Label(Right_frame,image=self.photoimg_Right) #for implementing image on application window
        f_lbl.place(x=0,y=0,width=500,height=130)


        #-----------------SEARCH SYSTEM----------
        #FOR searching data:-
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("Yu Gothic UI Semibold",12,"bold"))
        Search_frame.place(x=5,y=135,width=670,height=70)

        Search_label=Label(Search_frame,text="Search By:",bg="white",font=("Yu Gothic UI Semibold",15,"bold"),)
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        self.var_search = StringVar()

        

        Search_entry=ttk.Entry(Search_frame,textvariable=self.var_search,width=15,font=("Yu Gothic UI Semibold",12,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Search_btn=Button(Search_frame,text="Search",command=self.search_data,width=12,font=("Yu Gothic UI Semibold",10,"bold"),bg="#342800",fg="#DFDED4")
        Search_btn.grid(row=0,column=3,padx=4)

        Showall_btn=Button(Search_frame,text="Show All",width=12,font=("Yu Gothic UI Semibold",10,"bold"),bg="#342800",fg="#DFDED4")
        Showall_btn.grid(row=0,column=4,padx=4)

        #For showing data:-

        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=670,height=350)


        #Scroll bars:-
        #X-axis and y-axis
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("Dep","course","year","sem","id","name","div","dob","gender","email","phone","rollno","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="PhoneNo")
        self.student_table.heading("rollno",text="Roll_No")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("Dep",width=180)
        self.student_table.column("course",width=90)
        self.student_table.column("year",width=50)
        self.student_table.column("sem",width=70)
        self.student_table.column("id",width=80)
        self.student_table.column("name",width=120)
        self.student_table.column("div",width=60)
        self.student_table.column("dob",width=60)
        self.student_table.column("gender",width=70)
        self.student_table.column("email",width=190)
        self.student_table.column("phone",width=90)
        self.student_table.column("rollno",width=70)
        self.student_table.column("photo",width=120)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cusor)
        self.fetch_data()

   #------function decration for adding data--------
    def add_data(self):
        if self.var_Dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="" :
            messagebox.showerror("Error","Can't save data you have not entered required field.",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_Dep.get(),
                                                                                        self.var_course.get(),
                                                                                        self.var_year.get(),
                                                                                        self.var_sem.get(),
                                                                                        self.var_std_id.get(),
                                                                                        self.var_std_name.get(),
                                                                                        self.var_div.get(),
                                                                                        self.var_dob.get(),
                                                                                        self.var_gender.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_phone.get(),
                                                                                        self.var_rollno.get(),
                                                                                        self.var_radio1.get()
                                                                                       
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root) 

  #------function decration for searching data--------
    def search_data(self):
        if self.var_search.get() == "":
            messagebox.showerror("Error", "Please enter a phone number to search.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="123456", database="face_recognizer")
                my_cursor = conn.cursor()
                query = "SELECT * FROM student WHERE Roll_No=%s"
                value = (self.var_search.get(),)
                my_cursor.execute(query, value)
                data = my_cursor.fetchone()
                if data:
                    self.var_Dep.set(data[0])
                    self.var_course.set(data[1])
                    self.var_year.set(data[2])
                    self.var_sem.set(data[3])
                    self.var_std_id.set(data[4])
                    self.var_std_name.set(data[5])
                    self.var_div.set(data[6])
                    self.var_dob.set(data[7])
                    self.var_gender.set(data[8])
                    self.var_email.set(data[9])
                    self.var_phone.set(data[10])
                    self.var_rollno.set(data[11])
                    self.var_radio1.set(data[12])
                else:
                    messagebox.showerror("Error", "No student found with this Roll No.", parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)               
    
    #-----------Fetching and showing data on the table------
    def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select*from student")
                data=my_cursor.fetchall()

                if len(data)!=0:
                     self.student_table.delete(*self.student_table.get_children())
                     for i in data:
                           self.student_table.insert("",END,values=i)
                     conn.commit()
                conn.close()
        #Get cursor------------->
    def get_cusor(self,event=""):
         cusor_focus=self.student_table.focus()
         content=self.student_table.item(cusor_focus)            
         data=content["values"]

         self.var_Dep.set(data[0])
         self.var_course.set(data[1]),
         self.var_year.set(data[2]),
         self.var_sem.set(data[3]),
         self.var_std_id.set(data[4]),
         self.var_std_name.set(data[5]),
         self.var_div.set(data[6]),
         self.var_dob.set(data[7]),
         self.var_gender.set(data[8]),
         self.var_email.set(data[9]),
         self.var_phone.set(data[10]),
         self.var_rollno.set(data[11]),
         self.var_radio1.set(data[12])


    #Functioning of Update button:---------
    def Update_data(self):
        if self.var_Dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="" :
            messagebox.showerror("Error","Can't save data you have not entered required field.",parent=self.root)
        else:
             try:
                   Update=messagebox.askyesno("Update","Do you want to update students details?",parent=self.root)    
                   if Update>0:
                       conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="face_recognizer")
                       my_cursor=conn.cursor()
                       my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,DOB=%s,Gender=%s,Email=%s,Phone_No=%s,Roll_No=%s,Photo_Sample=%s where Student_id=%s",(
                                                                                                                                                                                                              
                        self.var_Dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_dob.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_rollno.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()
                            ))
                   else:
                        if not Update:
                            return
                   messagebox.showinfo("Success","Students details successfully updated.",parent=self.root)
                   conn.commit()     
                   self.fetch_data()
                   conn.close()
             except Exception as es:
                  messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root) 
    #delete function
    def delete_data(self):
         if self.var_std_id.get()=="":
              messagebox.showerror("Error","Student id must be require",parent=self.root)              
         else:
              try:
                   delete=messagebox.askyesno("Student Delete Page","Do you want to delete the student",parent=self.root) 
                   if delete>0:
                        conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="face_recognizer")
                        my_cursor=conn.cursor()
                        sql="delete from student where Student_id=%s"
                        val=(self.var_std_id.get(),)
                        my_cursor.execute(sql,val)
                   else:
                        if not delete:
                             return
                   conn.commit()     
                   self.fetch_data()
                   conn.close()
                   messagebox.showinfo("Deleted","Successfully deleted student details",parent=self.root)
              except Exception as es:
                  messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #Reset Function-------------->
    def reset_data(self):
         self.var_Dep.set("Select Department"), 
         self.var_course.set("Select Course"),
         self.var_year.set("Select Year"),
         self.var_sem.set("Select Semester"),
         self.var_std_id.set(""),
         self.var_std_name.set(""),
         self.var_div.set("Select Division"),
         self.var_dob.set(""),
         self.var_gender.set("Select Gender"),
         self.var_email.set(""),
         self.var_phone.set(""),
         self.var_rollno.set(""),
         self.var_radio1.set("") 


    #-----------------GENERATE DATA SET TAKE PHOTO SAMPLE-------------------
    def generate_dataset(self):
         if self.var_Dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="" :
            messagebox.showerror("Error","Can't save data you have not entered required field.",parent=self.root)
         else:
             try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="123456",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("select * from student")
                    myresult=my_cursor.fetchall()
                    id=0
                    for x in myresult:
                         id+=1
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,DOB=%s,Gender=%s,Email=%s,Phone_No=%s,Roll_No=%s,Photo_Sample=%s where Student_id=%s",(
                                                                                                                                                                                                              
                        self.var_Dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_dob.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_rollno.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()==id+1
                            ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    #-----Loading pre define data on face frontals from open cv---------
                    face_classifire=cv2.CascadeClassifier("Model\haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                         gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                         faces=face_classifire.detectMultiScale(gray,1.3,5)
                         #scaling factor=1.3by default
                         #minium neighbor=5
                         for(x,y,w,h) in faces:
                              face_cropped=img[y:y+h,x:x+w]
                              return face_cropped
                         
                    cap=cv2.VideoCapture(0)
                    img_id=0
                    while True:
                         ret,my_frame=cap.read()
                         if face_cropped(my_frame) is not None:
                              img_id+=1
                              face=cv2.resize(face_cropped(my_frame),(450,450))     
                              face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                              file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                              cv2.imwrite(file_name_path,face)
                              cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                              cv2.imshow("Cropped Face", face)

                         if cv2.waitKey(1)==13 or int(img_id)==100:
                               break

               
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result","Generating data completed!",parent=self.root)
             except Exception as es:
                  messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)



                        








                                             
                        
                               

                     
             
             
                       
                            
                  
                       
             


                             
               
               







        


    def back_to_main(self):
        self.root.destroy()
        import main
        main.main()

      
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)#making class object
    root.mainloop()