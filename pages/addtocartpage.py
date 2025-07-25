# Assuming this file is pages/addtocartpage.py

from pages.placeorderpage import PlaceOrderPage


class AddToCartPage:
    def __init__(self, page):
        self.page = page
        self._cart_items = page.locator(".cart_item") # Locator for individual items in the cart
        self._checkout_button = page.get_by_role("button", name="Checkout")
        self._cart_item_name = page.locator(".inventory_item_name") # Name of item in the cart
        self.cart_items_locator = page.locator(".cart_item .inventory_item_name")
        

    def get_cart_item_names(self) -> list[str]:
        """
        Returns a list of names of all items currently displayed in the cart.
        """
        return self._cart_item_name.all_inner_texts()
        

    def get_number_of_items_in_cart(self) -> int:
        """
        Returns the total count of distinct cart items in the cart.
        """
        return self._cart_items.count()

    def click_checkout(self):
        """
        Clicks the 'Checkout' button on the cart page.
        """
        self._checkout_button.click()
        return PlaceOrderPage(self.page)  # Assuming placeorder is a function that initializes the next page
        # Depending on your application flow, this might return a CheckoutPage instance
        # return CheckoutPage(self.page)