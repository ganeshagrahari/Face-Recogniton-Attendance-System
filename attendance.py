from tkinter import* #for Gui inter face
from tkinter import ttk #for stylish tools
from PIL import Image,ImageTk #for images settings and crop
from tkinter import messagebox
import mysql.connector
import cv2#isme 2500 se jada ml algos hai for images reconition project types,, in this project we are using haar cascades algorithm:eye and face
import os
import csv
from tkinter import filedialog





mydata=[]

#MAKING INTERFACE:---
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")#giving dimentions for appearing width*height+x-axis+y-axis
        self.root.title("FRAS")

        #text variables----------->
        self.var_atten_name=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_status=StringVar()


        #image-1
        img1 =Image.open(r"images\W.jpg")
        img1=img1.resize((800,200))
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1) #for implementing image on application window
        f_lbl.place(x=0,y=0,width=800,height=200) #for showing img
        #image-2
        img2 =Image.open(r"images\N.png")
        img2=img2.resize((800,200))
        self.photoimg2=ImageTk.PhotoImage(img2)
        f_lbl=Label(self.root,image=self.photoimg2) #for implementing image on application window
        f_lbl.place(x=800,y=0,width=800,height=200) #for showing img

        #Background image:-
        img3 =Image.open(r"images\X.png")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3) #for implementing image on application window
        bg_img.place(x=0,y=200,width=1530,height=710)

        
        #For title label:-
        title_lbl=Label(bg_img,text="Attendance Management System",font=("Century",28,"bold"),bg="#E2DA99",fg="#342800")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        # Load the back button image
        back_img = Image.open(r"images\back.png")
        back_img = back_img.resize((40, 40), Image.Resampling.LANCZOS)
        self.photoimg_back = ImageTk.PhotoImage(back_img)

        # Create the back button
        back_btn = Button(self.root, image=self.photoimg_back, command=self.back_to_main, bg="black", borderwidth=0)
        back_btn.place(x=5, y=2, width=40, height=40)

        #making frame:-
        main_frame=Frame(self.root,bd=7)#hmko background img ke upar banana hai
        main_frame.place(x=20,y=250,width=1490,height=530)
         #making left and right label frame:-

        #left label frame:-
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students Attendance Details",font=("Yu Gothic UI Semibold",12,"bold"))
        Left_frame.place(x=5,y=5,width=760,height=510)


       

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")#hmko background img ke upar banana hai
        left_inside_frame.place(x=2,y=0,width=720,height=400)


        #label entries---------->

        #Attandance-id
        AttendanceID_label=Label(left_inside_frame,text="AttandanceID:Std_id",bg="white",font=("Yu Gothic UI Semibold",12,"bold"),)
        AttendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        #AttendanceID_entry=ttk.Entry(left_inside_frame,width=20,font=("Yu Gothic UI Semibold",12,"bold"))
        #AttendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


        #Student-name
        StudentName_label=Label(left_inside_frame,text="Student Name:",bg="white",font=("Yu Gothic UI Semibold",12,"bold"),)
        StudentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        StudentName_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_name,width=20,font=("Yu Gothic UI Semibold",12,"bold"))
        StudentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        #rollno
        rollno_label=Label(left_inside_frame,text="RollNo:",bg="white",font=("Yu Gothic UI Semibold",12,"bold"),)
        rollno_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        
        rollno_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=20,font=("Yu Gothic UI Semibold",12,"bold"))
        rollno_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        #deaparment
        department_label=Label(left_inside_frame,text="Deparment:",bg="white",font=("Yu Gothic UI Semibold",12,"bold"),)
        department_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        
        department_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=20,font=("Yu Gothic UI Semibold",12,"bold"))
        department_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        #date
        date_label=Label(left_inside_frame,text="Date:",bg="white",font=("Yu Gothic UI Semibold",12,"bold"),)
        date_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        
        date_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=20,font=("Yu Gothic UI Semibold",12,"bold"))
        date_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        #time
        time_label=Label(left_inside_frame,text="Time:",bg="white",font=("Yu Gothic UI Semibold",12,"bold"),)
        time_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        
        time_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=20,font=("Yu Gothic UI Semibold",12,"bold"))
        time_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Attendance
        Attendance_label=Label(left_inside_frame,text="Attandance:",bg="white",font=("Yu Gothic UI Semibold",12,"bold"),)
        Attendance_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_status,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

         #button frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=700,height=85)

         #Import CSV button
        
        import_btn=Button(btn_frame,text="Import CSV",command=self.importcsv,width=25,font=("Yu Gothic UI Semibold",12,"bold"),bg="#0073E6",fg="white")
        import_btn.grid(row=0,column=0)
         #Export CSV button
        export_btn=Button(btn_frame,text="Export CSV",command=self.exportcsv,width=25,font=("Yu Gothic UI Semibold",12,"bold"),bg="#0073E6",fg="white")
        export_btn.grid(row=0,column=1)
         #Update button
        #update_btn=Button(btn_frame,text="Update",width=18,font=("Yu Gothic UI Semibold",12,"bold"),bg="#0073E6",fg="white")
        #update_btn.grid(row=0,column=2)
         #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=25,font=("Yu Gothic UI Semibold",12,"bold"),bg="#0073E6",fg="white")
        reset_btn.grid(row=0,column=3)


         #Right label frame:-
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("Yu Gothic UI Semibold",12,"bold"))
        Right_frame.place(x=780,y=5,width=700,height=510)

        #table frame
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=690,height=460)

         #Scroll bars:-
        #X-axis and y-axis
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("name","rollno","department","time","date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        #self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("name",text="Student Name")
        self.AttendanceReportTable.heading("rollno",text="RollNo")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="date")
        self.AttendanceReportTable.heading("Attendance",text="Attendance Status")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cusor)

      #Fetch data--------------->
    def fetchdata(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
          self.AttendanceReportTable.insert("",END,values=i)
    #import csv------->
    def importcsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("ALL File","*.*")),parent=self.root)
        with open (fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchdata(mydata)    
    #export csv------->
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No data found to export!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("ALL File","*.*")),parent=self.root)
            with open(fln,"w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported!","Your data exported to " +os.path.basename(fln)+" Successfully")    
        except Exception as es:
                  messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)         
    def get_cusor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_name.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_dep.set(rows[2])
        self.var_atten_time.set(rows[3])
        self.var_atten_date.set(rows[4])
        self.var_atten_status.set(rows[5])

    def reset_data(self):
        self.var_atten_name.set("")
        self.var_atten_roll.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_status.set("")






    def back_to_main(self):
        self.root.destroy()
        import main
        main.main()




if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)#making class object
    root.mainloop()        