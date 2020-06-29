from tkinter import StringVar
class Player:
    def __init__(self, pid):
        self.pid = pid
        self.name = ""
        self.role = None
        self.status = "Alive"



class Role:
    def __init__(self, role):
        self.name = role