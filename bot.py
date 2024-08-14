import telegram

class TradewizBot:
    def __init__(self, token):
        self.bot = telegram.Bot(token)

    def start(self):
        print('Bot is running...')

if __name__ == '__main__':
    bot = TradewizBot('YOUR_API_TOKEN')
    bot.start()