from mainbot.main import DeskBot
from mainbot.mobile import MobileBot
import time

# Desktop Automated Testing
'''
with DeskBot() as bot:
    bot.homepage()
    bot.login_page()
    bot.login_details()

    bot.login_transition_load()
    bot.account_page()
    bot.address_book_page()
    bot.add_address()
    bot.fill_address()
    to_main = bot.switch_to_default_content()

    # clean up
    bot.delete_address()
'''

# Mobile Automated Testing
with MobileBot() as bot:
    bot.homepage()
    bot.hamburger_button()
    bot.login_page()
    bot.login_details()

    bot.login_transition_load()
    bot.hamburger_button()

    bot.accounts_page()
    bot.address_book_page()
    bot.add_address()
    bot.fill_address()
    to_main = bot.switch_to_default_content()

    # clean up
    bot.delete_address()
