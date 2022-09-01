#  creating a login page 


from ctypes import resize
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk


class resetpage:
    def __init__(self):
        self.root = Tk()
        self.root.title('RESET PAGE')
        self.root.geometry("1350x700") 
        self.root.resizable(height=False,width=False) 
        
        
    def mainframe(self):
    

# inserting image 
        
        self.image=ImageTk.PhotoImage(Image.open("C:/Users/harpr/Desktop/python/o7 python/project/images/bgrp.jpg").resize((1350,700)))
        self.imagelabel=Label(self.root,image=self.image)
        self.imagelabel.place(x=0,y=0)


# # creating a left side frame 

#         self.frame=Frame(self.root,bg="white")
#         self.frame.place(x=800,y=180,height=400,width=700)


        self.main_frame = Frame(self.root, bg='white')
        self.main_frame.place(x = 690, y = 100, width='350', height='500')
        
        self.label=Label(self.root,text="RESET PASSWORD", font=("yu gothic vi",25,"bold"),fg="black",bg="white" )
        self.label.place(x=710,y=110)
        
        self.image1=ImageTk.PhotoImage(Image.open("C:/Users/harpr/Desktop/python/o7 python/project/images/1.jpg").resize((440,430)))
        self.imagelabel=Label(image=self.image1,bg="white")
        self.imagelabel.place(x=690,y=150,height=450,width=350)
        
        
# creating a right side frame 
# creating right side frame 


        self.main_frame2 = Frame(self.root, bg='white')
        self.main_frame2.place(x = 1030, y = 100, width='400', height='500')
        
# label in right side frame


        self.image2=ImageTk.PhotoImage(Image.open("C:/Users\harpr/Desktop/python/o7 python/project/images/9020.jpg").resize((150,150)))
        self.imagelabel=Label(image=self.image2,bd=0)
        self.imagelabel.place(x=1100,y=110)
        
# OLD PASSWORD ENTRY WIDGET 


        self.passLabel = Label(self.root ,text='Old Password :',bg="white",font=("yu gothic vi",15),fg="aqua")
        self.passLabel.place(x = 1042, y = 270)
        self.entryValue1 = StringVar()
        self.entryWidget1 = Entry(self.root, textvariable=self.entryValue1,highlightthickness="0",
                                 relief=FLAT,fg="#040405", bg = "white",cursor="xterm",
                                 font=("yu gothic vi",12,"bold"),show="*")
        separator = ttk.Separator(orient="horizontal")
        separator.place(in_=self.entryWidget1, x=0, rely=1.0, height=2, relwidth=1.0)
        self.entryWidget1.place(x =1040,  y =300 , height=30, width=250)
        
        
# new password entry widget 
        self.passLabel2 = Label(self.root ,text='New Password :',bg="white",font=("yu gothic vi",15),fg="aqua")
        self.passLabel2.place(x = 1042, y = 340)
        self.entryValue2 = StringVar()
        self.entryWidget2 = Entry(self.root, textvariable=self.entryValue2,highlightthickness="0",
                                 relief=FLAT,fg="#040405", bg = "white",cursor="xterm",
                                 font=("yu gothic vi",12,"bold"),show="*")
        separator = ttk.Separator(orient="horizontal")
        separator.place(in_=self.entryWidget2, x=0, rely=1.0, height=2, relwidth=1.0)
        self.entryWidget2.place(x =1040,  y =370 , height=30, width=250)
        
# confirm password 
        self.passLabel = Label(self.root ,text='Confirm Password :',bg="white",font=("yu gothic vi",15),fg="aqua")
        self.passLabel.place(x = 1042, y = 410)
        self.entryValue3 = StringVar()
        self.entryWidget3 = Entry(self.root, textvariable=self.entryValue3,highlightthickness="0",
                                 relief=FLAT,fg="#040405", bg = "white",cursor="xterm",
                                 font=("yu gothic vi",12,"bold"),show="*")
        separator = ttk.Separator(orient="horizontal")
        separator.place(in_=self.entryWidget3, x=0, rely=1.0, height=2, relwidth=1.0)
        self.entryWidget3.place(x =1040,  y =440 , height=30, width=250)
        
        ############################ reset button #################################
        
        ##############################LOGIN BUTTON##################################
        self.image5=ImageTk.PhotoImage(Image.open("C:/Users/harpr/Desktop/python/o7 python/project/images/btn1.png"))
        self.imagelabel=Label(image=self.image5,bg="white")
        self.imagelabel.place(x=1030,y=482)
        
        
        self.loginButton=Button(self.root,text="RESET   " ,fg="white",bg="#3047ff",activebackground="#3047ff",cursor="hand2",font=("yu gothic vi",12,"bold"),bd=0,command=self.reset)  
        self.loginButton.place(x=1045  ,y=500, width=270)  


    

 

     
        self.root.mainloop()
        
    def reset (self):
        if self.entryWidget1.get() == '':
                 messagebox.showerror('Alert', 'All fields Required')
        elif  self.entryWidget2.get()=="":
                messagebox.showerror("Alert","New Password Required")
        elif self.entryWidget3.get()=="":
                     messagebox.showerror("Alert","Confirm Password Required")
                
        elif self.entryWidget3.get()!="entryWidget2.get()":
                 messagebox.showerror("Alert","No match")
                
        else:
                messagebox.showinfo("Success","Password Reset Succefully")

        
 
 
 
 
 
 
 #Alerts in login page##
 
 
# def  login (self):
#         if self.entryValue1.get() =="":  and if self.entryValue2.get() =="": and  if self.entryValue3.get() =="":
#         messagebox.showerror('Alert', 'Enter your Username first')
                
                
                
        #     if self.passValue.get() =="":
        #         messagebox.showerror('Alert', 'Enter your Password first')

 
     
if __name__ == "__main__":
    obj = resetpage()
    obj.mainframe()
   