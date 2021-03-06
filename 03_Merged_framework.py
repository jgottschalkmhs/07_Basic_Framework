from tkinter import *


# Class that prevents more than one window from opening??
class OptionsWindow(Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        pass


class UserInput(Frame):
    def __init__(self, master="none", **kwargs):
        super().__init__(master, **kwargs)

        self.options_toplevel = None

        print("hello world")

        # contains formatting
        padding_x = 10
        padding_y = 10
        background_color = "light blue"

        # GUI
        self.user_input_frame = Frame(master ,bg=background_color, padx=padding_x, pady=padding_y)
        self.user_input_frame.grid()

        # heading label (first row)
        self.user_input_heading = Label(self.user_input_frame, text="User Input",
                                        padx=padding_x, pady=padding_y, bg=background_color,
                                        font=("Arial", "16", "bold"))
        self.user_input_heading.grid(row=0)

        # Buttons frame (second row)
        self.button_frame = Frame(self.user_input_frame)
        self.button_frame.grid(row=1)

        # Buttons (Help and Play)
        self.play_button = Button(self.button_frame, text="Play", command=self.play)
        self.play_button.grid(row=0, column=0)

        self.help_button = Button(self.button_frame, text="Help", command=self.help)
        self.help_button.grid(row=0, column=1)

    def play(self):
        print("You pushed play")

    def help(self, *args):
        get_help = Help()

    def on_tl_close(self, *args):
        self.options_toplevel.destroy()
        self.options_toplevel = None


class Help:
    def __init__(self):

        # if help box not already open, open it...
        if self.help_frame is None:
            self.help_frame = Toplevel()
            self.help_frame.protocol('WM_DELETE_WINDOW', self.on_tl_close)

        background = "orange"

        self.help_frame = Frame(self.help_box, width=300, height=200, bg=background)
        self.help_frame.grid()

        how_heading = Label(self.help_frame, text="Help / Instructions", font="arial 10 bold", bg=background)
        how_heading.grid(row=0)

        self.help_text = Label(self.help_frame,
                               text="Help text normally goes here",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(column=0, row=1)

        dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="orange", font="arial 10 bold",
                             command=self.close_help)
        dismiss_btn.grid(row=2, pady=10)

    def close_help(self):
        # Put help button back to normal...
        self.help_box.destroy()
        self.options_toplevel = None

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("User Input Goes Here")
    start_things = UserInput(root)
    root.mainloop()
