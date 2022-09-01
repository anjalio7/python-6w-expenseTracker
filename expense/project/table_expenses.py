
from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
import database, editExpenses

class table_expenses:
    def __init__(self):
        self.root = Toplevel()
        self.root.title('Expenses Table')
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
        self.label=Label(self.root,text="Expenditures", font=("yu gothic vi",30,"bold"),bg="white",fg="#0096FF", pady=10 )
        self.label.place(x=580,y=110)
        
        
        
# expenses label 
      
        
        
# tables in frame 

        self.monOptions = ['January', 'February', 'march', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.monthDrop = ttk.Combobox(self.main_frame2, values=self.monOptions )
        self.monthDrop.place(x=130,y=100)

        self.monthDrop.bind("<<ComboboxSelected>>", lambda type = 'filter': self.allTable(type))

        self.allTable('all')
        self.root.mainloop()

    def allTable(self, type):
        self.tr = ttk.Treeview(self.main_frame2, columns=('A', 'B', 'C', 'E', 'F', 'G'), selectmode="extended")

        self.tr.heading('#0',text="ID")
        self.tr.column('#0',minwidth=0,width=25,stretch=NO)

        self.tr.heading('#1',text="Category")
        self.tr.column('#1',minwidth=0,width=50 ,stretch=NO)

        self.tr.heading('#2', text="Amount")
        self.tr.column('#2', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#3', text="Month")
        self.tr.column('#3', minwidth=0, width=100, stretch=NO)


        self.tr.heading('#4', text="Edit")
        self.tr.column('#4', minwidth=0, width=100, stretch=NO)

        self.tr.heading('#5', text="Delete")
        self.tr.column('#5', minwidth=0, width=80, stretch=NO)


        if type == 'all':
       
            res = database.allExpenses((self.data[0], ))
            if res:
                for i in res:
                        self.tr.insert('', 0, text=i[0], values=(i[1], i[2], i[3], 'Edit', 'Delete'))
            else:
                messagebox.showerror('A')
        else:
            data = database.getFilterExp((self.data[0], self.monthDrop.get()))
            if len(data)>0:
                for i in data:
                    self.tr.insert('', 0, text=i[0], values=(i[1], i[2], i[3], 'Edit', 'Delete'))

        self.tr.bind('<Double-Button-1>', self.actions)
        self.tr.place(x=0,y=150,width="800",height="400")

    def actions(self, e):
        tt = self.tr.focus()

        # get the column id
        col = self.tr.identify_column(e.x)

        gup = (
            self.tr.item(tt).get('text'),
        )
        if col == '#5':
            res = messagebox.askyesno("ALERT", "Do You Realy Want to delete this item")
            if res:
                rs = database.deleteExpense(gup)
                if rs:
                    messagebox.showinfo("ALERT", "Suuccessfully Deleted")
                    self.root.destroy()
                    obj = table_expenses()
                    obj.mainframe(self.data)

        if col == '#4':
             obj = editExpenses.expenses()
             obj.mainframe(gup, self.data)



if __name__=="__main__":
    obj=table_expenses()
    obj.mainframe()        