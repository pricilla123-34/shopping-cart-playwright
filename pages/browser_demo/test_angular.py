import pytest
from playwright.sync_api import Page


def test_angular(set_up_tear_down: Page) -> None:
    page = set_up_tear_down
    
    # Navigate to Angular app
    page.goto("https://stackblitz.com/edit/angular-dfy6hf?file=src%2Fapp%2Fapp.component.ts", timeout=60000)
    
    # Wait for frame to load
    page.wait_for_load_state("networkidle")
    
    # Switch to preview frame and interact with elements
    frame = page.frame_locator("iframe#previewFrame")
    frame.locator("#undefined").click()
    page.wait_for_timeout(4000)  # Wait for the dropdown to appear
    
    # Wait for and click dropdown option
    option = frame.locator("//ul[@class='select-menu box']/li[contains(.,  'Label 2')]")
    option.wait_for(state="visible")
    option.click()
