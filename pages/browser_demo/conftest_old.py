# conftest.py
import pytest
from playwright.sync_api import sync_playwright, Page, expect
import time


@pytest.fixture(scope="session")
def browser():
    """Session-scoped browser instance"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        yield browser
        browser.close()
         # Reduced sleep time


@pytest.fixture(scope="session")
def browser_context(browser):
    """Session-scoped browser context - reused across all tests"""
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()
    page.wait_for_load_state("networkidle")
    yield context
    context.close()  # Close context instead of sleep
    


@pytest.fixture()
def set_up_tear_down(browser_context):
    """Login fixture - creates new tab in same browser window"""
    page = browser_context.new_page()
    page.goto("http://the-internet.herokuapp.com/secure")
    page.wait_for_load_state("networkidle")  # Add wait after navigation
    yield page
    page.close()
 
