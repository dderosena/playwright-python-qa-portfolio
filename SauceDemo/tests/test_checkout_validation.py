from playwright.sync_api import expect
from SauceDemo.pages.checkout_page import CheckoutPage

def test_checkout_requires_customer_info(logged_in_page):
    page = logged_in_page
    checkout_page = CheckoutPage(page)
    

    page.click("#add-to-cart-sauce-labs-backpack")
    page.click(".shopping_cart_link")
    page.click("#checkout")

    checkout_page.continue_checkout()

    # Don't enter any customer information

    page.click("#continue")

    expect(
        page.locator("[data-test='error']")
    ).to_contain_text("First Name is required")