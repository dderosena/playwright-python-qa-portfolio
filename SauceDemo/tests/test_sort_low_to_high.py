from SauceDemo.pages.inventory_page import InventoryPage

def test_sort_low_to_high(logged_in_page):
    page = logged_in_page

    inventory_page = InventoryPage(page)

    inventory_page.sort_low_to_high()


    prices = page.locator(".inventory_item_price").all_text_contents()

    prices = [
        float(price.replace("$", ""))
        for price in prices
    ]

    assert prices == sorted(prices)