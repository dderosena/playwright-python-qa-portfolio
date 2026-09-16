from playwright.sync_api import expect

def test_checkout(logged_in_page):
    page = logged_in_page

    # Add item
    page.click("#add-to-cart-sauce-labs-backpack")
    
    # Go to cart
    page.click(".shopping_cart_link")
    
    # Checkout
    page.click("#checkout")

    # Enter customer info
    page.fill("#first-name", "Dominique")
    page.fill("#last-name", "Derosena")
    page.fill("#postal-code", "94568")

    # Continue
    page.click("#continue")

    # Finish order
    page.click("#finish")

    # Verify success
    expect(
        page.locator(".complete-header")
    ).to_have_text(
        "Thank you for your order!"
    )


