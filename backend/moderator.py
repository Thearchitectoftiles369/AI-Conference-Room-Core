from logger import log


class Moderator:

    def __init__(self):
        self.name = "Conference Moderator"

    def start(self):
        log(f"{self.name} is online.")
