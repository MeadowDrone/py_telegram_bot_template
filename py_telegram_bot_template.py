import telegram

def main():
    global LAST_UPDATE_ID

    # Telegram Bot Authorization Token
    bot = telegram.Bot('233195724:AAEIvsboAE0TYEaN3DXZ5xyXSIb0hkoTW4M')

    # This will be our global variable to keep the latest update_id when requesting
    # for updates. It starts with the latest update_id if available.
    try:
        LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
    except IndexError as TypeError:
        LAST_UPDATE_ID = None

    while True:
        brain(bot)


def brain(bot):
    """Defines the main behaviour of the bot."""
    global LAST_UPDATE_ID

    # Request updates after the last updated_id
    for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=20):
        try:
            if update.message:
                if update.message.text:
                    # The ID of the chat message received
                    chat_id = update.message.chat_id
                
                    # The content of the text received from the chat
                    text = update.message.text.encode("utf-8")
                    
                    # The first name of the user sending the message
                    first_name = update.message.from_user.first_name.encode("utf-8")
                
                    # Makes the bot send a "bot is typing..." action
                    bot.sendChatAction(
                            chat_id,
                            action=telegram.ChatAction.TYPING)

                    # Post a message
                    bot.sendMessage(update.message.chat_id, 
                            "Hi %s, you wrote:\n%s" % (first_name, text))

        except Exception as e:
            print("Error occurred:\n%s" % e)
        finally:
            # Updates global offset to get the new updates
            LAST_UPDATE_ID = update.update_id + 1

if __name__ == '__main__':
    main()
