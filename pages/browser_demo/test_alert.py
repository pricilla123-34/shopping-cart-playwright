import pytest
from playwright.sync_api import Page, expect


def test_handle_alert(set_up_tear_down: Page) -> None:
    page = set_up_tear_down
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.get_by_role("button", name="Click for JS Alert").click()
    page.on("dialog", lambda dialog: dialog.accept())
    result = page.locator("#result")
    expect(result).to_have_text("You successfully clicked an alert")

def test_handle_confirm(set_up_tear_down: Page) -> None:
    page = set_up_tear_down
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    page.wait_for_load_state("networkidle")
    
    # Set up dialog handler before clicking
    def handle_dialog(dialog):
        print(f"Dialog message: {dialog.message}")  # Changed from dialog.message() to dialog.message
        dialog.accept()
    
    # Use once() to handle single dialog
    page.once("dialog", handle_dialog)
    
    # Click button to trigger confirm dialog
    confirm_button = page.get_by_role("button", name="Click for JS Confirm")
    confirm_button.click()
    
    # Wait for and verify result
    result = page.locator("#result")
    result.wait_for(state="visible")
    expect(result).to_have_text("You clicked: Ok")


def test_handle_prompt(set_up_tear_down: Page) -> None:
    page = set_up_tear_down
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    
    # Set up dialog handler before triggering the prompt
    page.on("dialog", lambda dialog: dialog.accept("New to automation"))
    page.wait_for_timeout(2000)
    
    # Click the button to trigger prompt
    alert_button = page.locator("button:has-text('Click for JS Prompt')")
    alert_button.click()
    
    # Wait for result and verify
    result = page.locator("#result")
    
    expect(result).to_have_text("You entered: New to automation")
    print(f"Result text: {result.text_content()}")

