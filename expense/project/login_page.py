#  creating a login page


from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import database
import sources1
import register_page, dashboard


class loginpage:
    def __init__(self):
        self.root = Tk()
        self.root.title('LOGIN PAGE')
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

        self.label = Label(self.root, text="WELCOME", font=(
            "yu gothic vi", 25), bg="#040405", fg="white")
        self.label.place(x=400, y=110)

        self.image1 = ImageTk.PhotoImage(Image.open("images/vector.png"))
        self.imagelabel = Label(image=self.image1, bg="#040405")
        self.imagelabel.place(x=350, y=150, height=450, width=350)

# creating right side frame

        self.main_frame2 = Frame(self.root, bg='#040405')
        self.main_frame2.place(x=705, y=100, width='400', height='500')

# right side image
        self.image2 = ImageTk.PhotoImage(Image.open("images/hyy.png"))
        self.imagelabel = Label(image=self.image2, bg="#040405")
        self.imagelabel.place(x=820, y=200)


# username right Side
        self.userLabel = Label(self.root, relief=SOLID, text='Username :',
                               bg="#040405", font=("yu gothic vi", 15), fg="white")
        self.userLabel.place(x=722, y=355)
        self.entryValue1 = StringVar()
        self.entryWidget1 = Entry(self.root, textvariable=self.entryValue1, highlightthickness="0",
                                  relief=FLAT, fg="white", bg="#040405", cursor="xterm",
                                  font=("yu gothic vi", 12, "bold"))
        separator = ttk.Separator(orient="horizontal")
        separator.place(in_=self.entryWidget1, x=0,
                        rely=1.0, height=2, relwidth=1.0)
        self.entryWidget1.place(x=850,  y=350, height=30, width=250)


# username image :
        self.image3 = ImageTk.PhotoImage(
            Image.open("images/username_icon.png"))
        self.imagelabel = Label(image=self.image3, bg="#040405")
        self.imagelabel.place(x=1070, y=352)

# ############################### Password ##############################################

        self.passvalue = Label(self.root, text='Password :', bg="#040405", font=(
            "yu gothic vi", 15), fg="white")
        self.passvalue.place(x=722, y=405)
        self.passValue = StringVar()
        self.entryWidget2 = Entry(self.root, textvariable=self.passvalue, highlightthickness="0",
                                  relief=FLAT, bg="#040405", show="*", fg="white",
                                  font=("yu gothic vi", 12, "bold"))
        separator = ttk.Separator(orient="horizontal")
        separator.place(in_=self.entryWidget2, x=0,
                        rely=1.0, height=2, relwidth=1.0)
        self.entryWidget2.place(x=850,  y=400, height=30, width=250)

# password image :
        self.image4 = ImageTk.PhotoImage(
            Image.open("images/password_icon.png"))
        self.imagelabel = Label(image=self.image4, bg="#040405")
        self.imagelabel.place(x=1070, y=400)

##################################LOGIN BUTTON##################################
        self.image5 = ImageTk.PhotoImage(Image.open("images/btn1.png"))
        self.imagelabel = Label(image=self.image5, bg="#040405")
        self.imagelabel.place(x=750, y=452)

        self.loginButton = Button(self.root, text="LOGIN", fg="white", bg="#3047ff", activebackground="#3047ff",
                                  cursor="hand2", font=("yu gothic vi", 12, "bold"), bd=0, command=self.login)

        self.loginButton.place(x=763, y=468, width=250)


###############################forgot password ########################

        self.forgot = Button(self.root, text="Forgot password ?", fg="white", bg="#040405", cursor="hand2",
                             font=("yu gothic vi", 12, "bold underline"), bd=0)
        self.forgot.place(x=820, y=510)

# new account

        self.new = Button(self.root, text="Sign Up", fg="white", bg="#040405", cursor="hand2",
                          font=("yu gothic vi", 12, "bold underline"), bd=0, command=self.goRegister)
        self.new.place(x=855, y=540)

        self.root.mainloop()


#     def loginpage (self):

#                 if self.entryWidget1.get() == '' or self.entryWidget2.get()=="" :
#                         messagebox.showerror('Alert', 'All fields required')

#                 res = database.login_page(self.data)

#                 if res:
#                         messagebox.showinfo('Success', 'Registered Successfully')
#                         self.root.destroy()
#                         obj =loginpage()
#                         obj.mainframe()
#                 else:
#                         messagebox.showerror('Alert', 'Something went wrong.')


    def goRegister(self):
        self.root.destroy()
        obj = register_page.registerpage()
        obj.mainframe()

    def login(self):
        if self.entryWidget1.get() == '' or self.entryWidget2.get() == "":
            messagebox.showerror('Alert', 'All fields required')

        else:
            self.data = (
                self.entryWidget1.get(),
                self.entryWidget2.get()
            )
            print(self.data)
            res = database.login_page(self.data)
            print(f'res is {res}')
            if res:
                messagebox.showinfo('Success', 'Login Successfully')
                self.root.destroy()
                obj = dashboard.dashboard()
                obj.mainframe(res)
            else:
                messagebox.showerror('Alert', 'Something went wrong.')


if __name__ == "__main__":
    obj = loginpage()
    obj.mainframe()
