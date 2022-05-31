import os

BASE_URL = 'https://www.dempuraworks.com/'
MOBILE_URL = 'https://m.dempuraworks.com/'
login = '' # removed for privacy/security
password = '' # removed for privacy/security
shop_link = 'DEMPURAWORKS 0' # Sample taget test link
shop_item = 'OVERSHIRT' # Sample target test link
item_size = 'ONE SIZE' # Sample target test link
item_cart = 'ADD TO CART'

# test browser file path
dirname = os.path.dirname(__file__)
driver_path = ':' + dirname + os.sep + os.pardir + '/Dbot_automated_tests/'

# Sample text for filling form
name = 'Test Automation'
pw = 'Abc1234'
pw_confirm = 'Abc1234'
zip_code = '1234'
address_2 = '123-321'
phone_1 = '000'
phone_2 = '0000'
email_1 = 'abc'
email_2 = 'gmail.com'
