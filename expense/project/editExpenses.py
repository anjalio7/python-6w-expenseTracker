

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import database
import table_sources


class expenses:
    def __init__(self):
        self.root = Toplevel()
        self.root.title('Sources_of_income')
        self.root.geometry("1350x700")
        self.root.resizable(height=False, width=False)

    def mainframe(self, sourceId, userData):

        self.sourceId = sourceId
        self.userData = userData

        # self.data = data
        # inserting image

        self.image1 = ImageTk.PhotoImage(
            Image.open("images/bgbg.jpg").resize((1350, 700)))
        self.imagelabel = Label(self.root, image=self.image1)
        # self.imagelabel.pack(fill="both",expand="yes")
        self.imagelabel.place(x=0, y=0)


# creating right side frame

        self.main_frame2 = Frame(self.root, bg='white')
        self.main_frame2.place(x=705, y=100, width='400', height='500')


# right side image
        self.image2 = ImageTk.PhotoImage(
            Image.open("images/sign1.png").resize((350, 400)))
        self.imagelabel = Label(
            self.root, image=self.image2, activebackground="white", bd=0)
        self.imagelabel.place(x=730, y=150)

# # sources of button
#         self.label=Label(self.root,text="SOUCES\nOF\nINCOME", font=("yu gothic vi",25,"bold"),bg="white",fg="blue"  )
#         self.label.place(x=760,y=150)


# creaTING LEFT SIDE FRAME
        self.main_frame = Frame(self.root, bg='white')
        self.main_frame.place(x=305, y=100, width='410', height='500')

        self.label = Label(self.root, text="WELCOME", font=(
            "yu gothic vi", 25, "bold"), bg="white", fg="blue")
        self.label.place(x=400, y=110)


################################### left side labeling #####################


# field in left side frame

        self.monthLabel = Label(
            self.root, text='Month', bg="white", font=("yu gothic vi", 15), fg="blue")
        self.monthLabel.place(x=322, y=200)

        self.monOptions = ['January', 'February', 'march', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.monthDrop = ttk.Combobox(self.root, values=self.monOptions )
        self.monthDrop.place(x=500,y=200 ,width="250")

        # self.sourceEntry = Entry(self.root)
        # self.sourceEntry.place(x = 500, y = 200)

        self.catLabel = Label(
            self.root, text='Category', bg="white", font=("yu gothic vi", 15), fg="blue")
        self.catLabel.place(x=322, y=250)

        option = database.getCat((self.userData[0], ))
        self.catDrop = ttk.Combobox(self.root, values=option)
        self.catDrop.place(x = 500, y = 250)

        self.amtLabel = Label(self.root, text='Amount', bg="white", font=("yu gothic vi", 15), fg="blue")
        self.amtLabel.place(x = 322, y = 300)

        self.amtEntry = Entry(self.root)
        self.amtEntry.place(x = 500, y = 300)

        # self.incomeEntry = Entry(self.root)
        # self.incomeEntry.place(x = 500, y = 350)

        
        res = database.singleExpense(self.sourceId)
        if res:
            self.monthDrop.insert(0, res[3])
            self.catDrop.insert(0, (res[0], res[1]))
            self.amtEntry.insert(0, res[2])

            self.monthDrop.config(state = 'readonly')
            self.catDrop.config(state = 'readonly')
        else:
            messagebox.showerror('Alert', 'Something went wrong.')


        self.addButton = Button(self.root, text="ADD", fg="white", bg="#3047ff", activebackground="#3047ff",
                                cursor="hand2", font=("yu gothic vi", 12, "bold"), bd=0, command=self.sources1)

        self.addButton.place(x=389, y=540, width=200)


        self.xPos = 322
        self.yPos = 250
        self.i = 0

        self.root.mainloop()


    def sources1(self):
        if self.monthDrop.get() == '':
            messagebox.showerror('Alert', 'Please select month')
        elif self.catDrop.get() == '':
            messagebox.showerror('Alert', 'Please select category')
        elif self.amtEntry.get() == '':
            messagebox.showerror('Alert', 'please enter amount')
        else:
            a = self.catDrop.get().split()
            self.data = (
                a[0],
                self.amtEntry.get(),
                self.monthDrop.get(),
                self.sourceId[0]                
            )
            print(self.data)
            res = database.updateExpenses(self.data)
            if res:
                self.root.destroy()
                messagebox.showinfo('Success', 'Source updated successfully.')
            else:
                messagebox.showerror('Alert', 'Soemething went wrong.')

if __name__ == "__main__":
    obj = expenses()
    obj.mainframe()
