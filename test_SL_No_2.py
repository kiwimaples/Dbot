from mainbot.main import DeskBot
from mainbot.mobile import MobileBot
from selenium import webdriver

# Desktop Automated Testing
'''
with DeskBot() as bot:
    bot.homepage()
    bot.shop_page()
    bot.select_item()
    bot.select_item_size()
    bot.add_to_cart()

    # clean up
    bot.box_cart_page()
    bot.empty_cart_one_item()
'''

# Mobile Automated Testing
with MobileBot() as bot:
    bot.homepage()
    bot.hamburger_button()
    bot.shop_page()
    bot.select_item()
    bot.select_item_size()
    bot.add_to_cart()

    # clean up
    bot.box_cart_page()
    bot.empty_cart_one_item()