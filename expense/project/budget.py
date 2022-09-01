# budget page for project in tkinter  

from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
import database,table_budget

class budget:
    def __init__(self):
        self.root = Tk()
        self.root.title('Sources_of_income')
        self.root.geometry("1350x700") 
        self.root.resizable(height=False,width=False) 
        
        
    def mainframe(self):
        
        
        
# inserting image 
        
        self.image=ImageTk.PhotoImage(Image.open("C:/Users/harpr/Desktop/python/o7 python/project/images/bgbudget.jpg").resize((1350,700)))
        self.imagelabel=Label(self.root,image=self.image)
        self.imagelabel.pack(fill="both",expand="yes")
        
        
        
        
# creating left side frame 

        self.main_frame = Frame(self.root, bg='#040405')
        self.main_frame.place(x = 305, y = 100, width='410', height='500')
        
        self.image1=ImageTk.PhotoImage(Image.open("C:/Users/harpr/Desktop/python/o7 python/project/images/budget.png").resize((390,450)))
        self.imagelabel=Label(image=self.image1,bg="#040405")
        self.imagelabel.place(x=350,y=150,height=450,width=350)
        
# creating right side frame 


        self.main_frame2 = Frame(self.root, bg='aqua')
        self.main_frame2.place(x = 705, y = 100, width='400', height='500')
        
# labeling wecome 
    
        self.label=Label(self.root,text="WELCOME ", font=("yu gothic vi",25),fg="aqua",bg="black" )
        self.label.place(x=410,y=110)
# labling budget world
        self.label=Label(self.root,text="BUDGET WORLD", font=("yu gothic vi",25,"bold"),fg="#040405",bg="aqua" )
        self.label.place(x=755,y=110)

#  month dropdown box
        
        self.monthLabel = Label(self.root, text='Month :',bg="aqua",font=("yu gothic vi",15),fg="black")
        self.monthLabel.place(x =715, y = 230)

        self.monthValue = StringVar()
        self.options = ['January', 'Febraury', 'March',"April","May","June","July","August","September","October","November","December"]
        
        self.dropDown = ttk.Combobox(self.root, textvariable=self.monthValue, values=self.options)
    
        self.dropDown.place(x=790,y=230 ,width="300",height="30")
        
# income .label 

        self.incomeLabel = Label(self.root, text='Income:',bg="aqua",font=("yu gothic vi",15),fg="#040405")
        self.incomeLabel.place(x =715, y = 290)
        self.incomeValue1 = StringVar()
        self.incomeWidget1 = Entry(self.root, textvariable=self.incomeValue1,highlightthickness="0",
                                 relief=FLAT,fg="#040405",cursor="xterm",
                                 font=("yu gothic vi",12,"bold"))
        self.incomeWidget1.place(x =790 ,  y =290 , height=30, width=300)
        
        
# # saving labeling 
#         self.savingLabel = Label(self.root, text='Saving:',bg="aqua",font=("yu gothic vi",15),fg="#040405")
#         self.savingLabel.place(x =715, y = 325)
#         self.savingValue1 = StringVar()
#         self.savingWidget1 = Entry(self.root, textvariable=self.savingValue1,highlightthickness="0",
#                                  relief=FLAT,fg="blue",cursor="xterm",
#                                  font=("yu gothic vi",12,"bold"))
#         self.savingWidget1.place(x =790 ,  y =330 , height=30, width=300)

# saving dropdown 
  
        self.savingLabel = Label(self.root, text='Saving :',bg="aqua",font=("yu gothic vi",15),fg="black")
        self.savingLabel.place(x =715, y = 355)

        self.savingValue = StringVar()
        self.options = ['5%', '10%', '15%',"20%","30%","40%","50%","60%","  CUSTOM "]
        
        self.dropDown = ttk.Combobox(self.root, textvariable=self.savingValue, values=self.options)
    
        self.dropDown.place(x=790,y=355 ,width="300",height="30")
        
# add button

        self.add_button=ImageTk.PhotoImage(Image.open("C:/Users/harpr/Desktop/python/o7 python/project/images/btn1.png").resize((250,50)))
        self.imagelabel=Label(image=self.add_button,bg="aqua")
        self.imagelabel.place(x=800,y=430)
         
        self.addButton=Button(self.root,text="ADD" ,fg="white",bg="#3047ff",activebackground="#3047ff",cursor="hand2",font=("yu gothic vi",12,"bold"),bd=0,command=self.budget)  
        
        self.addButton.place(x=830,y=444, width=200)   
        
        self.root.mainloop()
        
        
        
        
# alert boxes 
    def budget (self):
        if self.monthValue.get() == '' or self.incomeWidget1.get()==""  or self.savingValue.get()=="":
                 messagebox.showerror('Alert', 'All fields required')

        # else:
        #          messagebox.showinfo("Success","Data Enter succefully ")
        
        else:
                  self.data = (
                          self.monthLabel.get(),
                          self.incomeWidget1.get(),
                          self.savingValue.get()
                  )
                  print(self.data)
                  res = database.budget(self.data)
                  if res:
                          messagebox.showinfo('Success', 'Registered Successfully')
                          self.root.destroy()
                          obj = table_budget.tablebudget()
                          messagebox.showerror('Alert', 'Something went wrong.')
                          obj.mainframe()
                  else:
                        messagebox.showerror('Alert', 'Something went wrong.')
        
        
        
        
if __name__ ==  "__main__":
    obj=budget()
    obj.mainframe()

        