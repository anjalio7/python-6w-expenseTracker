from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk

class tablebudget:
    def __init__(self):
        self.root = Tk()
        self.root.title('Expenses Table')
        self.root.geometry("1350x700") 
        self.root.resizable(height=False,width=False) 
        
        
    def mainframe(self):
#  inserting image 
  
        self.image=ImageTk.PhotoImage(Image.open("C:/Users/harpr/Desktop/python/o7 python/project/images/desk-office.jpg").resize((1350,700)))
        self.imagelabel=Label(self.root,image=self.image)
        self.imagelabel.pack(fill="both",expand="yes")
        
        
        
        
# frame

        self.main_frame2 = Frame(self.root, bg='white')
        
        self.main_frame2.place(x =300, y = 100, width='800', height='500')
        self.label=Label(self.root,text="Budget Plan", font=("Times New Roman",30,"bold"),bg="white",fg="#0096FF" )
        self.label.place(x=580,y=110)
        
        
        
# expenses label 
      
        
        
# tables in frame 

        self.tr = ttk.Treeview(self.main_frame2, columns=('A', 'B', 'C', 'E', 'F', 'G','H', 'I'), selectmode="extended")

        self.tr.heading('#0',text="ID")
        self.tr.column('#0',minwidth=25,width=40,stretch=NO)

        self.tr.heading('#1',text="Month")
        self.tr.column('#1',minwidth=50,width=60 ,stretch=NO)

        self.tr.heading('#2', text="Income")
        self.tr.column('#2', minwidth=70, width=70, stretch=NO)

        self.tr.heading('#3', text="Saving")
        self.tr.column('#3', minwidth=80, width=80, stretch=NO)



        self.tr.heading('#4', text="Edit")
        self.tr.column('#4', minwidth=100, width=100, stretch=NO)

        self.tr.heading('#5', text="Delete")
        self.tr.column('#5', minwidth=80, width=80, stretch=NO)


        self.tr.place(x=0,y=100,width="800",height="400")

        
        
    
        self.root.mainloop()
        
if __name__=="__main__":
    obj=tablebudget()
    obj.mainframe()       