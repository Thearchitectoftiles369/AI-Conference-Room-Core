from logger import log


class Conference:

    def __init__(self, topic):
        self.topic = topic

    def start(self):
        log("Conference started.")
        print()
        print(f"Topic: {self.topic}")
        print("Phase: Understanding the Problem")
        print()
