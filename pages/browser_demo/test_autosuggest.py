import pytest
from playwright.sync_api import Page, expect

def test_auto_sugg(set_up_tear_down: Page) -> None:
    page = set_up_tear_down
    page.goto("https://www.redbus.in/")
    # Wait for page load
    page.wait_for_load_state("networkidle")
    # Locate and click source input field
    from_section = page.locator("//div[contains(text(),'From')]")
    from_section.click()
    page.wait_for_timeout(3000)  # Wait for the dropdown to appear
    from_section.type("Bangalore")
    from_section.press("Enter")
    page.wait_for_timeout(3000)  # Wait for the suggestions to load
    auto_suggest = page.locator("//div[@class='listHeader___db864f']")
    # auto_suggest = page.locator("//div[@role='button']//div[1]//div[2]//div[1]//div[1]//div[1]")
    # auto_suggest = page.locator("inputWrapper___017bdb", has = page.locator("div", has_text="Popular Boarding Point near you"))
    page.wait_for_timeout(3000)  # Wait for the suggestions to appear
    all_suggestions = auto_suggest.all()
    print("\nAvailable suggestions:")
    for suggestion in all_suggestions:
        print(f"- {suggestion.inner_text()}")

    # Verify the first suggestion
    first_suggestion = auto_suggest.first
    # expect(first_suggestion).to_have_text("Bangalore")
    # Click the first suggestion
    first_suggestion.click()
    page.wait_for_timeout(3000)  # Wait for the selection to be processed
    


 