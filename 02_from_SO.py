# Source: https://stackoverflow.com/questions/50330378/python-3-tkinter-trying-to-stop-multiple-windows-from-opening-with-one-button

from tkinter import *


class OptionsWindow(Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        pass


class MainWindow(Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.options_toplevel = None
        Button(self, text='open toplevel', command=self._open_toplevel).pack()

    def _open_toplevel(self, *args):
        if self.options_toplevel is None:
            self.options_toplevel = Toplevel(self.master)
            self.options_toplevel.protocol('WM_DELETE_WINDOW', self.on_tl_close)
            gui = OptionsWindow(self.options_toplevel, width=300, height=300)
            gui.pack()

    def on_tl_close(self, *args):
        self.options_toplevel.destroy()
        self.options_toplevel = None


root = Tk()
gui = MainWindow(root)
gui.pack()
root.mainloop()
