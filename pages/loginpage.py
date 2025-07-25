from playwright.sync_api import sync_playwright
from pages.addtocartpage import AddToCartPage
#  # Only if Productspage exists


class Loginpage:
    def __init__(self, page):
        self.page = page
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._login_button = page.get_by_role("button", name="Login")
      

    def enter_user_name(self, u_name):
        self._username.fill(u_name)
        return self

    def enter_password(self, pwd):
        self._password.fill(pwd)
        return self

    def click_login_button(self):
        self._login_button.click()
        return self
    
    
    def login(self, u_name, pwd):
        from pages.productspage import Productspage 
        self.enter_user_name(u_name)
        self.enter_password(pwd)
        self.click_login_button()
        return Productspage(self.page)
