from SauceDemo.pages.inventory_page import InventoryPage

def test_sort_high_to_low(logged_in_page):
    page = logged_in_page

    inventory_page = InventoryPage(page)

    inventory_page.sort_high_to_low()


    page.select_option(
        ".product_sort_container",
        value="hilo"
    )

    prices = page.locator(".inventory_item_price").all_text_contents()

    prices = [
        float(price.replace("$",""))
        for price in prices
    ]

    assert prices == sorted(prices, reverse=True)