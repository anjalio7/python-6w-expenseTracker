

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import database
import table_expenses


class sources_of_expenses:
    def __init__(self):
        self.root = Toplevel()
        self.root.title('EXPENSES')
        self.root.geometry("1350x700")
        self.root.resizable(height=False, width=False)

    def mainframe(self, data):
        self.data = data

# inserting image

        self.image1 = ImageTk.PhotoImage(Image.open(
            "images/expenses.jpg").resize((1400, 800)))
        self.imagelabel = Label(self.root, image=self.image1)
        # self.imagelabel.pack(fill="both",expand="yes")
        self.imagelabel.place(x=0, y=0)


# creating right side frame

        self.main_frame2 = Frame(self.root, bg='white')
        self.main_frame2.place(x=705, y=100, width='400', height='500')


# right side image
        self.image2 = ImageTk.PhotoImage(
            Image.open("images/123.jpg").resize((350, 400)))
        self.imagelabel = Label(
            self.root, image=self.image2, activebackground="white", bd=0)
        self.imagelabel.place(x=730, y=150)

# # sources of button
#         self.label=Label(self.root,text="SOUCES\nOF\nINCOME", font=("yu gothic vi",25,"bold"),bg="white",fg="blue"  )
#         self.label.place(x=760,y=150)


# creaTING LEFT SIDE FRAME
        self.main_frame = Frame(self.root, bg='white')
        self.main_frame.place(x=305, y=100, width='410', height='500')

        self.label = Label(self.root, text="Expenses", font=(
            "yu gothic vi", 25, "bold"), bg="white", fg="blue")
        self.label.place(x=400, y=110)


################################### left side labeling #####################

# field dropdown box\

        self.sourceLabel = Label(self.root, text='Month', bg="white", font=(
            "yu gothic vi", 15), fg="#040405")
        self.sourceLabel.place(x=322, y=200)

        self.monOptions = ['January', 'February', 'march', 'April', 'May', 'June',
                           'July', 'August', 'September', 'October', 'November', 'December']
        self.monthDrop = ttk.Combobox(self.root, values=self.monOptions)
        self.monthDrop.place(x=500, y=205, width="250")
        self.monthDrop.bind("<<ComboboxSelected>>", self.getBudgets)

        self.CategoryLabel = Label(
            self.root, text='Category', bg="white", font=("yu gothic vi", 15), fg="blue")
        self.CategoryLabel.place(x=322, y=250)

        self.AmountLabel = Label(
            self.root, text='Amount', bg="white", font=("yu gothic vi", 15), fg="blue")
        self.AmountLabel.place(x=500, y=250)

        self.addBtn = Button(
            self.root, text='+', bg="white", font=("yu gothic vi", 10), fg="blue", command=self.fields)
        self.addBtn.place(x=700, y=250)

        # self.comboValue1 = StringVar()
        self.options = database.getCat((self.data[0], ))


# add button
        self.add_button = ImageTk.PhotoImage(
            Image.open("images/btn1.png").resize((250, 50)))
        self.imagelabel = Label(image=self.add_button, bg="white")
        self.imagelabel.place(x=370, y=500)

        self.addButton = Button(self.root, text="ADD", fg="white", bg="#3047ff", activebackground="#3047ff",
                                cursor="hand2", font=("yu gothic vi", 12, "bold"), bd=0, command=self.expense)

        self.addButton.place(x=389, y=515, width=200)

        self.xPos = 322
        self.yPos = 300
        self.i = 0

        self.root.mainloop()

    def fields(self):
        globals()[f"self.catDrop{self.i}"] = ttk.Combobox(
            self.root, values=self.options)
        globals()[f"self.catDrop{self.i}"].place(x=self.xPos, y=self.yPos)

        globals()[f"self.amountEntry{self.i}"] = Entry(self.root)
        globals()[f"self.amountEntry{self.i}"].place(
            x=self.xPos + 178, y=self.yPos)

        globals()[f"self.removeBtn{self.i}"] = Button(
            self.root, text='-', command=lambda j=self.i: self.getIndex(j))
        globals()[f"self.removeBtn{self.i}"].place(
            x=self.xPos + 378, y=self.yPos)

        self.yPos += 40

        self.i += 1

    def getIndex(self, j):
        self.i -= 1
        print(j)
        globals()[f"self.catDrop{j}"].destroy()
        globals()[f"self.amountEntry{j}"].destroy()
        globals()[f"self.removeBtn{j}"].destroy()

    def getBudgets(self, e):
        self.expAllowed = database.getBudget(
            (self.data[0], self.monthDrop.get()))
        if self.expAllowed is None:
            messagebox.showerror(
                'Alert', 'Add budget first for the choosen month.')
            self.root.destroy()
        else:
            self.expAllowed = int(self.expAllowed[0])

    def expense(self):
        sourceList = []
        for i in range(self.i):
            if globals()[f'self.catDrop{i}'].get() == '' or globals()[f"self.amountEntry{i}"].get() == '':
                messagebox.showerror('Alert', 'Please enter details.')
            else:
                a = globals()[f'self.catDrop{i}'].get().split()
                sourceList.append((self.data[0], a[0], globals()[
                                  f"self.amountEntry{i}"].get(), self.monthDrop.get()))
        # print(self.cityEntry.get())
        print(sourceList)

        if self.i == 0:
            messagebox.showerror('Alert', 'Please add source(s)')
        else:
            a = [int(i[2]) for i in sourceList]
            expMade = sum(a)
            if expMade > self.expAllowed:
                messagebox.showerror('Alert', 'Expenses exceeded your budget')
            for i in sourceList:
                self.data = i
                print(self.data)
                res = database.addExpenses(self.data)
                if res:
                    messagebox.showinfo(
                        'Success', 'categories added successfully.')
                    self.root.destroy()
                else:
                    messagebox.showerror('Error', 'Something went wrong.')


if __name__ == "__main__":
    obj = sources_of_expenses()
    obj.mainframe()
