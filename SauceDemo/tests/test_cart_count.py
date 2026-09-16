from playwright.sync_api import expect

def test_cart_count(logged_in_page):
    page = logged_in_page

    page.click("#add-to-cart-sauce-labs-backpack")
    page.click("#add-to-cart-sauce-labs-bike-light")
    page.click("#add-to-cart-sauce-labs-bolt-t-shirt")

    expect(
        page.locator(".shopping_cart_badge")
    ).to_have_text("3")
