from logger import log


class Memory:

    def __init__(self):
        self.history = []

    def initialize(self):
        log("Memory initialized.")

    def save(self, message):
        self.history.append(message)
        log("Memory updated.")
