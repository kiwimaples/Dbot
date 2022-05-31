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

    bot.shop_page()
    bot.select_item()
    bot.select_item_size()
    bot.add_to_cart()

    #clean up
    bot.box_cart_page()
    bot.empty_cart_one_item()
'''

# Mobile Automated Testing
with MobileBot() as bot:
    bot.homepage()
    bot.hamburger_button()
    bot.login_page()
    bot.login_details()

    bot.login_transition_load()
    bot.hamburger_button()

    bot.shop_page()
    bot.select_item()
    bot.select_item_size()
    bot.add_to_cart()

    # clean up
    bot.box_cart_page()
    bot.empty_cart_one_item()