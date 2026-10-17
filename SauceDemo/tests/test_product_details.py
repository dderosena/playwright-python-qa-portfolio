from playwright.sync_api import expect
from SauceDemo.pages.product_page import ProductPage

def test_product_details(logged_in_page):
    page = logged_in_page
    product_page = ProductPage(page)

    product_page.open_backpack()


    expect(page.locator(".inventory_details_name")).to_have_text(
        "Sauce Labs Backpack"
    )

    expect(page.locator(".inventory_details_price")).to_have_text(
        "$29.99"

    )

    expect(page.locator(".inventory_details_desc")).not_to_be_empty()