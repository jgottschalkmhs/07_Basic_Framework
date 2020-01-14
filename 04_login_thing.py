from tkinter import *

class Main():

    def __init__(self, master):

        self.child_window = None

        self.master = master
        self.master.title("Main Window")

        self.button1 = Button(self.master, text="Click Me 1", command = self.Open1)
        self.button1.grid(row=0, column=0, sticky=W)
        self.button2 = Button(self.master, text="Click Me 2", command = self.Open2)
        self.button2.grid(row=0, column=2, sticky=W)
        self.button3 = Button(self.master, text="Close", command = self.Close)
        self.button3.grid(row=1, column=0, sticky=W)

    def Login(self):

        login_win = Toplevel(self.master)
        login_window = Login(login_win)
        login_window.Focus()
        #main_window.Hide()


    def Open1(self):
        if not self.child_window:
            second_window = Toplevel(self.master)
            window2 = Second(second_window)

    def Open2(self):
        if not self.child_window:
            third_window = Toplevel(self.master)
            window3 = Third(third_window)

    def Close(self):
        self.master.destroy()

    #def Hide(self):
        #self.master.withdraw()

    #def Appear(self):
        #self.master.deiconify()


class Second():

    def __init__(self, master):
        self.master = master
        self.master.title("Child 1 of Main")
        self.master.geometry("300x300")
        self.button4 = Button(self.master, text="Click Me 1", command = self.Open_Child)
        self.button4.grid(row=0, column=0, sticky=W)


    def Open_Child(self):
        second_child_window = Toplevel(self.master)
        window4 = Second_Child(second_child_window)

class Third():
    def __init__(self, master):
        self.master = master
        self.master.geometry("300x300")
        self.master.title("Child 2 of Main")

class Second_Child():
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x300")
        self.master.title("Child of 'Child 1 of Main'")

class Login():
    def __init__(self, window):

        self.window = window
        self.window.title("Current Library")

        Label(self.window, text="Log in to use this program:").grid(row=0, column=0, sticky=W)

        self.userbox=Entry(self.window, width=20, bg="light green")
        self.userbox.grid(row=1, column=0, sticky=W)

        self.passbox=Entry(self.window, width=20, bg="light green")
        self.passbox.grid(row=2, column=0, sticky=W)

        Button(self.window, text="Submit", width=5, command=self.clicked).grid(row=3, column=0, sticky=W)

    def Focus(self):
        self.window.attributes('-topmost', 1)
        self.window.grab_set()

    def clicked(self):
        username = self.userbox.get()
        password = self.passbox.get()
        if password == "password" and username == "username":
            self.correct = True
            self.window.grab_release()
            self.window.destroy()
        else:
            pass

root_window = Tk()
root_window.geometry("200x100")

main_window = Main(root_window)
main_window.Login()

root_window.mainloop()
