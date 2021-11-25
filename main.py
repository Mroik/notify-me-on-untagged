from telegrambot import updater
from userbot import client


def main():
    client.start()
    updater.start_polling()
    client.run_until_disconnected()


if __name__ == "__main__":
    main()
