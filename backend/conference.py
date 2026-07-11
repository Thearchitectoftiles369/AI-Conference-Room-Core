from logger import log


class Conference:

    def __init__(self, topic, agents):
        self.topic = topic
        self.phase = "Understanding the Problem"
        self.agents = agents

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

        for agent in self.agents:
            print()
            print("Moderator:")
            print(f"{agent.name}, you have the floor.")
            agent.speak()

        print()
        print("Moderator:")
        print("Phase 1 completed.")

        print("=" * 50)
