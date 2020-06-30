from tkinter import Button, Label
from roletypes import *
import random


def make_buttons(master, buttonlist, self):
    buttons = []
    for button in buttonlist:
        b = Button(master, activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                   disabledforeground="#a3a3a3",
                   font="-family Arial -size 15 -weight bold -slant roman -underline 0 -overstrike 0",
                   foreground="#0080ff", highlightbackground="#d9d9d9", text=button)
        buttons.append(b)
    return buttons


def set_buttons(self, items, frame):
    row = 0
    col = 0
    for x, y in items.items():
        row = 1
        button = Button(frame)
        button.configure(
            font="-family Arial -size 20 -weight bold -slant roman -underline 0 -overstrike 0", foreground="#0080ff",
            background="#d9d9d9", text=x, width=10)
        button.configure(command=lambda rlist=y, s=self: choose_random(rlist, s))
        button.grid(row=0, column=col)
        for button in make_buttons(frame, y, self):
            button.grid(row=row, column=col)
            button.configure(width=14, command=lambda role=button["text"]: self.set_role(role))
            row += 1
        col += 1


def choose_random(rlist, self):
    self.set_role(random.choice(rlist))
