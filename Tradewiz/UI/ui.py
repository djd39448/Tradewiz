# UI Components for TradeWiz Bot

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

class TradeWizUI:
    def __init__(self):
        pass

    def start_buttons(self):
        keyboard = [[InlineKeyboardButton('Start', callback_data='start')]]
        return InlineKeyboardMarkup(keyboard)

    def handle_message(self, update, context):
        # Handle incoming messages
        pass

if __name__ == '__main__':
    ui = TradeWizUI()
    print(ui.start_buttons())
