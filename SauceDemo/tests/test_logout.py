from playwright.sync_api import expect
from SauceDemo.pages.inventory_page import InventoryPage

def test_logout(logged_in_page):
    page = logged_in_page
    inventory_page = InventoryPage(page)
    
    inventory_page.logout()

    expect(page).to_have_url("https://www.saucedemo.com/")
    expect(page.locator("#login-button")).to_be_visible()
