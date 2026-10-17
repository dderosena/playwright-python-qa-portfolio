from SauceDemo.pages.inventory_page import InventoryPage
from playwright.sync_api import expect

def test_remove_item(logged_in_page):
    page = logged_in_page
    inventory_page = InventoryPage(page)

    inventory_page.add_backpack_to_cart
    inventory_page.remove_backpack

    expect(
        page.locator(".shopping_cart_badge")
    ).to_have_count(0)