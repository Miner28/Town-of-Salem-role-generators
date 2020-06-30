from tkinter import Button, Frame, Label
import random
from classes import *


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


def make_actions(self, role: Role, players, lower=True):
    actions = role.actions
    try:
        self.actionSelect.destroy()
    except:
        pass
    self.actionSelect = Frame(self.Frame1)
    self.actionSelect.place(relx=0.0, rely=0.135, relheight=0.791, relwidth=0.745)
    if lower:
        self.actionSelect.lower(belowThis=self.roleSelect)
        self.actionSelect.lift(aboveThis=self.playerSelect)
    self.actionSelect.configure(relief="groove")
    self.actionSelect.configure(background="#d9d9d9")
    self.actionSelect.configure(highlightbackground="#d9d9d9")
    self.actionSelect.configure(highlightcolor="#00ff40")
    print(actions)
    r=0
    for action in actions:
        if action == "attack":
            action_text = "Attack"
        elif action == "defend-other":
            action_text = "Defend player"
        elif action == "defend-self":
            action_text = "Defend self"
        elif action == "investigate":
            action_text = "Investigate"
        elif action == "douse":
            action_text = "Douse"
        elif action == "ignite":
            action_text = "Ignite"
        else:
            continue

        button = Button(self.actionSelect)
        button.configure(
            font="-family Arial -size 20 -weight bold -slant roman -underline 0 -overstrike 0", foreground="#0080ff",
            background="#d9d9d9", text=action_text, width=10, command=lambda frame=self.Frame1, s=self, p=players: make_player_list(frame, s, p))
        button.grid(row=r, column=0)
        r+=1

def make_player_list(frame, self, players):
    try:
        self.playerActionSelect.destroy()
    except:
        pass
    self.playerActionSelect = Frame(frame)
    self.playerActionSelect.place(relx=0.0, rely=0.135, relheight=0.791, relwidth=0.745)
    self.playerActionSelect.configure(relief="groove")
    self.playerActionSelect.configure(background="#d9d9d9")
    self.playerActionSelect.configure(highlightbackground="#d9d9d9")
    self.playerActionSelect.configure(highlightcolor="#00ff40")
    self.playerActionSelect.lift()
    r = 0
    c = 0
    for player in players:
        button = Button(self.playerActionSelect)
        button.configure(
            font="-family Arial -size 20 -weight bold -slant roman -underline 0 -overstrike 0", foreground="#0080ff",
            background="#d9d9d9", text=f"{player.pid} - {player.role.name}", width=10)
        button.grid(row=r, column=c)
        r += 1
        if r == 5:
            r = 0
            c += 1

