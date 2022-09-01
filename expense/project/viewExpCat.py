
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
import database, editExpCat

class table_expCat:
    def __init__(self):
        self.root = Toplevel()
        self.root.title('ASSETS Table')
        self.root.geometry("1350x700") 
        self.root.resizable(height=False,width=False) 
        
        
        
    def mainframe(self, data):
        self.data = data
#  inserting image 
  
        self.image=ImageTk.PhotoImage(Image.open("images/desk-office.jpg").resize((1350,700)))
        self.imagelabel=Label(self.root,image=self.image)
        self.imagelabel.pack(fill="both",expand="yes")
        
        
        
        
# frame

        self.main_frame2 = Frame(self.root, bg='white')
        
        self.main_frame2.place(x =300, y = 100, width='800', height='500')
        self.label=Label(self.root,text="ASSETS", font=("yu gothic vi",30,"bold"),bg="white",fg="#0096FF" )
        self.label.place(x=600,y=110)
        
        
        
      
        
        
# tables in frame 

        self.tr = ttk.Treeview(self.main_frame2, columns=('A', 'B', 'C', 'E', 'F', 'G'), selectmode="extended")

        self.tr.heading('#0',text="ID")
        self.tr.column('#0',minwidth=0,width=25,stretch=NO)

        self.tr.heading('#1',text="Name")
        self.tr.column('#1',minwidth=0,width=50 ,stretch=NO)

        self.tr.heading('#2', text="Type")
        self.tr.column('#2', minwidth=0, width=100, stretch=NO)

        # self.tr.heading('#3', text="Source")
        # self.tr.column('#3', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#3', text="Edit")
        self.tr.column('#3', minwidth=0, width=100, stretch=NO)


        self.tr.heading('#4', text="Delete")
        self.tr.column('#4', minwidth=0, width=100, stretch=NO)

        # print(self.data[0][0])
        res = database.allExpCat((self.data[0], ))
        if res:
                for i in res:
                        self.tr.insert('', 0, text=i[0], values=(i[2], i[3], 'Edit', 'Delete'))
        else:
                messagebox.showerror('A')
       

        self.tr.bind('<Double-Button-1>', self.actions)
        self.tr.place(x=0,y=100,width="800",height="400")

        
        
    
        self.root.mainloop()


    def actions(self, e):
        tt = self.tr.focus()

        # get the column id
        col = self.tr.identify_column(e.x)

        gup = (
            self.tr.item(tt).get('text'),
        )
        if col == '#4':
            res = messagebox.askyesno("ALERT", "Do You Realy Want to delete this item")
            if res:
                rs = database.deleteExpCat(gup)
                if rs:
                    messagebox.showinfo("ALERT", "Suuccessfully Deleted")
                    self.root.destroy()
                    obj = table_expCat()
                    obj.mainframe(self.data)

        if col == '#3':
             obj = editExpCat.expCat()
             obj.mainframe(gup, self.data)

        
if __name__=="__main__":
    obj=table_expCat()
    obj.mainframe()        