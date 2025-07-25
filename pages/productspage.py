# Make sure this import path is correct

from playwright.sync_api import Page, Locator

from pages.addtocartpage import AddToCartPage


class Productspage:

    def __init__(self, page):
        self.page = page
        self._product_header = page.locator("span.title")
        self._item_name = page.locator("[data-test='inventory-item-name']")
        # self._add_to_cart_button = page.locator("//button[text()='ADD TO CART']")
        self._cart_link = page.locator("a.shopping_cart_link")
        self._all_add_to_cart_buttons = page.locator(
            "[data-test^='add-to-cart-']")
        self._shopping_cart_badge = page.locator("[data-test='shopping-cart-badge']")

        self._dynamic_add_to_cart = page.locator("//div[text()='Sauce Labs Bike Light' and @data-test='inventory-item-name']")
        self._remove_button = page.locator(
            "[data-test^='Remove-']")
 
    
    @property
    def product_header(self) -> Locator:  # Added type hint for clarity
        return self._product_header

    def get_all_product_names(self) -> list[str]:
        product_names = []
        self._item_name.first.wait_for(state="visible", timeout=10000)
        for item in self._item_name.all():
            product_names.append(item.inner_text())
        return product_names

    def get_first_product_name(self):
        first_item = self._item_name.first
        first_item.wait_for(state="visible", timeout=10000)
        return first_item.inner_text()

    def add_first_item_to_cart(self):
        """Clicks the 'Add to Cart' button for the first product displayed."""
        first_add_button = self._all_add_to_cart_buttons.first
        first_add_button.wait_for(state="visible", timeout=30000)
        first_add_button.click()
    
    

        """click add to cart button for the corresponding product."""
    def get_add_to_cart_button_for_product(self, product_name):
        return self.page.locator(f"//div[text()='{product_name}' and @data-test='inventory-item-name']/ancestor::div[@class='inventory_item']//button[starts-with(@data-test, 'add-to-cart')]")

    def add_product_to_cart(self, product_name):

        """Clicks the 'Add to Cart' button for a specific product by name."""
        add_button = self.get_add_to_cart_button_for_product(product_name)
        add_button.wait_for(state="visible", timeout=10000)
        add_button.click()

    def get_cart_badge_count(self) -> int:  # New method to get cart count
        """Returns the number of items in the cart from the badge."""
        self._shopping_cart_badge.wait_for(state="visible", timeout=10000)
        return int(self._shopping_cart_badge.count())

    # Renamed and added return type hint
    def click_shopping_cart_icon(self) -> AddToCartPage:
        """ Clicks the shopping cart icon/link and navigates to the cart page."""
        self._cart_link.wait_for(
            state="visible", timeout=10000)  # Wait for the cart link to be visible
        self._cart_link.click()
        return AddToCartPage(self.page)  # Return the next page object
    


