from logger import log


class Agent:

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def introduce(self):
        log(f"{self.name} joined the conference as {self.role}.")
