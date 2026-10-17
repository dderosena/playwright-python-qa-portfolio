from playwright.sync_api import expect
from SauceDemo.pages.checkout_page import CheckoutPage

def test_checkout(logged_in_page):
    page = logged_in_page
    checkout_page = CheckoutPage(page)


    # Add item
    page.click("#add-to-cart-sauce-labs-backpack")
    
    # Go to cart
    page.click(".shopping_cart_link")
    
    # Checkout
    page.click("#checkout")
    checkout_page.enter_customer_info(
        "Dominique",
        "Derosena",
        "94568"
    )
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()
    print("Current URL:", page.url)
    print("Page text:", page.locator("body").inner_text())
    # Verify success
    expect(
        page.locator(".complete-header")
    ).to_have_text(
        "Thank you for your order!"
    )


