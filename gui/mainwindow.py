import tkinter
import tkinter as tk

from gui.editor import Editor
from gui.sidemenu import SideMenu


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.title = "Quanty Lisp Editor"

        # always call last
        self.__layout__()

    def get_code(self):
        return self.editor.text_widget.get("1.0", tkinter.END)

    def show(self):
        self.root.mainloop()

    def __layout__(self):
        self.editor = Editor(self.root)
        self.editor.pack(side=tk.LEFT, padx=10, pady=10)  # padx and pady give some padding

        # Button on the right
        self.sidemenu = SideMenu(self.get_code, self.root)
        self.sidemenu.pack(side=tk.RIGHT)
