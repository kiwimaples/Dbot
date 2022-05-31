from mainbot.main import DeskBot
from mainbot.mobile import MobileBot
from selenium import webdriver

# Desktop Automated Testing
'''
with DeskBot() as bot:
    bot.homepage()
    bot.login_page()
    bot.login_details()
'''

# Mobile Automated Testing
with MobileBot() as bot:
    bot.homepage()
    bot.hamburger_button()
    bot.login_page()
    bot.login_details()