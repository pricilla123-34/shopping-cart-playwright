from playwright.sync_api import expect
import pytest
from pages.productspage import Productspage
from pages.addtocartpage import AddToCartPage


class CartActions:
    def __init__(self,page):
        self.page = page
        self.products_p = Productspage(page)
        self.cart_p = AddToCartPage(page)  # Assuming AddToCartPage is defined in pages/addtocartpage.py

    def verify_cart_badge(self, expected_count):
        expect(
            self.products_p._shopping_cart_badge
        ).to_have_text(str(expected_count))
        return self
    
    def go_to_cart(self):
        self.cart_p = self.products_p.click_shopping_cart_icon()
        expect(self.page).to_have_url("https://www.saucedemo.com/cart.html")
        return self.cart_p
    
    def verify_cart_item(self, product_name):
        self.cart_item_names = self.cart_p.get_cart_item_names()
        return self
    