
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk
import database
import login_page


class registerpage:
    def __init__(self):
        self.root = Tk()
        self.root.title('SIGNUP PAGE')
        self.root.geometry("1350x700")
        self.root.resizable(height=False, width=False)

    def mainframe(self):

        # inserting image

        self.image = ImageTk.PhotoImage(Image.open("images/background1.png"))
        self.imagelabel = Label(self.root, image=self.image)
        self.imagelabel.pack(fill="both", expand="yes")

        # creating left side frame

        self.main_frame = Frame(self.root, bg='#040405')
        self.main_frame.place(x=305, y=100, width='410', height='500')

        # left side image

        self.image1 = ImageTk.PhotoImage(Image.open("images/login.png"))
        self.imagelabel = Label(image=self.image1, bg="#040405")
        self.imagelabel.place(x=320, y=200)

        # creating right side frame

        self.main_frame2 = Frame(self.root, bg='#040405')
        self.main_frame2.place(x=705, y=100, width='400', height='500')

        self.label = Label(self.root, text="Sign Up", font=(
            "yu gothic vi", 25), bg="#040405", fg="white")
        self.label.place(x=830, y=110)

        self.label = Label(self.root, text="WELCOME", font=(
            "yu gothic vi", 25), bg="#040405", fg="white")
        self.label.place(x=440, y=110)

        self.image2 = ImageTk.PhotoImage(Image.open("images/hyy.png"))
        self.imagelabel = Label(image=self.image2, bg="#040405")
        self.imagelabel.place(x=820, y=160)

        ###############    Right side      #############################

        # Name

        self.nameLabel = Label(self.root, relief=SOLID, text='NAME :', bg="#040405", font=(
            "yu gothic vi", 15, "bold"), fg="white")
        self.nameLabel.place(x=732, y=285)
        self.nameValue = StringVar()
        self.nameWidget = Entry(self.root, textvariable=self.nameValue, highlightthickness="0",
                                relief=FLAT, fg="white", bg="#040405", cursor="xterm",
                                font=("yu gothic vi", 12, "bold"))
        separator = ttk.Separator(orient="horizontal")
        separator.place(in_=self.nameWidget, x=0,
                        rely=1.0, height=2, relwidth=1.0)
        self.nameWidget.place(x=835,  y=280, height=30, width=250)

        # username

        self.userLabel = Label(self.root, relief=SOLID, text='Username :', bg="#040405", font=(
            "yu gothic vi", 15, "bold"), fg="white")
        self.userLabel.place(x=722, y=335)
        self.entryValue1 = StringVar()
        self.entryWidget1 = Entry(self.root, textvariable=self.entryValue1, highlightthickness="0",
                                  relief=FLAT, fg="white", bg="#040405", cursor="xterm",
                                  font=("yu gothic vi", 12, "bold"))
        separator = ttk.Separator(orient="horizontal")
        separator.place(in_=self.entryWidget1, x=0,
                        rely=1.0, height=2, relwidth=1.0)
        self.entryWidget1.place(x=835,  y=330, height=30, width=250)

        # password

        self.passvalue = Label(self.root, text='Password :', bg="#040405", font=(
            "yu gothic vi", 15), fg="white")
        self.passvalue.place(x=722, y=385)
        self.passValue = StringVar()
        self.entryWidget2 = Entry(self.root, textvariable=self.passvalue, highlightthickness="0",
                                  relief=FLAT, bg="#040405", show="*", fg="white",
                                  font=("yu gothic vi", 12, "bold"))
        separator = ttk.Separator(orient="horizontal")
        separator.place(in_=self.entryWidget2, x=0,
                        rely=1.0, height=2, relwidth=1.0)
        self.entryWidget2.place(x=840,  y=380, height=30, width=250)

        # gender

        self.label = Label(self.root, text="Gender :",
                           bg="#040405", font=("yu gothic vi", 16), fg="white")
        self.label.place(x=735, y=440)

        self.genderOpt = ['Male', 'Female']
        self.genderDrop = ttk.Combobox(self.root, values=self.genderOpt)
        self.genderDrop.place(x=832, y=443, width=260, height=25)
        # self.genderOpt = Radiobutton(self.root, text='Male', value='male',
        #                              cursor="hand2", bg="#040405", fg="#0096FF", font=("yu gothic vi", 16))
        # self.genderOpt.place(x=850, y=440)

        # self.genderOpt = Radiobutton(self.root, value='female', text='Female',
        #                              cursor="hand2", bg="#040405", fg="#0096FF", font=("yu gothic vi", 16))
        # self.genderOpt.place(x=930, y=440)

        # sign in button

        self.image5 = ImageTk.PhotoImage(Image.open("images/btn1.png"))
        self.imagelabel = Label(image=self.image5, bg="#040405")
        self.imagelabel.place(x=750, y=482)

        self.loginButton = Button(self.root, text="SIGN UP", fg="white", bg="#3047ff", activebackground="#3047ff",
                                  cursor="hand2", font=("yu gothic vi", 12, "bold"), bd=0, command=self.registerUser)

        self.loginButton.place(x=763, y=500, width=250)

        # i have an account

        self.forgot = Button(self.root, text="I Have An Account", fg="aqua", bg="#040405", cursor="hand2",
                             font=("yu gothic vi", 12, "bold "), bd=0, activebackground="#040405", command=self.goLogin)
        self.forgot.place(x=820, y=550)

        self.root.mainloop()

    def goLogin(self):
        self.root.destroy()
        obj = login_page.loginpage()
        obj.mainframe()

    def registerUser(self):
        if self.entryWidget1.get() == '' or self.entryWidget2.get() == "" or self.nameWidget.get() == "" or self.genderDrop.get() == "":
            messagebox.showerror('Alert', 'All fields required')

        else:
            self.data = (
                self.entryValue1.get(),
                self.entryWidget2.get(),
                self.genderDrop.get(),
                self.nameValue.get()
            )
            print(self.data)
            res = database.registerUser(self.data)
            if res:
                messagebox.showinfo('Success', 'Registered Successfully')
                self.root.destroy()
                obj = login_page.loginpage()
                obj.mainframe()
            else:
                messagebox.showerror('Alert', 'Something went wrong.')


if __name__ == "__main__":
    obj = registerpage()
    obj.mainframe()
