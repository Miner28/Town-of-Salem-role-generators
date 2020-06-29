from classes import *
from tkinter import Button
players = []

for player in range(15):
    players.append(Player(player + 1))

def make_buttons(master, buttonlist, self):
    buttons = []
    for button in buttonlist:
        b = Button(master, activebackground="#ececec", activeforeground="#000000", background="#d9d9d9", disabledforeground="#a3a3a3", font="-family Arial -size 15 -weight bold -slant roman -underline 0 -overstrike 0", foreground="#0080ff", highlightbackground="#d9d9d9", text=button)
        buttons.append(b)
    return buttons
currentplayer = players[0]
