

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from tkinter import ttk
import database
import table_sources


class expCat:
    def __init__(self):
        self.root = Toplevel()
        self.root.title('Sources_of_income')
        self.root.geometry("1350x700")
        self.root.resizable(height=False, width=False)

    def mainframe(self, userData):

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

        self.nameLabel = Label(
            self.root, text='Name', bg="white", font=("yu gothic vi", 15), fg="blue")
        self.nameLabel.place(x=322, y=200)

        self.typeLabel = Label(
            self.root, text='Type', bg="white", font=("yu gothic vi", 15), fg="blue")
        self.typeLabel.place(x=500, y=200)

        self.addBtn = Button(
            self.root, text='+', bg = "white", font=("yu gothic vi", 10), fg="blue", command=self.fields)
        self.addBtn.place(x=700, y=200)


# add button
        # self.add_button = ImageTk.PhotoImage(
        #     Image.open("images/btn1.png").resize((250, 50)))
        # self.imagelabel = Label(image=self.add_button, bg="white")
        # self.imagelabel.place(x=370, y=530)

        self.addButton = Button(self.root, text="ADD", fg="white", bg="#3047ff", activebackground="#3047ff",
                                cursor="hand2", font=("yu gothic vi", 12, "bold"), bd=0, command=self.sources1)

        self.addButton.place(x=389, y=540, width=200)



        # self.exit_button = ImageTk.PhotoImage(
        #     Image.open("images/5844.jpg").resize((30, 30)))
        # self.imagelabel = Label(image=self.exit_button, bg="white")
        # self.imagelabel.place(x=370, y=553)

        # self.exit = Button(self.root, text="Exit", fg="blue", bg="white", cursor="hand2",
        #                    font=("yu gothic vi", 18, "bold underline"), bd=0)
        # self.exit.place(x=310, y=550)

        self.xPos = 322
        self.yPos = 250
        self.i = 0

        self.root.mainloop()


    def fields(self):
        globals()[f"self.nameEntry{self.i}"] = Entry(self.root)
        globals()[f"self.nameEntry{self.i}"].place(x = self.xPos, y = self.yPos)

        option = ['Fixed', 'Variable']
        globals()[f"self.typeDrop{self.i}"] = Combobox(self.root, values=option)
        globals()[f"self.typeDrop{self.i}"].place(x = self.xPos + 178, y = self.yPos)

        globals()[f"self.removeBtn{self.i}"] = Button(self.root, text= '-', command = lambda j = self.i : self.getIndex(j))
        globals()[f"self.removeBtn{self.i}"].place(x = self.xPos + 378, y = self.yPos)

        self.yPos += 40
        
        self.i += 1 


    def getIndex(self, j):
        self.i -= 1
        print(j)
        globals()[f"self.nameEntry{j}"].destroy()
        globals()[f"self.typeDrop{j}"].destroy() 
        globals()[f"self.removeBtn{j}"].destroy()


    def sources1(self):
        sourceList = []
        for i in range(self.i):
            if globals()[f'self.nameEntry{i}'].get() == '' or globals()[f"self.typeDrop{i}"].get() == '':
                messagebox.showerror('Alert', 'Please enter details.')
            else:
                sourceList.append((self.userData[0], globals()[f'self.nameEntry{i}'].get(), globals()[f"self.typeDrop{i}"].get()))
        # print(self.cityEntry.get())
        print(sourceList)

        if self.i == 0:
            messagebox.showerror('Alert', 'Please add source(s)')
        else:
            for i in sourceList:
                self.data = i
                print(self.data)
                res = database.addExpCat(self.data)
                if res:
                    messagebox.showinfo('Success', 'categories added successfully.')
                    self.root.destroy()
                #     obj = manageArea.ManageArea()
                #     obj.showCity()
                else:
                    messagebox.showerror('Error', 'Something went wrong.')
        


if __name__ == "__main__":
    obj = expCat()
    obj.mainframe()
