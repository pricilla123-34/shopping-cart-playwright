import pytest
from playwright.sync_api import Page, expect
import time



def test_checkbox(set_up_tear_down) -> None:
    page = set_up_tear_down
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_timeout(5000)  # Wait for the page to load
    page.locator("//input[@class='form-check-input' and @type='checkbox']").first.check()
    # Wait for the checkbox to be checked
    # time.sleep(1)  # Wait for 3 seconds to observe the checkbox state change
    # Verify the checkbox is checked
    assert page.locator("//input[@class='form-check-input' and @type='checkbox']").first.is_checked(), "Checkbox is not checked"
    page.wait_for_timeout(1000)

    page.locator("//input[@class='form-check-input' and @type='checkbox']").first.uncheck()
    # # Verify the checkbox is unchecked
    assert not page.locator("//input[@class='form-check-input' and @type='checkbox']").first.is_checked(), "Checkbox is not unchecked"


# multiple check box to be checked
    #page.locator("//input[@class='form-check-input' and @type='checkbox']").nth(3).check()
    check_boxes=page.locator("//input[@class='form-check-input' and @type='checkbox']").all()
    for check_box in check_boxes:
        check_box.check()
        time.sleep(1)   
    for i in range(len(check_boxes)):
        assert check_boxes[i].is_checked(), f"Checkbox {i+1} is not checked"


# multiselect dropdown
def test_multiselect_dropdown(set_up_tear_down) -> None:
    page = set_up_tear_down
    
    # Navigate to the page
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_load_state("networkidle")
    
    # Locate the select element (not the options)
    dropdown = page.locator("//select[@id='country']")

    # dropdown.scroll_into_view_if_needed()
    # Print available options
    options = page.locator("//select[@id='country']/option")
    print("\nAvailable options:")
    for i in range(options.count()):
        print(options.nth(i).inner_text())


def test_multiselect_dropdown2(set_up_tear_down) -> None:
    page = set_up_tear_down
    
    # Navigate to the page
    page.goto("https://testautomationpractice.blogspot.com/")
    page.wait_for_load_state("networkidle")
    multi_sel = page.locator("//select[@id='colors']")
    multi_sel.scroll_into_view_if_needed()
    # Select multiple options
    selected_values = multi_sel.select_option(value=["yellow", "green", "blue"])
    print(f"Selected values: {selected_values}")
    page.wait_for_timeout(3000)  # Wait for the selection to take effect
    selected_options = multi_sel.locator("option:checked")
    print(f"Number of selected options: {selected_options.count()}")
    
    # Wait for the selection to take effect
    page.wait_for_timeout(1000)

    # Verify the selected options
    # expect(multi_sel).to_be_checked("yellow,green,blue")
    # Verify the selected options
    for option in selected_options.all():
        print(f"Selected option: {option.inner_text()}")
        page.wait_for_timeout(4000)
        # assert option.is_checked(), f"Option {option.inner_text()} is not selected"
