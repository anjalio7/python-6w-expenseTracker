

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import database
import table_sources


class budget:
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

        self.sourceLabel = Label(
            self.root, text='Month', bg="white", font=("yu gothic vi", 15), fg="blue")
        self.sourceLabel.place(x=322, y=200)

        self.monOptions = ['January', 'February', 'march', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.monthDrop = ttk.Combobox(self.root, values=self.monOptions )
        self.monthDrop.place(x = 500, y = 200,width="250")

        # self.sourceEntry = Entry(self.root)
        # self.sourceEntry.place()

        self.incomeLabel = Label(
            self.root, text='Income', bg="white", font=("yu gothic vi", 15), fg="blue")
        self.incomeLabel.place(x=322, y=250)

        self.incomeEntry = Entry(self.root)
        self.incomeEntry.place(x = 500, y = 250)

        res  = database.allSources((self.userData[0], ))
        if res:
            a = [i[3] for i in res]
            self.incomeEntry.insert(0, sum(a))
            self.incomeEntry.config(state = 'readonly')

        self.expLabel = Label(self.root, text='Exp.\n Allowed', bg="white", font=("yu gothic vi", 15), fg="blue").place(x = 322, y = 300)

        self.expEntry = Entry(self.root)
        self.expEntry.place(x = 500, y = 300)


        
        res = database.singleBudget(self.sourceId)
        if res:
            self.monthDrop.insert(0, res[2])
            self.expEntry.insert(0, res[3])
        else:
            messagebox.showerror('Alert', 'Something went wrong.')


        self.addButton = Button(self.root, text="ADD", fg="white", bg="#3047ff", activebackground="#3047ff",
                                cursor="hand2", font=("yu gothic vi", 12, "bold"), bd=0, command=self.sources1)

        self.addButton.place(x=389, y=540, width=200)



        self.root.mainloop()


    def sources1(self):
        if self.monthDrop.get() == '':
            messagebox.showerror('Alert', 'Please enter income source')
        elif self.expEntry.get() == '':
            messagebox.showerror('Alert', 'Please enter income')
        else:
            self.data = (
                self.monthDrop.get(),
                self.expEntry.get(),
                self.sourceId[0]
            )
            print(self.data)
            res = database.updateBudget(self.data)
            if res:
                self.root.destroy()
                messagebox.showinfo('Success', 'Source updated successfully.')
            else:
                messagebox.showerror('Alert', 'Soemething went wrong.')

if __name__ == "__main__":
    obj = budget()
    obj.mainframe()
