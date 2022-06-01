from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import mainbot.constant as const
import os
import time

# Choose which web app to test on
driver = webdriver.Firefox

# Change the parameters inside the brackets of the MobileBot if you want to test in different browsers
class MobileBot(driver):
    def __init__(self, driver_path=const.driver_path, teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(MobileBot, self).__init__()
        self.maximize_window()
        self.wait = WebDriverWait(self, 30)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    # Goes to destinated URL
    def homepage(self):
        self.get(const.MOBILE_URL)

    def hamburger_button(self):
        hamburger = self.find_element_by_css_selector('#header > div.top_section > div.top_cate.fold > svg > path')
        hamburger.click()

    # Goes to Login Page
    def login_page(self):
        homepage_to_login_page = self.find_element_by_link_text('LOGIN')
        homepage_to_login_page.click()

    # Insert Login Credentials
    def login_details(self):
        # Waiting for website/Ajax to fully load before inserting login credentials
        self.wait.until(lambda driver: driver.execute_script('return jQuery.active') == 0)
        self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

        add_login_id = self.find_element_by_id('member_id')
        add_login_id.send_keys(const.login)

        add_login_pw = self.find_element_by_id('member_passwd')
        add_login_pw.send_keys(const.password)

        enter_login_details = self.find_element_by_id('loginButton')
        enter_login_details.click()

    # Waits for Login to be complete before doing any further actions
    def login_transition_load(self):
        self.wait.until(EC.url_to_be(const.MOBILE_URL))
        self.wait.until(lambda driver: driver.execute_script('return jQuery.active') == 0)
        self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')

    def shop_page(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'SHOP')))
        homepage_to_shop_nav = self.find_element_by_link_text('SHOP')
        homepage_to_shop_nav.click()

        # Goes to selected shop page
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, const.shop_link)))
        homepage_to_shop_page = self.find_element_by_link_text(const.shop_link)
        homepage_to_shop_page.click()

    def select_item(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, const.shop_item)))
        shop_page_item = self.find_element_by_link_text(const.shop_item)
        shop_page_item.click()

    def select_item_size(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, const.item_size)))
        item_size = self.find_element_by_link_text(const.item_size)
        item_size.click()

    def add_to_cart(self):
        # Wait for website/Ajax to fully load
        self.wait.until(lambda driver: driver.execute_script('return jQuery.active') == 0)
        self.wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable((By.ID, 'actionCart')))
        add_to_cart = self.find_element_by_id('actionCart')
        add_to_cart.click()

    # Message box appears after successfully adding item to cart, this function closes that message box
    def cart_msgbox_close(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'popClose')))
        popup_close = self.find_element_by_id('popClose')
        popup_close.click()

    # Popup appears if adding same item to the cart, this function closes the popup
    def cart_popup_close(self, teardown=False):
        switch = self.switch_to_alert()

        if teardown:
            switch.accept()
        else:
            switch.dismiss()

    # Goes to Cart Page
    def box_cart_page(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'popCart')))
        msgbox_to_cart_page = self.find_element_by_id('popCart')
        msgbox_to_cart_page.click()

    # Goes to Checkout Page
    def checkout_page(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'checkout')))
        cart_to_checkout_page = self.find_element_by_id('checkout')
        cart_to_checkout_page.click()

    # In between page if checking out without being logged in, asks if you want to checkout as a non-member
    def checkout_non_member(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'nonMemberCheckout')))
        non_member_to_checkout_page = self.find_element_by_id('nonMemberCheckout')
        non_member_to_checkout_page.click()

    # Fill in checkout details as a non-member
    def checkout_non_member_fill_details(self):
        non_member_order_pw = self.find_element_by_id('order_password')
        non_member_order_pw.send_keys(const.pw)

        non_member_order_pw_confirm = self.find_element_by_id('order_password_confirm')
        non_member_order_pw_confirm.send_keys(const.pw_confirm)

        non_member_order_name = self.find_element_by_id('rname')
        non_member_order_name.send_keys(const.name)

        non_member_zip_code = self.find_element_by_id('btn_search_rzipcode')
        non_member_zip_code.click()

        to_active = self.switch_to_active_element()

        self.wait.until(EC.presence_of_element_located((By.ID,'zboo_keyword')))
        self.wait.until(EC.element_to_be_clickable((By.ID, 'zboo_keyword')))
        non_member_zip_text = self.find_element_by_id('zboo_keyword')
        non_member_zip_text.click()
        non_member_zip_text.send_keys(const.zip_code)

        non_member_zip_text.send_keys(Keys.ENTER)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div/div/div[3]/div/table/tbody/tr[1]/td[1]/a[1]')))
        non_member_address_1 = self.find_element_by_xpath('/html/body/div[6]/div/div/div[3]/div/table/tbody/tr[1]/td[1]/a[1]')
        non_member_address_1.click()

        to_main = self.switch_to_default_content()
        non_member_address_2 = self.find_element_by_id('raddr2')
        non_member_address_2.send_keys(const.address_2)

        non_member_phone_1 = self.find_element_by_id('rphone2_2')
        non_member_phone_1.send_keys(const.phone_1)

        non_member_phone_2 = self.find_element_by_id('rphone2_3')
        non_member_phone_2.send_keys(const.phone_2)

        non_member_email_1 = self.find_element_by_id('oemail1')
        non_member_email_1.send_keys(const.email_1)

        non_member_email_2 = self.find_element_by_id('oemail2')
        non_member_email_2.send_keys(const.email_2)

        non_member_payment_method = self.find_element_by_id('addr_paymethod1')
        non_member_payment_method.click()

        non_member_t_c = self.find_element_by_id('allAgree')
        non_member_t_c.click()

        checkout_to_payment_page = self.find_element_by_id('total_order_sale_price_view')
        checkout_to_payment_page.click()

    # Fill in checkout details as a member
    def checkout_member_fill_details(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'btn_search_rzipcode')))
        address_zip_code = self.find_element_by_id('btn_search_rzipcode')
        address_zip_code.click()

        to_main = self.switch_to_active_element()

        self.wait.until(EC.presence_of_element_located((By.ID, 'zboo_keyword')))

        self.wait.until(EC.element_to_be_clickable((By.ID, 'zboo_keyword')))
        member_zip_text = self.find_element_by_id('zboo_keyword')
        member_zip_text.send_keys(const.zip_code)
        member_zip_text.click()
        member_zip_text.send_keys(Keys.ENTER)

        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[6]/div/div/div[3]/div/table/tbody/tr[1]/td[1]/a[1]')))
        non_member_address_1 = self.find_element_by_xpath(
            '/html/body/div[6]/div/div/div[3]/div/table/tbody/tr[1]/td[1]/a[1]')
        non_member_address_1.click()

        to_main = self.switch_to_default_content()
        member_address_2 = self.find_element_by_id('raddr2')
        member_address_2.send_keys(const.address_2)

        member_phone_1 = self.find_element_by_id('rphone2_2')
        member_phone_1.send_keys(const.phone_1)

        member_phone_2 = self.find_element_by_id('rphone2_3')
        member_phone_2.send_keys(const.phone_2)

        member_payment_method = self.find_element_by_id('addr_paymethod1')
        member_payment_method.click()

        member_t_c = self.find_element_by_id('allAgree')
        member_t_c.click()

        checkout_to_payment_page = self.find_element_by_id('total_order_sale_price_view')
        checkout_to_payment_page.click()

    # deletes first item in cart
    def empty_cart_one_item(self, teardown=True):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div/div[1]/div[1]/div[2]/div/div/div/div[2]/ul/div/div/a')))
        remove_one = self.find_element_by_xpath('/html/body/div/div/div/div/div[1]/div[1]/div[2]/div/div/div/div[2]/ul/div/div/a')
        remove_one.click()
        time.sleep(1)
        switch = self.switch_to_alert()
        switch.accept()

    # Goes to address book page for members
    def accounts_page(self):
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'ACCOUNT')))
        homepage_to_account_page = self.find_element_by_link_text('ACCOUNT')
        homepage_to_account_page.click()

    def address_book_page(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'addressBook')))
        address_book_page = self.find_element_by_id('addressBook')
        address_book_page.click()

    def add_address(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'addAddr')))
        add_address_page = self.find_element_by_id('addAddr')
        add_address_page.click()

    # Fill address details
    def fill_address(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, 'ma_rcv_title')))
        address_title = self.find_element_by_id('ma_rcv_title')
        address_title.send_keys(const.name)
        address_name = self.find_element_by_id('ma_rcv_name')
        address_name.send_keys(const.name)

        address_zip_code = self.find_element_by_id('SearchAddress')
        address_zip_code.click()

        to_active = self.switch_to_active_element()

        self.wait.until(EC.element_to_be_clickable((By.ID, 'zboo_keyword')))

        zip_text = self.find_element_by_id('zboo_keyword')
        zip_text.send_keys(const.zip_code)
        zip_text.send_keys(Keys.ENTER)

        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/div/div/div[3]/div/table/tbody/tr[1]/td[1]/a[1]')))
        address_1 = self.find_element_by_xpath(
        '/html/body/div[2]/div/div/div[3]/div/table/tbody/tr[1]/td[1]/a[1]')
        address_1.click()

        to_main = self.switch_to_default_content()
        address_2 = self.find_element_by_id('address_addr2')
        address_2.send_keys(const.address_2)

        phone_1 = self.find_element_by_id('ma_rcv_mobile_no2')
        phone_1.send_keys(const.phone_1)

        phone_2 = self.find_element_by_id('ma_rcv_mobile_no3')
        phone_2.send_keys(const.phone_2)

        register_address = self.find_element_by_id('registerAddr')
        register_address.click()

    def delete_address(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[1]/form/div/div[1]/div[1]/div[2]/a[2]')))
        del_address = self.find_element_by_xpath('/html/body/div/div/div[1]/form/div/div[1]/div[1]/div[2]/a[2]')
        del_address.click()

        to_alert = self.switch_to_alert()
        to_alert.accept()

