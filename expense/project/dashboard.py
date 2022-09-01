
from cgitb import text
from tkinter import *
from tkinter import ttk,Tk
from tkinter import messagebox
from PIL import Image,ImageTk

import sources1, table_sources
import expenses, table_expenses
import addExpCat, viewExpCat
import addBudget, viewBudget, database
# import database,sources1

class dashboard:
    def __init__(self):
        self.root = Tk()
        self.root.title('DASHBOARD')
        self.root.geometry("1350x700") 
        self.root.resizable(height=False,width=False) 
        
        
    def mainframe(self, data):
        self.data = data
        
        
# inserting image 
        
        self.image=ImageTk.PhotoImage(Image.open("images/new4.jpg").resize((1350,700)))
        self.imagelabel=Label(self.root,image=self.image)
        self.imagelabel.pack(fill="both",expand="yes") 
        
        
# creating a frame

        self.main_frame = Frame(self.root, bg='#040405')
        self.main_frame.place(x = 105, y = 100, width='1130', height='550')
        
#creating a 2nd frame 
       
        self.main_frame2 = Frame(self.root, bg='aqua')
        self.main_frame2.place(x = 117, y = 110, width='1105', height='530')
        
        
# creating a 3rd frame
        self.main_frame3 = Frame(self.root, bg='white')
        self.main_frame3.place(x = 129, y = 120, width='1080', height='510')

        self.incomeLabel = Label(self.main_frame3, bg="white", font=("yu gothic vi", 25), fg="blue", text='Income').place(x = 30, y = 50)
        self.totalIncome = Label(self.main_frame3, bg="white", font=("yu gothic vi", 25))
        self.totalIncome.place(x = 200, y = 50)

        self.ExpenseLabel = Label(self.main_frame3, bg="white", font=("yu gothic vi", 25), fg="blue", text='Expense').place(x = 30, y = 150)
        self.totalExpense = Label(self.main_frame3, bg="white", font=("yu gothic vi", 25))
        self.totalExpense.place(x = 200, y = 150)

        self.CategoryLabel = Label(self.main_frame3, bg="white", font=("yu gothic vi", 25), fg="blue", text='Expense \n Categories').place(x = 30, y = 250)
        self.totalCategory = Label(self.main_frame3, bg="white", font=("yu gothic vi", 25))
        self.totalCategory.place(x = 200, y = 250)


        res  = database.allSources((self.data[0], ))
        if len(res) > 0:
            a = [i[3] for i in res]
            self.totalIncome.config(text = '₹ ' + str(sum(a)) )
        else:
            self.totalIncome.config(text = '₹ ' + str(0) )

        res = database.allExpenses((self.data[0], ))
        if len(res) > 0:
            a = [i[2] for i in res]
            self.totalExpense.config(text = '₹ ' + str(sum(a)) )
        else:
            self.totalExpense.config(text = '₹ ' + str(0) )

        res = database.allExpCat((self.data[0], ))
        if len(res) > 0:
            self.totalCategory.config(text = len(res))
        
        
# creatin a menu in frame 3 
         
        self.menubar = Menu(self.root)  
        self.file = Menu(self.menubar,tearoff=0 , bg= 'light blue')  
        self.file.add_command(label="Add Sources", command=self.openAddSource)  
        self.file.add_command(label="Manage Sources", command=self.openViewSource)

        self.expenses = Menu(self.menubar, tearoff=0, bg='light blue')  
        self.expenses.add_command(label="Add Expenses", command=self.openAddExp)  
        self.expenses.add_command(label="Manage Expenses", command=self.openViewExp)
        self.expenses.add_command(label="Add Expense Category", command=self.openAddCat)
        self.expenses.add_command(label="Manage Expense Category", command=self.openViewCat)

        self.budget = Menu(self.menubar,tearoff=0 , bg= 'light blue')  
        self.budget.add_command(label="Add Budget", command=self.openAddBudget)  
        self.budget.add_command(label="Manage Budget", command=self.openViewBudget)


        # self.file.add_command(label="Edit Books" )
        # self.file.add_command(label="View racks")  
        # self.file.add_command(label="View Bills")  
  
        # self.file.add_separator()  
  
        # self.file.add_command(label="Exit", command=self.main_frame3.quit)  
  
        self.menubar.add_cascade(label="Source", menu=self.file)  
        self.menubar.add_cascade(label="Expenses", menu=self.expenses)  
        self.menubar.add_cascade(label="Budget", menu=self.budget)  
        self.edit = Menu(self.menubar, tearoff=0)  
        self.edit.add_command(label="Undo")


 
        self.root.config(menu=self.menubar)
        
        self.root.mainloop()
        


    def openAddSource(self):
        obj = sources1.sources_of_income()
        obj.mainframe(self.data)

    def openViewSource(self):
        obj = table_sources.table_sources()
        obj.mainframe(self.data)

    def openAddExp(self):
        obj = expenses.sources_of_expenses()
        obj.mainframe(self.data)

    def openViewExp(self):
        obj = table_expenses.table_expenses()
        obj.mainframe(self.data)
        
        
    def openAddCat(self):
        obj = addExpCat.expCat()
        obj.mainframe(self.data)

    def openViewCat(self):
        obj = viewExpCat.table_expCat()
        obj.mainframe(self.data)

    def openAddBudget(self):
        obj = addBudget.budget()
        obj.mainframe(self.data)
    
    def openViewBudget(self):
        obj = viewBudget.table_budget()
        obj.mainframe(self.data)
        
if __name__=="__main__":
    obj=dashboard()
    obj.mainframe()