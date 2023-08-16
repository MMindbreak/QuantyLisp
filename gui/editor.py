import tkinter as tk
from tkinter import simpledialog, scrolledtext, Y


class Editor(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self._layout()

    def _layout(self):
        self.text_widget = scrolledtext.ScrolledText(self, wrap="word")
        self.text_widget.pack(fill=tk.BOTH, expand=True)
