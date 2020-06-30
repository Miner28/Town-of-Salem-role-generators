from tkinter import StringVar
import json
with open("defs/roles.json", "r") as f:
    roles = json.load(f)
print(roles)


class Player:
    def __init__(self, pid):
        self.pid = pid
        self.name = ""
        self.role = None
        self.status = "Alive"
        self.doused = False




class Role:
    def __init__(self, rolename):
        role = roles[rolename]
        self.name = rolename
        self.type = role['type']
        self.attack = role['attack-type']
        self.defense = role['defense-type']
        self.priority = role['priority']
        self.sheriff = role['sheriff']
        self.classic_results = role['classic-results']
        self.coven_results = role['coven-results']
        self.actions = role['actions']
        try:
            self.defense_self_use = role['defense-type-self-use']
            self.defense_other = role['defense-type-other']
        except:
            self.defense_self_use = None
            self.defense_other = None

