from config import APP_NAME, VERSION
from database import connect
from logger import log
from moderator import Moderator
from memory import Memory
from agents import Agent


def main():
    print("=" * 50)
    print(APP_NAME)
    print(f"Version: {VERSION}")
    print("=" * 50)

    log("Starting system...")

    connect()

    moderator = Moderator()
    moderator.start()

    memory = Memory()
    memory.initialize()

    chatgpt = Agent("ChatGPT", "Strategist")
    gemini = Agent("Gemini", "Research")
    grok = Agent("Grok", "Trends")

    chatgpt.introduce()
    gemini.introduce()
    grok.introduce()

    log("Conference system ready.")

    print("=" * 50)
    print("AI Conference Room is ONLINE")
    print("=" * 50)


if __name__ == "__main__":
    main()
