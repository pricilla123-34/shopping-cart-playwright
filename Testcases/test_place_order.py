from playwright.sync_api import expect
from pages.loginpage import Loginpage
from pages.productspage import Productspage
from pages.addtocartpage import AddToCartPage
from pages.placeorderpage import PlaceOrderPage


def test_place_order(set_up):
    page = set_up
    login_p = Loginpage(page)
    products_p = Productspage(page)
    login_p.login("standard_user", "secret_sauce")
    product_names = ['Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Backpack']
    for product_name in product_names:
        products_p.add_product_to_cart(product_name)
    if not product_name:
        raise AssertionError(f"Product '{product_name}' not found on the page.")
    
    cart_p = products_p.click_shopping_cart_icon()
    cart_p.click_checkout()
    place_p = PlaceOrderPage(page)
    place_p.enter_shipping_info("John", "Doe", "12345")
    place_p.click_continue()
    place_p.click_finish()
    confirmation_message = place_p.get_confirmation_message()
    expect(confirmation_message).to_have_text("Thank you for your order!")




