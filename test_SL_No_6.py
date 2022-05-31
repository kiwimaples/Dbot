from mainbot.main import DeskBot
from mainbot.mobile import MobileBot
import time

# Desktop Automated Testing
'''
with DeskBot() as bot:
    bot.homepage()
    bot.shop_page()
    try:
        bot.select_item()
        bot.select_item_size()
        bot.add_to_cart()
    except Exception as e:
        print(e)
    bot.box_cart_page()
    bot.checkout_page()
    bot.checkout_non_member()
    bot.checkout_non_member_fill_details()
'''

# Mobile Automated Testing
with MobileBot() as bot:
    bot.homepage()
    bot.hamburger_button()
    bot.shop_page()
    try:
        bot.select_item()
        bot.select_item_size()
        bot.add_to_cart()
    except Exception as e:
        print(e)
    bot.box_cart_page()
    bot.checkout_page()
    bot.checkout_non_member()
    bot.checkout_non_member_fill_details()

    bot.refresh()