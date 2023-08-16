import tkinter as tk

from lang.Eval import quanty_lisp_eval
from lang.Read import quanty_lisp_parse


class SideMenu(tk.Frame):
    def __init__(self, get_code, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.get_code = get_code
        self._layout()

    def _layout(self):
        self.eval_button = tk.Button(self, text="Eval Code", command=self._eval)
        self.eval_button.pack(side=tk.TOP, padx=5, pady=5)

        self.output = tk.Text(self, state=tk.DISABLED)
        self.output.pack(side=tk.BOTTOM)

    def _eval(self):
        try:
            code = self.get_code()
            res = quanty_lisp_eval(quanty_lisp_parse(code))
            self.output.config(state=tk.NORMAL)
            self.output.insert("1.0", res)
            self.output.config(state=tk.DISABLED)
        except Exception as e:
            self.output.config(state=tk.NORMAL)
            self.output.insert("1.0", f"Something went wrong {e}")
            self.output.config(state=tk.DISABLED)
