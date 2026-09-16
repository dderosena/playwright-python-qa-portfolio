from playwright.sync_api import expect

def test_remove_item(page):
    page.goto("https://www.saucedemo.com/")

    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.click("#add-to-cart-sauce-labs-backpack")
    page.click("#remove-sauce-labs-backpack")

    expect(
        page.locator(".shopping_cart_badge")
    ).to_have_count(0)