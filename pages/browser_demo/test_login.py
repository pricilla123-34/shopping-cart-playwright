from playwright.sync_api import expect
import time


def test_01_login(set_up_tear_down) -> None:
    page = set_up_tear_down
    # succ_msg =page.locator('#flash').inner_text()
    # print(succ_msg)
    logout_button=page.locator(".button.secondary.radius")  
    # Verify we're on login page
    assert logout_button.is_visible(), "Logout button is not visible on the page"
    # Wait for and verify successful login message
    # expect(page.locator("div#flash.flash.success")).to_be_visible()
    # expect(page.locator("//div[@id='flash']")
    #    ).to_contain_text("You logged into a secure area!")

    # Click logout
    # page.locator("//a[@class='button secondary radius']").click()




def test_02_login_logout(set_up_tear_down):
    page = set_up_tear_down
    
    # Verify we're on secure page
    expect(page.locator("h2")).to_contain_text("Secure Area")
    
    # Click logout
    logout_button = page.locator(".button.secondary.radius")
    logout_button.click()
    
    # Verify logout success
    page.wait_for_load_state("networkidle")
    expect(page.locator("#flash")).to_contain_text("You logged out")
