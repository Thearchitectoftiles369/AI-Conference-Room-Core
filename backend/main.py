from config import APP_NAME, VERSION
from database import connect
from logger import log


def main():
    print("=" * 50)
    print(APP_NAME)
    print(f"Version: {VERSION}")
    print("=" * 50)

    log("Starting system...")
    connect()
    log("System ready.")


if __name__ == "__main__":
    main()
