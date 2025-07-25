from typing import Any
from playwright.sync_api import sync_playwright, expect
from pages.loginpage import Loginpage
from pages.productspage import Productspage
from pages.addtocartpage import AddToCartPage



def test_add_to_cart1(login: Productspage, cart_actions_fixture: Any):
    """Test to verify that the user can add an item to the cart."""

    products_p = login
    my_cart_actions = cart_actions_fixture 
    first_product_name = products_p.get_first_product_name()
    if first_product_name is None:
        raise AssertionError("Could not retrieve the name of the first product.")
    print(f"First product: {first_product_name}")
    products_p.add_first_item_to_cart()

    my_cart_actions.verify_cart_badge(expected_count=1)
    my_cart_actions.go_to_cart()
    my_cart_actions.verify_cart_item(first_product_name)
    print(f"Items in cart: {my_cart_actions.cart_item_names}")
    expect(products_p._item_name).to_have_text(first_product_name)

def test_dynamic_add_to_cart(login: Productspage, cart_actions_fixture: Any):
    """Test to verify that the user can add a specific item to the cart using dynamic locator."""
    products_p = login
    my_cart_actions = cart_actions_fixture 
    product_name = 'Sauce Labs Bike Light'
    products_p.add_product_to_cart(product_name)
    my_cart_actions.verify_cart_badge(expected_count=1)
    my_cart_actions.go_to_cart()
    my_cart_actions.verify_cart_item(product_name)
    print(f"Items in cart: {my_cart_actions.cart_item_names}")
    expect(products_p._item_name).to_have_text(product_name)


def test_all_items_add_to_cart(login: Productspage, cart_actions_fixture: Any):
    products_p = login
    my_cart_actions = cart_actions_fixture 
    product_names = products_p.get_all_product_names()
    if not product_names:
        raise AssertionError("No products found on the page.")
    print(f"Product names: {product_names}")
    for product_name in product_names:
        products_p.add_product_to_cart(product_name)
    my_cart_actions.verify_cart_badge(expected_count=len(product_names))
    my_cart_actions.go_to_cart()
    for product_name in product_names:
        my_cart_actions.verify_cart_item(product_name)
    print(f"Items in cart: {my_cart_actions.cart_item_names}")   
    print(f"Total items in cart: {len(my_cart_actions.cart_item_names)}") 


def test_random_add_to_cart(login: Productspage, cart_actions_fixture: Any):
    products_p = login
    my_cart_actions = cart_actions_fixture 
    product_names = ['Sauce Labs Bike Light', 'Sauce Labs Bolt T-Shirt', 'Sauce Labs Backpack']
    for product_name in product_names:
        products_p.add_product_to_cart(product_name)
    if not product_name:
        raise AssertionError(f"Product '{product_name}' not found on the page.")
    
    my_cart_actions.verify_cart_badge(expected_count=len(product_names))
    my_cart_actions.go_to_cart()
    my_cart_actions.verify_cart_item(product_names)
    print(f"Items in cart: {my_cart_actions.cart_item_names}")
    print(f"Total items in cart: {len(my_cart_actions.cart_item_names)}")



