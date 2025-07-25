import pytest
from playwright.sync_api import sync_playwright, expect

from Testcases.basetest import CartActions
from pages.loginpage import Loginpage


@pytest.fixture()
def set_up_tear_down():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.fixture()
def set_up(set_up_tear_down):
    page = set_up_tear_down
    page.set_viewport_size({"width": 1280, "height": 720})
    page.goto("https://www.saucedemo.com/",timeout=60000)
    return page

@pytest.fixture()
def login(set_up):
    """Fixture to log in and return the products page."""
    page = set_up
    login_p = Loginpage(page)
    products_p = login_p.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    return products_p


@pytest.fixture
def cart_actions_fixture(set_up):
    return CartActions(set_up)