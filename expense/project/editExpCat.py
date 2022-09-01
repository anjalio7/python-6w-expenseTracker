

from tkinter import *
from tkinter import messagebox
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
            self.root, text='Name', bg="white", font=("yu gothic vi", 15), fg="blue")
        self.sourceLabel.place(x=322, y=200)


        self.nameEntry = Entry(self.root)
        self.nameEntry.place(x = 500, y = 200)

        self.incomeLabel = Label(
            self.root, text='Type', bg="white", font=("yu gothic vi", 15), fg="blue")
        self.incomeLabel.place(x=322, y=350)

        option = ['Fixed', 'Variable']
        self.typeDrop = ttk.Combobox(self.root, values=option)
        self.typeDrop.place(x = 500, y = 350)

        
        res = database.singleExpcat(self.sourceId)
        if res:
            self.nameEntry.insert(0, res[0])
            self.typeDrop.insert(0, res[1])
        else:
            messagebox.showerror('Alert', 'Something went wrong.')


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


    # def fields(self):
    #     globals()[f"self.sourceEntry{self.i}"] = Entry(self.root)
    #     globals()[f"self.sourceEntry{self.i}"].place(x = self.xPos, y = self.yPos)

    #     globals()[f"self.incomeEntry{self.i}"] = Entry(self.root)
    #     globals()[f"self.incomeEntry{self.i}"].place(x = self.xPos + 178, y = self.yPos)

    #     globals()[f"self.removeBtn{self.i}"] = Button(self.root, text= '-', command = lambda j = self.i : self.getIndex(j))
    #     globals()[f"self.removeBtn{self.i}"].place(x = self.xPos + 378, y = self.yPos)

    #     self.yPos += 40
        
    #     self.i += 1 


    # def getIndex(self, j):
    #     self.i -= 1
    #     print(j)
    #     globals()[f"self.sourceEntry{j}"].destroy()
    #     globals()[f"self.incomeEntry{j}"].destroy() 
    #     globals()[f"self.removeBtn{j}"].destroy()


    def sources1(self):
        if self.nameEntry.get() == '':
            messagebox.showerror('Alert', 'Please enter category name')
        elif self.typeDrop.get() == '':
            messagebox.showerror('Alert', 'Please select type.')
        else:
            self.data = (
                self.nameEntry.get(),
                self.typeDrop.get(),
                self.sourceId[0]
            )
            print(self.data)
            res = database.updateExpcat(self.data)
            if res:
                self.root.destroy()
                messagebox.showinfo('Success', 'Category updated successfully.')
            else:
                messagebox.showerror('Alert', 'Soemething went wrong.')

if __name__ == "__main__":
    obj = expCat()
    obj.mainframe()
