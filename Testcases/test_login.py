from typing import Any
import pytest
from playwright.sync_api import sync_playwright,expect
from pages import loginpage
from pages.loginpage import Loginpage



def test_login(set_up: Any):
    page = set_up
    login_p = Loginpage(page)  # <-- Correct usage
    products_p = login_p.login("standard_user", "secret_sauce")

    expect(products_p.product_header).to_be_visible()
    expect(products_p.product_header).to_have_text("Products")

