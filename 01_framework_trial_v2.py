from tkinter import *
from functools import partial   # To prevent unwanted windows

# Uses 'partial' to prevent multiple instances of a window...


# Remember to name classes using CamelCase
class UserInput:
    def __init__(self, parent):

        # Initialise variables that need checking...

        # Set money / rounds to a STRING and make it 1
        how_much = StringVar()
        how_much.set("1")

        # contains formatting
        padding_x = 10
        padding_y = 10
        background_color = "light blue"

        # GUI
        self.user_input_frame = Frame(width=600, height=600,bg=background_color, padx=padding_x, pady=padding_y)
        self.user_input_frame.grid()

        # heading label (first row)
        self.user_input_heading = Label(self.user_input_frame, text="User Input",
                                        padx=padding_x, pady=padding_y, bg=background_color,
                                        font=("Arial", "16", "bold"))
        self.user_input_heading.grid(row=0)

        # Get User Input (second row)
        self.get_input_frame = Frame(self.user_input_frame, bg=background_color)
        self.get_input_frame.grid(row=1)

        # Label asking for Money (for example)
        self.how_much_lbl = Label(self.get_input_frame, text="Enter Amount",
                                  padx = padding_x, pady=padding_y, bg=background_color,
                                  font=("Arial", "12"))
        self.how_much_lbl.grid(row=0, column=0)

        self.how_much_entry = Entry(self.get_input_frame, width=5,
                                    textvariable=how_much)
        self.how_much_entry.grid(row=0, column=1)

        # Buttons frame (third row)
        self.button_frame = Frame(self.user_input_frame)
        self.button_frame.grid(row=2)

        # Buttons (Help and Play)
        self.play_button = Button(self.button_frame, text="Play", command=self.play)
        self.play_button.grid(row=0, column=0)

        self.help_button = Button(self.button_frame, text="Help", command=self.help)
        self.help_button.grid(row=0, column=1)

    def play(self):
        amount = self.how_much_entry.get()

        ok = "yes"
        # Check it's a valid (eg: an integer)
        try:
            int(amount)
        except ValueError:
            ok = "no"
            self.how_much_entry.config(bg="pink")

        if ok == "yes":
            Game(self, amount)

            # Either destroy main area or disable Play button.

    def help(self):
        print("You asked for help")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")


class Game:
    def __init__(self, partner, amount):
        print(amount)

        # disable play button
        partner.play_button.config(state=DISABLED)

        # Initialise variables
        self.var_gained = IntVar()
        self.var_lost = IntVar()

        self.var_balance=IntVar()
        self.var_balance.set(amount)

        # GUI Setup
        self.game_box = Toplevel()
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        # Heading Row
        self.heading_label = Label(self.game_frame, text="Heading",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Plus / Minus Row
        self.plus_minus_frame = Frame(self.game_frame)
        self.plus_minus_frame.grid(row=1)

        # Buttons!
        self.gain_btn = Button(self.plus_minus_frame, text="Gain",
                               padx=10, pady=10, command=self.gain)
        self.gain_btn.grid(row=0, column=0)

        self.lose_btn = Button(self.plus_minus_frame, text="Lose",
                               padx=10, pady=10, command=self.lose)
        self.lose_btn.grid(row=0, column=1)

        # Balance Label
        self.balance_frame = Frame(self.game_frame)
        self.balance_frame.grid(row=2)

        self.balance_label = Label(self.balance_frame, text="Balance...")
        self.balance_label.grid(row=0, column=0)

        # Quit Button

    def gain(self):
        # retrieve balance and add 1 to it
        balance = self.var_balance.get()
        balance += 1
        self.var_balance.set(balance)
        self.balance_label.configure(text="Balance: {}".format(balance))

    def lose(self):
        # retrieve balance and subtract 1 from it
        balance = self.var_balance.get()
        balance -= 1
        self.var_balance.set(balance)
        self.balance_label.configure(text="Balance: {}".format(balance))

class Help:
    def __init__(self, partner):

        background = "orange"

        # disable help button
        partner.help_button.config(state=DISABLED)

        # Sets up child window (ie: help box)
        self.help_box = Toplevel()
        # If users press cross at top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300, height=200, bg=background)
        self.help_frame.grid()

        how_heading = Label(self.help_frame, text="Help / Instructions", font="arial 10 bold", bg=background)
        how_heading.grid(row=0)

        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(column=0, row=1)

        dismiss_btn = Button(self.help_frame, text="Dismiss", width=10, bg="orange", font="arial 10 bold",
                             command=partial(self.close_help, partner))
        dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("User Input Goes Here")
    start_things = UserInput(root)
    root.mainloop()

