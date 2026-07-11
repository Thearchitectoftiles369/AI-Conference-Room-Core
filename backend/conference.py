from logger import log


class Conference:

    def __init__(self, topic):
        self.topic = topic
        self.phase = "Understanding the Problem"

    def start(self):
        print()
        print("=" * 50)
        print("AI CONFERENCE ROOM")
        print("=" * 50)

        log("Conference started.")

        print()
        print("Chairman:")
        print(f"> {self.topic}")

        print()
        print("Moderator:")
        print(f"Today's topic is: {self.topic}")

        print()
        print(f"Current Phase: {self.phase}")

        print()
        print("Moderator:")
        print("ChatGPT, you have the floor.")

        print("=" * 50)
