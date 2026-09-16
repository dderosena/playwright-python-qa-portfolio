


def test_sort_high_to_low(logged_in_page):
    page = logged_in_page


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